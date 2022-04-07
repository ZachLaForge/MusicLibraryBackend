from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET','PUT','DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)

    if request.method == "GET":
        serializer = SongSerializer(song)
        return Response(serializer.data)


    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    elif request.method == 'DELETE':
        serializer =SongSerializer(song)
        song.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)