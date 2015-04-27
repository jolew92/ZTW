from django.shortcuts import render
from list.models import MovieListItem
from django.views.generic import View
from django.http import HttpResponseRedirect


class ListsView(View):
    template_name = 'lists.html'

    def get(self, request):
        if request.user.is_authenticated():
            lists = MovieListItem.objects.filter(movielist__user=request.user)
            return render(request, self.template_name, {'lists': lists, 'user': request.user})
        else:
            return HttpResponseRedirect('/')


class ListItemView(View):
    template_name = 'list.html'

    def get(self, request, movielistitem_id=1):
        if request.user.is_authenticated():
            list = MovieListItem.objects.get(id=movielistitem_id)
            return render(request, self.template_name, {'list': list})
        else:
            return HttpResponseRedirect('/')