from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+507\d{8}$',
                message="El número debe estar en formato: '+507xxxxxxxx'."
            )
        ],
        blank=True, 
        null= True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    
    """
    Modelo personalizado para usuarios que utiliza el modelo AbstractUser de Django.

    Este modelo utiliza el campo de correo electrónico como nombre de usuario y 
    agrega un campo de número de teléfono con validación personalizada.

    Atributos:
        email (EmailField): El correo electrónico del usuario. Este campo es único.
        phone_number (CharField): El número de teléfono del usuario. Debe seguir el formato '+507xxxxxxxx'.
        USERNAME_FIELD (str): Campo que se utilizará como nombre de usuario para autenticación. En este caso, es el correo electrónico.
        REQUIRED_FIELDS (list): Campos requeridos al crear un superusuario. Aquí se incluyen 'username', 'first_name' y 'last_name'.
    """