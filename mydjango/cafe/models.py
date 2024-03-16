from django.db import models

# Create your models here.
class Product(models.Model):
    SIZES={
        ("S", "SMALL"),
        ("M", "MEDIUM"),
        ("L", "LARGE"),
    } 

    pid = models.CharField(max_length = 5)
    name = models.CharField(max_length = 10)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length = 1,choices=SIZES )


class Category(models.Model):
    cid = models.PositiveIntegerField()
    name = models.CharField(max_length = 10)

class UserInfo(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 64)
 
