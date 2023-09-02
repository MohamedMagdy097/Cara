from django.contrib import admin
from .models import Customer, Shop, Product, ProductDetail, Site, Contact, People

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

admin.site.register(Site)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ProductDetail)

admin.site.register(Contact)
admin.site.register(People)