from django.contrib import admin

from .models import Album, Genre, Musician, Song


class DiscographyAdmin(admin.ModelAdmin):
    list_display = ["name", "musician", "album", "genre",]
    list_filter = ["musician", "album",]
    search_fields = ["name",]

    class Meta:
        model = Song


admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Musician)
admin.site.register(Song, DiscographyAdmin)