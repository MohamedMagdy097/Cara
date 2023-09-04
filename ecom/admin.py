from django.contrib import admin
from .models import Customer, Shop, Product, ProductDetail, Site, Contact, People, Massage

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)
# navbar + footer + products
admin.site.register(Site)
admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(ProductDetail)
# contact + feedback
admin.site.register(Contact)
admin.site.register(People)
admin.site.register(Massage)