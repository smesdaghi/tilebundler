from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from tilebundler.models import Tileset


class IndexView(generic.ListView):
    template_name = 'tilesets/index.html'

    def get_queryset(self):
        return Tileset.objects.order_by('-created_at')[:5]


class DetailView(generic.DetailView):
    model = Tileset
    template_name = 'tilesets/detail.html'


class ResultsView(generic.DetailView):
    model = Tileset
    template_name = 'tilesets/results.html'


def generate(request, tileset_id):
    tileset = get_object_or_404(Tileset, pk=tileset_id)
    try:
        #selected_name = request.POST['name']
        #tileset.save()
        print 'generate(), tileset: ', tileset
    except Exception:
        return render(request, 'tilesets/detail.html', {
            'tileset': tileset,
            'error_message': 'Name must be unique',
        })
    else:

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('tilesets:results', args=(tileset_id,)))
