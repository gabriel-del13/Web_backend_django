from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError

def validate_email(value):
    if '@' not in value:
        raise ValidationError('El email debe contener "@".')

def validate_password(value):
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
    if sum(c.isdigit() for c in value) < 2:
        raise ValidationError('La contraseña debe contener al menos 2 números.')

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    first_name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(3, 'El nombre debe tener al menos 3 caracteres.')]
    )
    last_name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(3, 'El apellido debe tener al menos 3 caracteres.')]
    )
    email = models.EmailField(
        unique=True,
        max_length=40,
        validators=[MinLengthValidator(3, 'El email debe tener al menos 3 caracteres.'), validate_email]
    )
    password = models.CharField(
        max_length=25,
        validators=[validate_password]
    )
    phone_number = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^\d{8}$',
                message="El número debe contener 8 dígitos."
            )
        ],
        blank=True, 
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
    
    
    """
    Creamos un CustomUserManager para manejar la creación de usuarios sin necesidad de un username.
    Modificamos el método save para establecer el username igual al email si no se proporciona.
    Eliminamos 'username' de REQUIRED_FIELDS.
    
    
    Modelo personalizado para usuarios que utiliza el modelo AbstractUser de Django.

    Este modelo utiliza el campo de correo electrónico como nombre de usuario y 
    agrega un campo de número de teléfono con validación personalizada.

    Atributos:
        email (EmailField): El correo electrónico del usuario. Este campo es único.
        phone_number (CharField): El número de teléfono del usuario. Debe seguir el formato 'xxxxxxxx'.
        USERNAME_FIELD (str): Campo que se utilizará como nombre de usuario para autenticación. En este caso, es el correo electrónico.
        REQUIRED_FIELDS (list): Campos requeridos al crear un superusuario. Aquí se incluyen 'username', 'first_name' y 'last_name'.
    """