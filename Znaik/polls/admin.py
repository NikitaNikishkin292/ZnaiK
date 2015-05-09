from django.contrib import admin

from .models import Choise, Question

# Register your models here.


class ChoiseInline(admin.TabularInline):
	model = Choise
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	#Разбиение на подразделы
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	#Добавить к вопросу опцию добавлния ответов
	inlines = [ChoiseInline]
	#отобразить до поля
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

#Добавить в админку модель из БД
admin.site.register(Question, QuestionAdmin)

