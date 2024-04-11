from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('details/<int:pid>/<slug:slug>', views.product_details_view, name='product_details'),
]
