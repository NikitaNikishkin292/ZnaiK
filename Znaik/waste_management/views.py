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
	last_measurement = this_bin.measurement_set.get(pk = 1)
	try:
		delta = int(request.POST['recycle_inside'])
	except (KeyError, Measurement.DoesNotExist):
		return render(request, 'waste_management/detail.html', {'bin': this_bin} )
	else:
		last_measurement.voulume_of_recycle_inside += delta
		last_measurement.save()
		#reverse создаёт нормальный url waste_management/this_bin.id/waste_inside
		return HttpResponseRedirect(reverse('waste_management:waste_inside', args=(this_bin.id,)))


