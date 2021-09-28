from django.contrib import admin
from ManageApp.models import Product, Location, ProductMovement

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id','product','warehouse','qty','created','updated']


class LocationAdmin(admin.ModelAdmin):
    list_display=('location','created','updated')


class ProductMovementAdmin(admin.ModelAdmin):
    list_display=('movement_id','from_location','to_location','product_id','warehouse','qty','created','updated')


admin.site.register(Product,ProductAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(ProductMovement,ProductMovementAdmin)
