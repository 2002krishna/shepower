"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from shepower.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', base_view, name='base'),
    path('login/', login_view, name='login'),
    path('logout/', base_view, name='logout'),
    path('register/', register, name='register'),
    path('register/employee/', register_employee, name='register_employee'),
    path('register/employer/', register_employer, name='register_employer'),
    path('register/customer/', register_customer, name='register_customer'),
    path('profile/', base_view, name='profile'),
    path('history/', base_view, name='history'),
    path('sellproducts/',sell_products, name="sell_products"),
    path('register_product/',register_product, name="register_product"),
    path('employee_home/',employee_home, name="employee_home"),
    path('employer_home/',employer_home, name="employer_home"),
    path('customer_home/',customer_home, name="customer_home"),
    path('error_page/',error_page, name="error_page"),
    path('products/', product_list, name='product_list'),
    path('product/edit/<int:product_id>/', edit_product, name='edit_product'),
    path('view_jobs/', view_jobs, name='view_jobs'),
    path('list_jobs/', list_jobs, name='list_jobs'),
    path('post_jobs/', post_jobs, name='post_jobs'),  
    path('view_cart/', view_cart, name='view_cart'),
    path('thankyou/', buy, name='buy'),
]

