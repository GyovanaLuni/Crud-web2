from django.urls import include, path
from django.contrib import admin
from CRUDweb.views import create_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('CRUDweb/', include('CRUDweb.urls'), ),
    path('accounts/', include('accounts.urls'), ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', create_view),
]
