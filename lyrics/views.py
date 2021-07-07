from django.views import View
from django.http.response import HttpResponse
from lyrics.models import SongInfo, Lyrics, Mood, SongMood
import json
from django.db.models import Q


class Song(View):
    """ Create SongInfo by GET method
        returns:
            HttpResponse
    """
    def get(self, request):
        data = []
        if request.GET.get('songid', False):
            song_id = request.GET['songid']
            all_entries = SongInfo.objects.filter(songId=song_id)
            for all_entry in all_entries:
                lyrics = Lyrics.objects.get(songId=all_entry.songId).content
                mood_list = self.get_mood(all_entry)
                data.append({
                    'songId': all_entry.songId,
                    'singer': all_entry.artist,
                    'imgURL': all_entry.imgURL,
                    'title': all_entry.title,
                    'moods': mood_list,
                    'lyrics': lyrics,
                })
        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return HttpResponse(json_data, content_type="application/json")

    def get_mood(self, entry):
        mood_list = []
        for songmood in SongMood.objects.filter(songId=entry.songId):
            mood_list.extend(Mood.objects.filter(
                            moodId=songmood.moodId.moodId
                            ).values('moodId', 'mood'))
        return mood_list


class Crawler(View):
    """ Get data from Models
        returns:
            HttpResponse
    """
    def post(self, request):
        data = json.loads(request.body)
        # TODO Data predict code 넣기
        for song_info in data:
            song = SongInfo(songId=song_info['songId'],
                            title=song_info['title'],
                            artist=song_info['artists'],
                            imgURL=song_info['imgUrl'],
                            mood1=Mood.objects.get(moodId=song_info['mood1']),
                            mood2=Mood.objects.get(moodId=song_info['mood2']),
                            mood3=Mood.objects.get(moodId=song_info['mood3']),
                            )
            lyric = Lyrics(songId=SongInfo.objects.get(songId=song_info['songId']), 
                           content=song_info['lyrics'])
            song.save()
            lyric.save()
        return HttpResponse("OK")


class MusicList(View):
    """ Create MusicList by GET method

        returns:
            HttpResponse
    """
    def get(self, request):
        data = []
        if request.GET.get('moodid', False):
            song_entries = self.get_songentry(request.GET['moodid'])
            for lyrics, songinfo in song_entries:
                data.append({
                    'songId': songinfo.songId,
                    'singer': songinfo.artist,
                    'title': songinfo.title,
                    'imgURL': songinfo.imgURL,
                    'lyrics': lyrics,
                })

        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        return HttpResponse(json_data, content_type="application/json")

    def get_songentry(self, moodid):
        mood_entries = Mood.objects.filter(moodId=moodid)
        song_entries = []
        for mood in mood_entries:
            song_id_entries = SongMood.objects.filter(moodId=mood)
            for songmood in song_id_entries:
                print(songmood.songId)
                lyrics = Lyrics.objects.get(songId=songmood.songId).content
                songinfo = songmood.songId
                song_entries.append((lyrics, songinfo))
        return song_entries

    def musiclist(self, request):
        return HttpResponse("OK")
