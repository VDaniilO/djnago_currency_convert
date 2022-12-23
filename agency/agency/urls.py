from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('converter.urls'))
]

urlpatterns += doc_url
