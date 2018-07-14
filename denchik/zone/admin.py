from django.contrib import admin
from .models import *
from .forms import *

#https://pypi.org/project/django-nested-inline/

class UserTabularInline(admin.TabularInline):
	model = Actionz
	ordering = ('action_id', 'creator', 'action') # не работает
	readonly_fields = ('action_id',)
	#form = MyForm
		
class InlineClass(admin.ModelAdmin):
	inlines = [UserTabularInline]

	#class Meta:
	#	model = CheckList

class TodoListAdmin(admin.ModelAdmin):
    readonly_fields = ('action_id',)
	
#admin.site.register(User)
#admin.site.register(Actionz)
admin.site.register(CheckList, InlineClass)







