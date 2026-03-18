from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    session_id = models.CharField(max_length=255)

    def __str__(self):
        return self.session_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def get_total(self):
        return self.product.price * self.quantity
