from django.db import models

# Create your models here.
class Artist(models.Model):
    ism = models.CharField(max_length=30)
    rasm = models.URLField()
    def __str__(self):
        return self.ism

class Album(models.Model):
    nom = models.CharField(max_length=30)
    muqova = models.URLField()
    def __str__(self):
        return self.nom

class Song(models.Model):
    nom = models.CharField(max_length=30)
    cover = models.URLField()
    source = models.URLField()
    def __str__(self):
        return self.nom


