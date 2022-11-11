from django.shortcuts import render

from django.http import JsonResponse

from rest_framework import authentication, generics, permissions
from rest_framework.response import Response

from .models import Songs

from .serializers import SongSerializer



class SongsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]

songs_list_create_view = SongsListCreateAPIView.as_view()

class SongsDetailAPIView(generics.RetrieveAPIView):
    queryset = Songs.objects.all()
    serializer_class =  SongSerializer

    permission_classes = [permissions.DjangoModelPermissions]

songs_detail_view = SongsDetailAPIView.as_view()

class SongsUpdateAPIView(generics.UpdateAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'

    permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAuthenticated]

songs_update_view = SongsUpdateAPIView.as_view()

class SongsDestroyAPIView(generics.DestroyAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'

    permission_classes = [permissions.DjangoModelPermissions]

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

songs_destroy_view = SongsDestroyAPIView.as_view()
