from django.urls import path

from apps.index import views

app_name = 'index'

urlpatterns = [
    path('', views.home_page_view, name='home'),
]
