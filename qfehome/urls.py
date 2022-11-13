
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/search/', include('search.urls')),
    path('api/songs/', include('songs.urls')),
    path('api/users/', include('users.urls')),
]
