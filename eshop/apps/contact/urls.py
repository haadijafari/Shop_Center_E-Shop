from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    # path('', views.contact_page_view, name='contact'),
    path('', views.ContactView.as_view(), name='contact'),
]
