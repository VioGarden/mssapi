from django.db import models


class Songs(models.Model):
    song = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    annid = models.IntegerField(blank=True)
    show = models.CharField(max_length=200)
    opedin = models.CharField(max_length=25)
    h720 = models.URLField(max_length=100, blank=True)
    h480 = models.URLField(max_length=100, blank=True)
    mp3 = models.URLField(max_length=100, blank=True)
