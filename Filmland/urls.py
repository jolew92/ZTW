from django.conf.urls import patterns, include, url
from django.contrib import admin
from movies.views import MoviesView, MovieView
from people.views import PeopleView, PersonView
from search.views import SearchView

urlpatterns = patterns('',

    url(r'^$', 'Filmland.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

    # user auth urls
    url(r'^accounts/login/$', 'accounts.views.login'),
    url(r'^accounts/auth/$', 'accounts.views.auth_view'),
    url(r'^accounts/logout/$', 'accounts.views.logout'),
    url(r'^accounts/loggedin/$', 'accounts.views.loggedin'),
    url(r'^accounts/invalid/$', 'accounts.views.invalid_login'),
    url(r'^accounts/register/$', 'accounts.views.register_user'),
    url(r'^accounts/register_success/$', 'accounts.views.register_success'),

    # movies
    url(r'^movies/all/$', MoviesView.as_view()),
    url(r'^movies/get/(?P<movie_id>\d+)/$', MovieView.as_view()),
    url(r'^people/all/$', PeopleView.as_view()),
    url(r'^people/get/(?P<person_id>\d+)/$', PersonView.as_view()),
    url(r'^search/$', SearchView.as_view()),
)
