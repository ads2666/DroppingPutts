from django.contrib import admin
from .models import Player, Tournament, Score, Odd


class TournamentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]
    list_display = ('name', 'pub_date')

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Score)
admin.site.register(Player)
admin.site.register(Odd)
