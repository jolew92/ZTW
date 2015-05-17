from django.contrib import admin
from photogallery.models import Image, PersonAlbum, MovieAlbum


class MovieAlbumAdmin(admin.ModelAdmin):
    search_fields = ["movie__title"]
    list_display = ["movie", "images"]


class PersonAlbumAdmin(admin.ModelAdmin):
    search_fields = ["person__last_name", "person__first_name"]
    list_display = ["person", "images"]


class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["__unicode__", "title", "size", "people_", "movies_",
        "thumbnail", "created"]
  #  list_filter = ["people", "movies"]
    search_fields = ["movies__movie__title", "people__person__last_name", "people__person__first_name"]
    filter_horizontal = ("people", "movies")

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Image, ImageAdmin)
admin.site.register(PersonAlbum, PersonAlbumAdmin)
admin.site.register(MovieAlbum, MovieAlbumAdmin)