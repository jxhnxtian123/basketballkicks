from django.contrib import admin
from django.urls import path, include
from timprojsys.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include('timprojsys.urls'))
]
