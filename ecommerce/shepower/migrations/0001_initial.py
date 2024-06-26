# Generated by Django 5.0.6 on 2024-06-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('aadhar_number', models.CharField(max_length=12)),
                ('mobile_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
