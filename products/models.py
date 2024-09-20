from django.db import models


#Parent Category (name, created_at, updated_at)
class ParentCategory(models.Model):
    name_parentcategory = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name_parentcategory
    
"""
Modelo para las Categorias Padre, que es capaz de almacenar su nombre, 
obtener su fecha de creacion/actualizacion
"""   

# Category (name, created_at, updated_at)
class ChildCategory(models.Model):
    name_childcategory = models.CharField(max_length=50) 
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_childcategory} (Subcategoría de {self.parent_category.name_parentcategory})"


"""
Modelo para la clase Categorias que es capaz de almacenar su nombre, 
asociarla a una sub-categoriay obtener su fecha de creacion/actualizacion

Atributos: 
    name_category (CharField) = nombre de la categoria, 50 caracteres como maximo
    parent_category (ForeignKey) = Permite enlazar una categoria padre a una categoria, pudiendo crear subcategorias.
    created_at (DateTimeField) = Agrega automaticamente la fecha de creacion
    updated_at (DateTimeField) = Actualiza automaticamente a la ultima fecha de actualizacion
"""

# Product (name, description, price, available_quantity, images, status, created_at, updated_at)
class Product(models.Model):
    STATUS_CHOICES = [
        ('DISPONIBLE', 'disponible'),
        ('AGOTADO', 'agotado'),
        ('PRÓXIMAMENTE', 'próximamente'),
    ]
        
    name_product = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_quantity = models.PositiveIntegerField(null= True, blank= True)
    child_category = models.ForeignKey(ChildCategory, on_delete=models.SET_NULL, null=True)
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIBLE') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.available_quantity == 0:
            self.status = 'AGOTADO'
        super().save(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        if self.child_category:
            self.parent_category = self.child_category.parent_category
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_product

'''
Modelo para la clase Producto, cuenta con nombre, descripcion, 
precio, cantidad, categorias (del modelo category), estado, fecha de creacion/actualizacion
Atributos: 

    STATUS_CHOICES (list): Opciones para el estado del producto. Puede ser 'DISPONIBLE', 'AGOTADO' o 'PRÓXIMAMENTE'.
    name_product (CharField): Nombre del producto, con un límite máximo de 50 caracteres.
    description (TextField): Descripción del producto, puede ser nulo o estar en blanco.
    price (DecimalField): Precio del producto, con un máximo de 6 dígitos y 2 decimales.
    available_quantity (PositiveIntegerField): Cantidad disponible en stock del producto.
    category (ForeignKey): Categoría a la que pertenece el producto. Es una clave foránea que apunta al modelo Category y permite valores nulos.
    parent_category(ForeignKey): Categoria padre a la que pertenece el producto. Es una clave foránea que apunta al modelo ParentCategory y permite valores nulos.
    status (CharField): Estado actual del producto, basado en las opciones definidas en `STATUS_CHOICES`. El valor por defecto es 'DISPONIBLE'.
    created_at (DateTimeField): Fecha y hora de creación del producto, asignada automáticamente.
    updated_at (DateTimeField): Fecha y hora de la última actualización del producto, asignada automáticamente.

Métodos:
    save(*args, **kwargs): Sobrescribe el método `save` para actualizar el estado del producto a 'AGOTADO' si `available_quantity` es igual a 0.
'''

# ProductImage (image)
class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')

    def __str__(self):
        return f"Image for {self.product.name_product}"


    """
Modelo que representa las imágenes asociadas a un producto.

Atributos:
    product (ForeignKey): Clave foránea que enlaza la imagen con un producto específico. 
                          Utiliza `related_name='images'` para poder acceder a las imágenes relacionadas desde el producto.
    image (ImageField): Campo de imagen que almacena la ruta de la imagen subida. Las imágenes se guardarán en el directorio 'products_images/'.
    """