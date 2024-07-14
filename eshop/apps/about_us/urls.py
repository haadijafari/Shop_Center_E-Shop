from django.urls import path

from . import views

app_name = 'about_us'

urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
]
