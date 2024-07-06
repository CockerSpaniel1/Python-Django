from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 64)
 

class Product(models.Model):
    #pid =models.PositiveBigIntegerField()
    name = models.CharField(max_length = 32)
    unit = models.CharField(max_length = 32)
    price = models.FloatField()
    supplierid = models.PositiveBigIntegerField()
    categoryid = models.PositiveBigIntegerField()
 

class Orderdetail(models.Model):
    no = models.PositiveBigIntegerField()
    date = models.DateField()
    pid = models.PositiveIntegerField()
    qty = models.PositiveIntegerField()
    cid = models.CharField(max_length = 4)
    channel = models.PositiveIntegerField()
 

class Member(models.Model):
    email = models.CharField(max_length = 64)
    pwd = models.CharField(max_length = 64)
    uname = models.CharField(max_length = 64)


 