import datetime

from django.db import models
from django.utils import timezone

# test models for app designed for polls
class Bin(models.Model):
	bin_id = models.IntegerField(default = 1)
	#bin_x_coord = models.DecimalField(max_digits = 10, decimal_places = 8)
	#bin_y_coord = models.DecimalField(max_digits = 10, decimal_places = 8)
	bin_adress = models.CharField(max_length = 200)
	#Объём контейнера в литрах
	bin_volume = models.IntegerField(default = 2000)
	

class Measurement(models.Model):
	its_bin = models.ForeignKey(Bin)
	measurement_date = models.DateTimeField()
	#Заполненность контейнера в л
	voulume_of_recycle_inside = models.IntegerField(default = 0)
	#True, если произведена выграузка, False, если сделан замер, но не произведена выгрузка
	was_unloaded = models.BooleanField
	#Масса содержимого контейнера. Заполняется только если производилась выгрузка
	mass_of_recycle_inside = models.DecimalField(max_digits = 3, decimal_places = 1) 
