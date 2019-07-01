from django.shortcuts import render,get_object_or_404
from .models import Album,song


def index(request):
    all_album = Album.objects.all()
    return render(request,'musica/index.html', { 'all_album': all_album})

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'musica/detail.html', {'album': album} )

def favorite(request,album_id):
    album = get_object_or_404(Album , pk=album_id)
    try: # id do banco de dados, correspondente ao post do formulário do song do detail
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,song.DoesNotExit):
        return render(request,  'musica/detail.html', {
        'album':album,
        'error_message': "Você não selecionou nehuma música válida",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'musica/detail.html',{'album':album})