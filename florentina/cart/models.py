from django.db import models
from flowers.models import Flower

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Flower, unique=False)

    class Meta:
        db_table = 'cart_items'
        ordering = ['added_at']

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    def price(self):
        return self.product.price

    def get_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()
