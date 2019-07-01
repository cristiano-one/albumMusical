from django.contrib import admin
from .models import Album,song

# É preciso registrar as variáveis que foram criadas no arquivo models.py

admin.site.register(Album)
admin.site.register(song)