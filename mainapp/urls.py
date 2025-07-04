from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path('ajouter/', views.ajouter_photo, name='ajouter_photo'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]



