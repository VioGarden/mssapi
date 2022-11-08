from rest_framework import serializers
from .models import Songs

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = [
            'song',
            'artist',
            'annid',
            'show',
            'opedin',
            'h720',
            'h480',
            'mp3',
        ]
