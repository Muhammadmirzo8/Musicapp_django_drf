
from rest_framework import serializers

from .models import * 
 
class ArtistSerilizer(serializers.ModelSerializer):  
 class Meta:
    model = Artist 
    fields = "__all__" 

class SongSerilizer(serializers.ModelSerializer):  
 class Meta:
    model = Song
    fields = "__all__"  

class AlbumSerilizer(serializers.ModelSerializer):  
     class Meta:
      model = Album
      fields = "__all__"