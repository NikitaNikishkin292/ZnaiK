from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404


from .models import Bin, Measurement

def index(request):
	first_five_bins = Bin.objects.order_by('bin_id')[:5]
	context = { 'first_five_bins' : first_five_bins }
	#Передаём context по данному адресу, там ждут его содержимое
	return render(request, 'waste_management/index.html', context)


def detail(request, bin_id):
	this_bin = get_object_or_404(Bin, pk = bin_id)
	return render(request, 'waste_management/detail.html', { 'bin': this_bin } )

def waste_inside(request, bin_id):
	response = "You're looking at current mass inside the bin %s."
	return HttpResponse (response % bin_id)

def unload (request, bin_id):
	this_bin = get_object_or_404(Bin, pk = bin_id)
	try:
		new_date = request.POST['date_of_new_measurement']
		new_volume = int(request.POST['volume_of_new_measurement'])
		new_mass = int(request.POST['mass_of_new_measurement'])
	except (KeyError, Measurement.DoesNotExist):
		return render(request, 'waste_management/detail.html', {'bin': this_bin} )
	else:
		this_bin.measurement_set.create(measurement_date = new_date, voulume_of_recycle_inside = new_volume, mass_of_recycle_inside = new_mass)
		#reverse создаёт нормальный url waste_management/this_bin.id/waste_inside
		return render(request, 'waste_management/detail.html', {'bin' : this_bin})


