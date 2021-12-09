from django.urls import path
from .views import create_view
from .views import list_view
from .views import consulta_create
from .views import consulta_delete
from .views import editConsulta
from .views import list_view_id

app_name = "CRUDweb"
urlpatterns = [
    path('', create_view),
    path('list_view/', list_view, name='list_view'),
    path('cosulta/', consulta_create, name='consulta'),
    path('list_view/delete/<int:id>', consulta_delete, name="consulta-delete"),
    path('list_view/edit/<int:id>', editConsulta, name="consulta-edit"),
    path('list_view/ver_mais/<int:id>', list_view_id, name="consulta-ver-mais"),
]