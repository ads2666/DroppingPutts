from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Tournament, Player, Odd, Pick, Score


class IndexView(generic.ListView):
    template_name = 'pga/index.html'
    context_object_name = 'recent_tourneys'

    def get_queryset(self):
        """Return last 5 tournaments"""
        return Tournament.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Tournament
    template_name = 'pga/detail.html'


class ResultsView(generic.DetailView):
    model = Score
    template_name = 'pga/results.html'
# def vote(request, score_id):
