from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart_list'),
    path('add-product-tp-cart', views.add_product, name='add-product'),
]
