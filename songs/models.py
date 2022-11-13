from django.db import models
from django.db.models import Q


class SongsQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(song__icontains=query) | Q(artist__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs = qs.filter(user=user)
        return qs


class SongsManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return SongsQuerySet(self.model, using=self.db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Songs(models.Model):
    song = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    annid = models.IntegerField(blank=True)
    show = models.CharField(max_length=200)
    opedin = models.CharField(max_length=25)
    h720 = models.URLField(max_length=100, blank=True)
    h480 = models.URLField(max_length=100, blank=True)
    mp3 = models.URLField(max_length=100, blank=True)
    public = models.BooleanField(default=True)

    objects = SongsManager()
