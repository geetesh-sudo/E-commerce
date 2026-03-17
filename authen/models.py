from django.db import models
from django.contrib.auth.models import User

class CartModel(models.Model):
    pname = models.CharField(max_length=50)
    price = models.IntegerField()
    pcategory = models.CharField(max_length=50)
    quantity = models.IntegerField()
    totalprice = models.IntegerField()
    host = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pname
