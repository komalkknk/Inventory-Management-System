"""komal_nitin_kale_inventory_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ManageApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product_index/', views.product_inventory_table),
    path('product_create/', views.product_create_view),
    path('product_update/<int:id>/', views.product_update_view),
    path('product_retrieve/<int:id>/', views.product_retrieve_view),
    path('product_delete/<int:id>/', views.product_delete_view),
    path('location_index/', views.location_inventory_table),
    path('location_create/', views.location_create_view),
    path('location_update/<int:id>/', views.location_update_view),
    path('location_retrieve/<int:id>/', views.location_retrieve_view),
    path('location_delete/<int:id>/', views.location_delete_view),
    path('productmovement_index/', views.product_movement_inventory_table),
    path('productmovement_create/', views.product_movement_create_view),
    path('productmovement_update/<int:id>/', views.product_movement_update_view),
    path('productmovement_retrieve/<int:id>/', views.product_movement_retrieve_view),
    path('productmovement_delete/<int:id>/', views.product_movement_delete_view),
    path('inventory_balance/', views.get_product_balance),
]
