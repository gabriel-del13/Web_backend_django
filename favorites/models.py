from django.db import models
from django.conf import settings
from products.models import Product, Category, ProductImage

class Favorites(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.product.name_product}"

    @property
    def name_product(self):
        return self.product.name_product

    @property
    def price(self):
        return self.product.price

    @property
    def available_quantity(self):
        return self.product.available_quantity

    @property
    def images(self):
        return self.product.images.all()

    @property
    def category(self):
        return self.product.category

    @property
    def category_name(self):
        return self.product.category.name_category if self.product.category else None

    @property
    def status(self):
        return self.product.status

    @property
    def description(self):
        return self.product.description