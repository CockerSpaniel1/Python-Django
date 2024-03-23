from django.contrib import admin
from cafe.models import Product,Category,UserInfo

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(UserInfo)

