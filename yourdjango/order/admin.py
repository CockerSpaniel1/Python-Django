from django.contrib import admin
from order.models import  UserInfo,Product,Orderdetail,Member

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Product)
admin.site.register(Orderdetail)
admin.site.register(Member)

