from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from . import forms


def index(request):
	checklist_result = Dota_2.objects.all()
	return render(request, 'index.html', {'dota': checklist_result})
	

