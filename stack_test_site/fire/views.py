# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from .models import Firefighter
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='/login/')
def status(request):

  firefighters = Firefighter.objects.all()

  context = {
    'firefighters': firefighters,
    'availableCount': firefighters.filter(status='AV').count() + firefighters.filter(status='OD').count(),
    'leaveCount': firefighters.filter(status='LV').count(),
    'unAvCount': firefighters.filter(status='UN').count()
  }

  return render(request, 'status.html', context)

@login_required(login_url='/login/')
def details(request, id):
  class ChangeStatus(ModelForm):
    class Meta:
      model = Firefighter
      fields = ['status']

  form = ChangeStatus()
  firefighter = Firefighter.objects.get(id=id)

  if request.method == 'POST':
    form = ChangeStatus(request.POST, instance=firefighter)
    if form.is_valid():
      form.save() 
      return HttpResponseRedirect('/status/')
  else:
    form = ChangeStatus()

  context = {
    'firefighter': firefighter,
    'form': form
  }

  return render(request, 'details.html', context)

def members(request):

  firefighters = Firefighter.objects.all().order_by('rank')

  context = {
    'firefighters': firefighters,
  }
  return render(request, 'members.html', context)
