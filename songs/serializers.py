from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Songs
# from .validators import validate


class SongSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    delete_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='songs-detail',
        lookup_field='pk')

    class Meta:
        model = Songs
        fields = [
            'url',
            'edit_url',
            'delete_url',
            'song',
            'artist',
            'annid',
            'show',
            'opedin',
            'h720',
            'h480',
            'mp3',
        ]

    def validate(self, data):
        qs = Songs.objects.filter(
            song__iexact=data['song'], 
            artist__iexact=data['artist'], 
            annid=data['annid'],
            opedin__iexact=data['opedin'],
        )
        if qs.exists():
            raise serializers.ValidationError(f"already in api")
        return data

    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("songs-edit", kwargs={"pk": obj.pk}, request=request)

    def get_delete_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("songs-delete", kwargs={"pk": obj.pk}, request=request)
