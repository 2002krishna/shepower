from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import Employee, Employer, Customer
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductImageForm
from .models import Product, ProductImage
from django.contrib.auth import logout

def base_view(request):
    return render(request, 'base.html')

def employee_home(request):
    return render(request, 'register_employee.html')

def employer_home(request):
    return render(request, 'register_employer.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def view_cart(request):
    return render(request, 'cart.html')

def buy(request):
    return render(request, 'thankyou.html')

def customer_home(request):
    return render(request, 'register_customer.html')

def view_jobs(request):
    return render(request, 'jobs.html')

def list_jobs(request):
    return render(request, 'view_jobs.html')

def sell_products(request):
    received_data = request.GET.get('data_to_send')
    username = received_data
    print(username)
    employee = Employee.objects.get(username=username)
    user = employee
    user_type = 'employee'
    context = {
        'user': user
    }
    return render(request, 'Sellproduct.html',context)

def error_page(request):
    return render(request,'home.html')

from django.shortcuts import render, redirect
from .forms import ProductForm, JobForm
from .models import ProductImage, Employee

def post_jobs(request):
    context = {}
    if request.method == 'POST':
        product_form = JobForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            return redirect('employer_home')
    else:
        product_form = JobForm()
    
    context['product_form'] = product_form
    return render(request, 'job_listing.html', context)
def register_product(request):
    received_data = request.GET.get('data_to_send')
    if received_data:
        username = received_data
        try:
            employee = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            return redirect('employer_home')
        user = employee
        user_type = 'employee'
        context = {
            'user': user
        }
    else:
        return redirect('employer_home')

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            for image in request.FILES.getlist('upload'):
                ProductImage.objects.create(product=product, image=image)
            return redirect('employee_home')
    else:
        product_form = ProductForm()
    
    context['product_form'] = product_form
    return render(request, 'Sellproduct.html', context)


from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import Employee, Employer, Customer

def login_view(request):
    if request.method == 'POST':
        print("entered")
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = None
        user_type = None
        
        # Check if the user is an employee
        try:
            print("entered employee")
            employee = Employee.objects.get(username=username)
            if password == employee.password:
                user = employee
                user_type = 'employee'
        except Employee.DoesNotExist:
            print("entered employee does not exist")
            print("error 1")
        
        # Check if the user is an employer
        if user is None:
            try:
                employer = Employer.objects.get(username=username)
                if password == employer.password:
                    user = employer
                    user_type = 'employer'
            except Employer.DoesNotExist:
                print("error 2")
        
        # Check if the user is a customer
        if user is None:
            try:
                customer = Customer.objects.get(username=username)
                if password == customer.password:
                    user = customer
                    user_type = 'customer'
            except Customer.DoesNotExist:
                print("error 3")
        
        # If user is authenticated, log them in
        if user is not None:
            context = {
                'user': user  # Pass the user variable to the template context
            }
            # Redirect to specific home page based on user type
            if user_type == 'employee':
                return render(request, 'register_employee.html', context)
            elif user_type == 'employer':
                return render(request, 'register_employer.html')
            elif user_type == 'customer':
                return render(request, 'register_customer.html')
        else:
            # If user authentication fails, show an error message
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        print("error 4")
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form})


def register_employee(request):
    print(request.method)
    print(request.POST.get('username'))
    if request.method == 'POST':
        # Assuming the form fields are named username, age, aadharNumber, mobileNumber, password, and email
        username = request.POST.get('username')
        age = request.POST.get('age')
        aadhar_number = request.POST.get('aadharNumber')
        mobile_number = request.POST.get('mobileNumber')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Create and save the employee object
        employee = Employee.objects.create(
            username=username,
            age=age,
            aadhar_number=aadhar_number,
            mobile_number=mobile_number,
            password=password,
            email=email
        )
        employee.save()
        
        # Redirect to a success page or home page
        return redirect('login')  # Replace 'home' with the name of your home URL pattern
    
    return render(request, 'register.html')

def register_employer(request):
    print(request.method)
    if request.method == 'POST':
        # Assuming the form fields are named username, company, mobileNumber, password, and email
        username = request.POST.get('username')
        company = request.POST.get('company')
        mobile_number = request.POST.get('mobileNumber')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # Create and save the employer object
        employer = Employer.objects.create(
            username=username,
            company=company,
            mobile_number=mobile_number,
            password=password,
            email=email
        )
        employer.save()
        
        # Redirect to a success page or homepage
        return redirect('login')  # Replace 'home' with the name of your home URL pattern
    
    return render(request, 'login.html')

def register_customer(request):
    print(request.method)
    if request.method == 'POST':
        # Assuming the form fields are named username, email, mobileNumber, password
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobileNumber')
        password = request.POST.get('password')
        
        # Create and save the customer object
        customer = Customer.objects.create(
            username=username,
            email=email,
            mobile_number=mobile_number,
            password=password
        )
        customer.save()
        
        # Redirect to a success page or homepage
        return redirect('login')  # Replace 'home' with the name of your home URL pattern
    
    return render(request, 'login.html')
