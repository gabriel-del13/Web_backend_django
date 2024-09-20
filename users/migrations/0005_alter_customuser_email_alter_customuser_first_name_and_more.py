# Generated by Django 5.0.7 on 2024-09-16 10:30

import django.core.validators
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.MinLengthValidator(3, 'El email debe tener al menos 3 caracteres.'), users.models.validate_email]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres.')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(3, 'El apellido debe tener al menos 3 caracteres.')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, validators=[users.models.validate_password]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator(message='El número debe contener 8 dígitos.', regex='^\\d{8}$')]),
        ),
    ]