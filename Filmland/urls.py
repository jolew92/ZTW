from django.conf.urls import include, url, patterns
from django.contrib import admin
from movies.views import MoviesView, MovieView
from people.views import PeopleView, PersonView
from views import HomeView, SearchView
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from list.views import ListsView, ListItemView
from accounts.views import EditView, LoginView, LoggedinView, InvalidLoginView, LogoutView, RegisterSuccess, EditListsView, EditListView

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls),),
    url(r'^accounts/auth/$', 'accounts.views.auth_view'),
    url(r'^accounts/register/$', 'accounts.views.register_user'),
    url(r'^accounts/edit_user/$', 'accounts.views.update_profile'),
    url(r'^movies/get/(?P<movie_id>\d+)/set_rating/$', 'movies.views.set_rating'),
	url(r'^movies/set_role/$', 'movies.views.set_role'),
    url(r'^accounts/edit_list/remove_list/$', 'accounts.views.remove_list'),
    url(r'^accounts/edit_list/(?P<list_id>\d+)/remove_movie/$', 'accounts.views.remove_movie'),
    url(r'^accounts/edit_list/add_list/$', 'accounts.views.add_list'),
    url(r'^accounts/edit_list/(?P<list_id>\d+)/change_list_name/$', 'accounts.views.change_list_name'),
)

urlpatterns += i18n_patterns('',

    url(_(r'^$'), HomeView.as_view()),
    url(_(r'^accounts/login/$'), LoginView.as_view()),
    url(_(r'^accounts/logout/$'), LogoutView.as_view()),
    url(_(r'^accounts/loggedin/$'), LoggedinView.as_view()),
    url(_(r'^accounts/invalid/$'), InvalidLoginView.as_view()),
    url(_(r'^accounts/register_success/$'), RegisterSuccess.as_view()),
    url(_(r'^accounts/edit/$'), EditView.as_view()),
    url(_(r'^accounts/edit_list/$'), EditListsView.as_view()),
    url(_(r'^accounts/edit_list/(?P<movielistitem_id>\d+)/$'), EditListView.as_view()),

    # movies
    url(_(r'^movies/all/$'), MoviesView.as_view()),
    url(_(r'^movies/get/(?P<movie_id>\d+)/$'), MovieView.as_view()),
    url(_(r'^people/all/$'), PeopleView.as_view()),
    url(_(r'^people/get/(?P<person_id>\d+)/$'), PersonView.as_view()),
    url(_(r'^search/$'), SearchView.as_view()),
    url(_(r'^list/all/$'), ListsView.as_view()),
    url(_(r'^list/get/(?P<movielistitem_id>\d+)/$'), ListItemView.as_view()),
)