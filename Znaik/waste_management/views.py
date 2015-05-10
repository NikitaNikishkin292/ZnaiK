from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import Bin

def index(request):
	first_five_bins = Bin.objects.order_by('bin_id')[:5]
	context = { 'first_five_bins' : first_five_bins }
	#Передаём context по данному адресу, там ждут его содержимое
	return render(request, 'waste_management/index.html', context)


def detail(request, bin_id):
	return HttpResponse("You are looking at bin %s." % bin_id)

def waste_inside(request, bin_id):
	response = "You're looking at current mass inside the bin %s."
	return HttpResponse (response % bin_id)

def unload (request, bin_id):
	return HttpResponse("You are unloading the bin %s." % bin_id)