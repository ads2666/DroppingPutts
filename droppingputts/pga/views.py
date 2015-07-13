from django.http import HttpResponse
from .models import Tournament


def index(request):
    recent_tourneys = Tournament.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.name for p in recent_tourneys])
    return HttpResponse(output)


def detail(request, tournament_id):
    return HttpResponse("You're looking at tournament %s" % tournament_id)


def results(request, tournament_id):
    response = "You're looking at the results of tournament %s"
    return HttpResponse(response % tournament_id)
