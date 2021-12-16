from django.test import TestCase 
from musicapp.models import *  
from musicapp.serializers import * 
 
class TestAlbumSerializer(TestCase): 
    def setUp(self):
        self.album = Album.objects.create(nom="wewe", muqova="https://student.fbtuit.uz/education/tasks?subject=18")  
    def test_data(self): 
        data = AlbumSerilizer(self.album).data 
        self.assertIsNotNone(data) 
        assert data['id'] is not None 
        assert data['nom'] == "wewe"   
        assert data['muqova'] == "https://student.fbtuit.uz/education/tasks?subject=18"  
      
           

class TestArtistSerializer(TestCase): 
    def setUp(self):
        self.artist = Artist.objects.create(ism="Jony", rasm="https://student.fbtuit.uz/education/tasks?subject=18")  
    def test_data(self): 
        data = ArtistSerilizer(self.artist).data 
        self.assertIsNotNone(data) 
        assert data['id'] is not None 
        assert data['ism'] == "Jony"  
        self.assertEqual(data['rasm'], "https://student.fbtuit.uz/education/tasks?subject=18")  
          

class TestSongSerializer(TestCase): 
    def setUp(self):
        self.song = Song.objects.create(nom="Leonardo DiCaprio", cover="https://student.fbtuit.uz/education/tasks?subject=18", source="https://student.fbtuit.uz/education/tasks?subject=18")  
    def test_data(self): 
        data = SongSerilizer(self.song).data 
        self.assertIsNotNone(data) 
        assert data['id'] is not None 
        assert data['nom'] == "Leonardo DiCaprio"  
        self.assertEqual(data['cover'], "https://student.fbtuit.uz/education/tasks?subject=18")  
        assert data['source'] == "https://student.fbtuit.uz/education/tasks?subject=18"   
