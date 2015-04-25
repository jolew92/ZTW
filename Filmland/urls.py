from django.conf.urls import include, url, patterns
from django.contrib import admin
from movies.views import MoviesView, MovieView
from people.views import PeopleView, PersonView
from views import HomeView, SearchView
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from accounts.views import LoginView, AuthView, LogoutView, LoggedinView, InvalidLoginView, RegisterUserView, RegisterSuccessrView


urlpatterns = patterns('', url(r'^i18n/', include('django.conf.urls.i18n')),
                       url(r'^admin/', include(admin.site.urls),))

urlpatterns += i18n_patterns('',

    url(_(r'^$'), HomeView.as_view()),

    # user auth urls
    url(_(r'^accounts/login/$'), LoginView.as_view()),
    url(_(r'^accounts/auth/$'), AuthView.as_view()),
    url(_(r'^accounts/logout/$'), LogoutView.as_view()),
    url(_(r'^accounts/loggedin/$'), LoggedinView.as_view()),
    url(_(r'^accounts/invalid/$'), InvalidLoginView.as_view()),
    url(_(r'^accounts/register/$'), RegisterUserView.as_view()),
    url(_(r'^accounts/register_success/$'), RegisterSuccessrView.as_view()),

    # movies
    url(_(r'^movies/all/$'), MoviesView.as_view()),
    url(_(r'^movies/get/(?P<movie_id>\d+)/$'), MovieView.as_view()),
    url(_(r'^people/all/$'), PeopleView.as_view()),
    url(_(r'^people/get/(?P<person_id>\d+)/$'), PersonView.as_view()),
    url(_(r'^search/$'), SearchView.as_view()),
)