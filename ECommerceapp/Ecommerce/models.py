from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='Ecommerce/static/images/')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products=models.ManyToManyField(Items)
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"Order #{self.id} - User:{self.user.username}"
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Items,through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.username}"
    
class CartItem(models.Model):
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    products = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"
    