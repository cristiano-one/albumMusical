from django.db import models

# Cada vez que mecher neste arqui tem que fazer o makemigrations no banco de dados
# python mamage.py makemigrations nomedoapp
# e depois o migrate

class Album(models.Model):
    artista = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genero = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ' - ' + self.artista

class song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

