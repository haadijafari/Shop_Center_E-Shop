from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    # path('', views.home_page_view, name='home'),
    path('', views.HomeView.as_view(), name='home'),
]
