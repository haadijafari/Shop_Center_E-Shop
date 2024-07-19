from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart_list'),
    path('add-product-tp-cart', views.add_product, name='add-product'),
    path('remove-cart-detail', views.remove_cart_detail, name='remove_cart_detail_ajax'),
    path('change-cart-detail', views.change_cart_detail_count, name='change_cart_detail_count_ajax'),
]
