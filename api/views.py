from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from songs.serializers import SongSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """DRF API View"""
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "bad data"}, status=400)