from django.db import models
from drf_yasg.utils import swagger_auto_schema

#Parent Category (name, created_at, updated_at)
class ParentCategory(models.Model):
    """
    Modelo que representa una categoría principal.

    Atributos:
        name_parentcategory (CharField): El nombre de la categoría principal, con un máximo de 50 caracteres.
        created_at (DateTimeField): Fecha y hora de creación de la categoría.
        updated_at (DateTimeField): Fecha y hora de la última actualización de la categoría.
    """
    name_parentcategory = models.CharField(
        max_length=50, 
        help_text="Nombre de la categoría principal (máximo 50 caracteres)."
        )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="Fecha y hora en que se creó la categoría."
        )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="Fecha y hora de la última actualización de la categoría."
        )
    
    def __str__(self):
        return self.name_parentcategory
   
   
# Category (name, created_at, updated_at)
class ChildCategory(models.Model):
    """
    Modelo que representa una subcategoría, la cual está vinculada a una categoría principal (ParentCategory).

    Atributos:
        name_childcategory (CharField): El nombre de la subcategoría, con un máximo de 50 caracteres.
        parent_category (ForeignKey): Relación hacia la categoría principal (ParentCategory). Si se elimina la categoría principal,
                                      las subcategorías asociadas también se eliminan (on_delete=models.CASCADE).
        created_at (DateTimeField): Fecha y hora de creación de la subcategoría.
        updated_at (DateTimeField): Fecha y hora de la última actualización de la subcategoría.
    """
    name_childcategory = models.CharField(
        max_length=50, 
        help_text="Nombre de la subcategoría (máximo 50 caracteres)."
    )
    parent_category = models.ForeignKey(
        ParentCategory, 
        on_delete=models.CASCADE, 
        related_name='subcategories',
        help_text="Categoría principal a la que pertenece esta subcategoría. Si la categoría principal se elimina, también se eliminará esta subcategoría."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="Fecha y hora en que se creó la subcategoría."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="Fecha y hora de la última actualización de la subcategoría."
    )

    def __str__(self):
        return f"{self.name_childcategory} (Subcategoría de {self.parent_category.name_parentcategory})"


# Product (name, description, price, available_quantity, images, status, created_at, updated_at)
from django.db import models
class Product(models.Model):
    """
    Modelo que representa un producto.

    Atributos:
        name_product (CharField): Nombre del producto, con un máximo de 50 caracteres.
        description (TextField): Descripción opcional del producto.
        price (DecimalField): Precio del producto, con un máximo de 6 dígitos, incluyendo dos decimales.
        available_quantity (PositiveIntegerField): Cantidad disponible del producto. Si es 0, el estado cambia a 'AGOTADO'.
        child_category (ForeignKey): Subcategoría (ChildCategory) a la que pertenece el producto.
        parent_category (ForeignKey): Categoría principal (ParentCategory) asociada al producto, asignada automáticamente en función de la subcategoría.
        status (CharField): Estado del producto (DISPONIBLE, AGOTADO o PRÓXIMAMENTE).
        created_at (DateTimeField): Fecha y hora en que se creó el producto.
        updated_at (DateTimeField): Fecha y hora de la última actualización del producto.
    """
    
    STATUS_CHOICES = [
        ('DISPONIBLE', 'disponible'),
        ('AGOTADO', 'agotado'),
        ('PRÓXIMAMENTE', 'próximamente'),
    ]
    
    name_product = models.CharField(
        max_length=50, 
        help_text="Nombre del producto (máximo 50 caracteres)."
    )
    description = models.TextField(
        null=True, 
        blank=True, 
        help_text="Descripción del producto (opcional)."
    )
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        help_text="Precio del producto, con un máximo de 6 dígitos incluyendo 2 decimales."
    )
    available_quantity = models.PositiveIntegerField(
        null=True, 
        blank=True, 
        help_text="Cantidad disponible del producto. Si es 0, el estado cambiará automáticamente a 'AGOTADO'."
    )
    child_category = models.ForeignKey(
        'ChildCategory', 
        on_delete=models.SET_NULL, 
        null=True, 
        help_text="Subcategoría a la que pertenece el producto."
    )
    parent_category = models.ForeignKey(
        'ParentCategory', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        help_text="Categoría principal asociada al producto. Se asigna automáticamente en función de la subcategoría."
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='DISPONIBLE', 
        help_text="Estado del producto: DISPONIBLE, AGOTADO o PRÓXIMAMENTE."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="Fecha y hora en que se creó el producto."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="Fecha y hora de la última actualización del producto."
    )
    
    def save(self, *args, **kwargs):
        """
        Sobrescribe el método save para establecer el estado del producto en 'AGOTADO' cuando la cantidad disponible es 0.
        Además, asigna automáticamente la categoría principal según la subcategoría seleccionada.
        """
        if self.available_quantity == 0:
            self.status = 'AGOTADO'
        if self.child_category:
            self.parent_category = self.child_category.parent_category
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_product


# ProductImage (image)
class ProductImage(models.Model):
    """
    Modelo que representa una imagen asociada a un producto.

    Atributos:
        product (ForeignKey): Relación hacia el producto (Product) al que pertenece la imagen.
        image (ImageField): Archivo de imagen asociado al producto, que se almacena en la carpeta 'products_images/'.
    """
    
    product = models.ForeignKey(
        'Product', 
        related_name='images', 
        on_delete=models.CASCADE,
        help_text="Producto al que está asociada esta imagen. Si el producto es eliminado, también se eliminará la imagen."
    )
    image = models.ImageField(
        upload_to='products_images/', 
        help_text="Archivo de imagen asociado al producto. La imagen se almacenará en la carpeta 'products_images/'."
    )
    
    def __str__(self):
        return f"Image for {self.product.name_product}"



