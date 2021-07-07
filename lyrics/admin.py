from django.contrib import admin
from .models import SongInfo, Mood, Lyrics, SongMood

# Register your models here.


class SongInfoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    list_display = ['songId', 'title', 'artist', 'imgURL', ]


class MoodAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    list_display = ['moodId', 'mood', ]


class LyricsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    list_display = ['songId', 'content', ]


class SongMoodAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    list_display = ['songId', 'moodId', ]


admin.site.register(SongMood, SongMoodAdmin)
admin.site.register(Lyrics, LyricsAdmin)
admin.site.register(SongInfo, SongInfoAdmin)
admin.site.register(Mood, MoodAdmin)