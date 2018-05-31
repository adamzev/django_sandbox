from django.contrib import admin

# Register your models here
from .models import Team, Firefighter

admin.site.register(Team)
admin.site.register(Firefighter)
