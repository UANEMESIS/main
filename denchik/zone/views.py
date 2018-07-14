from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from . import forms


def index(request):
	checklist_result = CheckList.objects.all()
	actions_result = Actionz.objects.all()
	return render(request, 'index.html', {'listall' : checklist_result, 'actions' : actions_result})
	
