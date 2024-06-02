from django.db import models

class Employee(models.Model):
    username = models.CharField(max_length=10)
    age = models.IntegerField(blank=True, null=True)
    aadhar_number = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  
    email = models.EmailField()

    def __str__(self):
        return self.username

class Employer(models.Model):
    username = models.CharField(max_length=10)
    company = models.CharField(max_length=255)
    aadhar_number = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  
    email = models.EmailField()

    def __str__(self):
        return self.username

class Customer(models.Model):
    username = models.CharField(max_length=10)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Job(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.name}"
