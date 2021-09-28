from django.shortcuts import render,redirect
from ManageApp.models import Product, Location, ProductMovement
from ManageApp.forms import ProductForm, LocationForm, ProductMovementForm

# Create your views here.

#PRODUCT
def product_inventory_table(request):
    products=Product.objects.all()
    return render(request,'ManageApp/product_inventory.html',{'products':products})

def product_retrieve_view(request,id):
    products=Product.objects.filter(product_id=id)
    return render(request,'ManageApp/product_inventory.html',{'products':products})

def product_create_view(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            product=request.POST['product']
            qty=request.POST['qty']
            warehouse=request.POST['warehouse']
            for instance in Product.objects.all():
                if instance.product == product and instance.warehouse==warehouse:
                    instance.qty+=int(qty)
                    instance.save()
                    return redirect('/product_index')
                form.save(commit=True)
        return redirect('/product_index')
    return render(request,'ManageApp/product_create.html',{'form':form})

def product_delete_view(request,id):
    products=Product.objects.filter(product_id=id)
    products.delete()
    return redirect('/product_index')

def product_update_view(request,id):
    products=Product.objects.get(product_id=id)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=products)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/product_index')
    return render(request,'ManageApp/product_update.html',{'products':products})


#LOCATION

def location_inventory_table(request):
    location=Location.objects.all()
    return render(request,'ManageApp/location_inventory.html',{'location':location})

def location_retrieve_view(request,id):
    location=Location.objects.filter(location_id=id)
    return render(request,'ManageApp/location_inventory.html',{'location':location})

def location_create_view(request):
    form=LocationForm()
    if request.method=='POST':
        form=LocationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/location_index')
    return render(request,'ManageApp/location_create.html',{'form':form})

def location_delete_view(request,id):
    location=Location.objects.filter(location_id=id)
    location.delete()
    return redirect('/location_index')

def location_update_view(request,id):
    location=Location.objects.get(location_id=id)
    if request.method=='POST':
        form=LocationForm(request.POST,instance=location)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/location_index')
    return render(request,'ManageApp/location_update.html',{'location':location})



#PRODUCTMOVEMENT
def product_movement_inventory_table(request):
    product_movement=ProductMovement.objects.all()
    return render(request,'ManageApp/product_movement_inventory.html',{'product_movement':product_movement})


def product_movement_retrieve_view(request,id):
    product_movement=ProductMovement.objects.filter(movement_id=id)
    return render(request,'ManageApp/product_movement_inventory.html',{'product_movement':product_movement})


def product_movement_create_view(request):
    form=ProductMovementForm()
    if request.method=='POST':
        form=ProductMovementForm(request.POST)
        if form.is_valid():
            id = request.POST['product_id']
            warehouse = request.POST['warehouse']
            qty = request.POST['qty']
            product=Product.objects.get(product_id=id)
            if product.warehouse==warehouse:
                product.qty-=int(qty)
                product.save()
            form.save(commit=True)
        return redirect('/productmovement_index')
    return render(request,'ManageApp/product_movement_create.html',{'form':form})

def product_movement_delete_view(request,id):
    product_movement=ProductMovement.objects.get(movement_id=id)
    product_movement.delete()
    return redirect('/productmovement_index')

def product_movement_update_view(request,id):
    product_movement=ProductMovement.objects.get(movement_id=id)
    if request.method=='POST':
        form=ProductMovementForm(request.POST,instance=product_movement)
        if form.is_valid():
            id = request.POST['product_id']
            warehouse = request.POST['warehouse']
            qty = request.POST['qty']
            product = Product.objects.get(product_id=id)
            if product.warehouse == warehouse:
                product.qty -= int(qty)
                product.save()
            form.save(commit=True)
        return redirect('/productmovement_index')
    return render(request,'ManageApp/product_movement_update.html',{'product_movement':product_movement})


def get_product_balance(request):
    products=Product.objects.all()
    return render(request,'ManageApp/my_inventory_management.html',{'products':products})



