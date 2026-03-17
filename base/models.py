from django.db import models

class Products(models.Model):
    pname = models.CharField(max_length=25)
    pdesc = models.CharField(max_length=25)
    price = models.IntegerField()
    pcategory = models.CharField(max_length=50)
    trending = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)
    pimage = models.ImageField(upload_to='uploads/', default='Default.jpg')

    def __str__(self):
        return self.pname


class Update(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=15)

    def __str__(self):
        return self.username
