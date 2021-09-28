from django.db import models
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product=models.CharField(max_length=100)
    warehouse=models.CharField(max_length=100)
    qty=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_id)


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.location


class ProductMovement(models.Model):
    movement_id = models.AutoField(primary_key=True)
    from_location=models.ForeignKey(Location,on_delete = models.CASCADE,related_name='from_location',blank=True, null=True)
    to_location=models.ForeignKey(Location,on_delete = models.CASCADE,related_name='to_location',blank=True, null=True)
    warehouse=models.CharField(max_length=100)
    product_id=models.ForeignKey(Product,on_delete = models.CASCADE,related_name='p_id')
    qty=models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

