from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('zone/', include('zone.urls')),
    path('admin/', admin.site.urls),
]


#urlpatterns = [
#    path('admin/', admin.site.urls),
#]
