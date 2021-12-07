from django.urls import include, path
from . import views
from .views import create_view, list_view, consulta_create

app_name = "CRUDweb"
urlpatterns = [
    path('', create_view),
    path('list_view/', list_view, name='list_view'),
    path('cosulta/', consulta_create, name='consulta')
]