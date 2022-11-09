from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Songs

# def validate(data):
#     qs = Songs.objects.filter(
#         song__iexact=data['song'], 
#         artist__iexact=data['artist'], 
#         annid=data['annid'],
#         opedin__iexact=data['opedin'],
#     )
#     if qs.exists():
#         raise serializers.ValidationError(f"already in api")
#     return data