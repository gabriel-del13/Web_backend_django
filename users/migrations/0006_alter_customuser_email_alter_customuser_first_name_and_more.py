# Generated by Django 5.0.7 on 2024-09-17 00:59

import django.core.validators
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_email_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=40, unique=True, validators=[django.core.validators.MinLengthValidator(3, 'El email debe tener al menos 3 caracteres.'), users.models.validate_email]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres.')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3, 'El apellido debe tener al menos 3 caracteres.')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=25, validators=[users.models.validate_password]),
        ),
    ]
