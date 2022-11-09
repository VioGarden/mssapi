from django.urls import path

from . import views

urlpatterns = [
    path('', views.songs_list_create_view, name='songs-list'),
    path('<int:pk>/', views.songs_detail_view, name='songs-detail'),
    path('<int:pk>/update', views.songs_update_view, name='songs-edit'),
    path('<int:pk>/delete/', views.songs_destroy_view, name='songs-delete')
]
