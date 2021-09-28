from django import forms
from ManageApp.models import Product, Location, ProductMovement

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'



class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields='__all__'


class ProductMovementForm(forms.ModelForm):
    class Meta:
        model=ProductMovement
        fields='__all__'
