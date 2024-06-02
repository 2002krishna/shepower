from django import forms
from .models import Product, ProductImage, Job

class ProductForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('fashion', 'Fashion wear'),
        ('cooking', 'Cooking ingredients'),
        ('decor', 'Home decor'),
        ('health', 'Health and personal care'),
        ('fruits', 'Fruits and vegetables'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = ['name', 'details', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'details', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']
