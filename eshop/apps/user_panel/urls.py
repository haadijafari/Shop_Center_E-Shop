from django.urls import path
from . import views

app_name = 'user_panel'

urlpatterns = [
    path('', views.UserPanel.as_view(), name='dashboard'),
    path('edit-prof', views.EditProfileInfo.as_view(), name='edit_profile'),
    path('change-pass/', views.ChangePass.as_view(), name='change_password'),
]
