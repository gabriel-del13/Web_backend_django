from django.db import models


##Category (name, created_at, updated_at)
class Category(models.Model):
    name_category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


##Product (name, description, price, available_quantity, images, status, created_at, updated_at)
class Product(models.Model):
    name_product = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available_quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, default='disponible')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if self.available_quantity == 0:
            self.status = 'agotado'
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')

# "./db/Products_db.png"