from django.db import models


# Category (name, created_at, updated_at)
class Category(models.Model):
    name_category = models.CharField(max_length=50) 
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.parent_category:
            return f"{self.name_category} (Subcategoría de {self.parent_category.name_category})"
        return self.name_category



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
    available_quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIBLE') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.available_quantity == 0:
            self.status = 'AGOTADO'
        super().save(*args, **kwargs)

# ProductImage (image)
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
