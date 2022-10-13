from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login_view),
    path('register/', views.register),
    path('reset/', views.reset_password),
    path('logout/', views.logout_user),

]