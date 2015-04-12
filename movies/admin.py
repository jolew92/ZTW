from django.contrib import admin
from movies.models import Movie, Language, Country, Role, Description, MovieRole


class MoviePeopleInline(admin.TabularInline):
    model = MovieRole
    filter_horizontal = ("people",)
    extra = 0


class MovieCountryInline(admin.TabularInline):
    model = Movie.country.through
    extra = 0


class DescriptionMovieInline(admin.TabularInline):
    model = Description
    extra = 0


class MovieAdmin(admin.ModelAdmin):
    list_display = 'title', 'year', 'language'
    fields = 'title', 'year', 'language', 'genre'
    filter_horizontal = ("genre",)
    inlines = [MovieCountryInline, DescriptionMovieInline, MoviePeopleInline]
    exclude = ('country', 'roles',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Role)
admin.site.register(Description)

