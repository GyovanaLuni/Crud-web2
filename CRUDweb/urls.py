from django.urls import include, path
from . import views
from .views import create_view, helloworld, list_view

urlpatterns = [
    path('', create_view),
    path('list_view/', list_view),
    path('helloworld/', helloworld),
]