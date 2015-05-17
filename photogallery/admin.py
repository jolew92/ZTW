from django.contrib import admin
from photogallery.models import Image, PersonAlbum, MovieAlbum
from people.models import Person


class MovieAlbumAdmin(admin.ModelAdmin):
    search_fields = ["movie"]
    list_display = ["movie", "images"]


class PersonAlbumAdmin(admin.ModelAdmin):
    list_display = ["person"]
    list_display = ["person", "images"]

class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["__unicode__", "title", "size", "people_", "movies_",
        "thumbnail", "created"]
    list_filter = ["people", "movies"]
    filter_horizontal = ("people", "movies")

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Image, ImageAdmin)
admin.site.register(PersonAlbum, PersonAlbumAdmin)
admin.site.register(MovieAlbum, MovieAlbumAdmin)