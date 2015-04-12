from django.contrib import admin
from movies.models import Movie, Language, Genre, Country, Role, Person, Biography, Description, MovieRole, MovieItem,MovieList


class MoviePeopleInline(admin.TabularInline):
    model = MovieRole
    filter_horizontal = ("people",)
    extra = 0


class MovieCountryInline(admin.TabularInline):
    model = Movie.country.through
    extra = 0


class PersonBioInline(admin.TabularInline):
    model = Biography
    extra = 0


class PersonAdmin(admin.ModelAdmin):
    inlines = [PersonBioInline]
    exclude = ('biography',)


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
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Role)
admin.site.register(Person, PersonAdmin)
admin.site.register(Biography)
admin.site.register(Description)
admin.site.register(MovieItem)
admin.site.register(MovieList)

