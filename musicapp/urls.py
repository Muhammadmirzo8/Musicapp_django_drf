from django.urls import path 
from .views import * 




urlpatterns = [
    path('artist/', ArtisListCreateView.as_view()),   
    path('album/', AlbumListCreateView.as_view()),  
    path('songs/', SongListCreateView.as_view()),  
    # path('artist/', ArtisListCreateView.as_view()), 
    
]