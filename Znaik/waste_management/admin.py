from django.contrib import admin

from .models import Measurement, Bin

# Register your models here.


class MeasurementInline(admin.TabularInline):
	model = Measurement
	extra = 1

class BinAdmin(admin.ModelAdmin):
	#Разбиение на подразделы
	fieldsets = [
		(None, {'fields': ['bin_id', 'bin_adress', 'bin_volume']}),
		#('Date information', {'fields': ['pub_date']}),
	]
	#Добавить к вопросу опцию добавлния ответов
	inlines = [MeasurementInline]
	#отобразить доп поля
	list_display = ('bin_id', 'bin_adress')
	search_fields = ['bin_adress']

#Добавить в админку модель из БД
admin.site.register(Bin, BinAdmin)

