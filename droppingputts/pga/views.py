from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm

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


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('pga/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/tournaments/accounts/loggedin')
    else:
        return HttpResponseRedirect('/tournaments/accounts/invalid')


def loggedin(request):
    return render_to_response('pga/loggedin.html',
                              {'full_name': request.user.username})


def invalid_login(request):
    return render_to_response('pga/invalid_login.html')


def logout(request):
    auth.logout(request)
    return render_to_response('pga/logout.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tournaments/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('pga/register.html', args)


def register_success(request):
    return render_to_response('pga/register_success.html')




