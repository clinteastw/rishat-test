from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, default='usd')
    
    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=30, null=True)
    percentage = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_coupon_id = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Discount {self.percentage}%"
    

class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders', blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    
    def calculate_total_price(self):
        total_price = sum(item.price for item in self.items.all())
        
        if self.discount:
            total_price -= total_price * (self.discount.percentage / 100)
            
        self.total_price = total_price
        self.save()
        
    def __str__(self):
        return f"Order № {self.id}"