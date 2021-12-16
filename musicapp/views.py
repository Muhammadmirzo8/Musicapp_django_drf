from rest_framework import generics
from .models import * 
from .serializers import * 
from django.contrib.postgres.search import TrigramSimilarity 
from rest_framework.filters import SearchFilter, OrderingFilter  


class ArtisListCreateView(generics.ListCreateAPIView): 
    queryset = Artist.objects.all() 
    serializer_class = ArtistSerilizer  
    filter_backends = [OrderingFilter, SearchFilter,] 
    search_fields = ["ism", ]
    ordering_fields = ['ism', ] 


class AlbumListCreateView(generics.ListCreateAPIView): 
    queryset = Album.objects.all() 
    serializer_class = AlbumSerilizer  
    filter_backends = [OrderingFilter, SearchFilter,] 
    search_fields = ["nom", ]
    ordering_fields = ['nom', ]


class SongListCreateView(generics.ListCreateAPIView): 
    queryset =  Song.objects.all() 
    serializer_class = SongSerilizer 


class SongListSeachrView(generics.ListAPIView): 
    queryset = Song.objects.all() 
    serializer_class = SongSerilizer  
    filter_backends = [OrderingFilter]
    ordering_fields = ['nom', ]

    def get_queryset(self):
        queryset = Song.objects.all()
        ism = self.request.query_params.get('search')
        if ism is not None:
            queryset = Song.objects.annotate(
                    similarity=TrigramSimilarity(
                        'nom',ism
                    )).filter(similarity__gt=0.3)
        return queryset