from django.urls import include, path
from . import views
from .views import create_view, list_view, consulta_create, consulta_delete

app_name = "CRUDweb"
urlpatterns = [
    path('', create_view),
    path('list_view/', list_view, name='list_view'),
    path('cosulta/', consulta_create, name='consulta'),
    path('list_view/delete/<int:id>', consulta_delete, name="consulta-delete"),
]