from django.contrib import admin
from list.models import MovieListItem, MovieList


class MovieListItemInline(admin.TabularInline):
    model = MovieListItem
    filter_horizontal = ("movies",)
    extra = 0


class MovieListAdmin(admin.ModelAdmin):
    list_display = 'user',
    fields = 'user',
    inlines = [MovieListItemInline]
    exclude = ('movies',)


class MovieListItemAdmin(admin.ModelAdmin):
    list_display = 'name', 'movielist'
    fields = 'name', 'movielist', 'movies',
    filter_horizontal = ("movies",)


admin.site.register(MovieList, MovieListAdmin)
admin.site.register(MovieListItem, MovieListItemAdmin)