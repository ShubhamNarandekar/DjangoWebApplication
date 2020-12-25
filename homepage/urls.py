from homepage import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
]
