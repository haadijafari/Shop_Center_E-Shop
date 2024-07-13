from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('forget-pass/', views.ForgotPasswordView.as_view(), name='forget_pass'),
    path('activation/<str:verification_code>', views.ActivationView.as_view(), name='activation'),
    path('reset-pass/<str:verification_code>', views.ResetPasswordView.as_view(), name='reset_pass'),
]
