from django.urls import path
from . import views

urlpatterns = [
    path('product-list/', views.product_list_view,name='product_list'),
    path('product-details/', views.product_details_view, name='product_details'),
]