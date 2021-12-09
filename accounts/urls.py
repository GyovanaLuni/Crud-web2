from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.SingUp.as_view(), name='singup')
]