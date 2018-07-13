from django.contrib import admin
#from .models import Author
#from .models import Dota_2
#from .models import Corelist

from .models import *

#class StudentEnrollmentInline(admin.TabularInline):
#    model = Enrollment
#    readonly_fields=('id',)


class Fullstructure(admin.TabularInline):
	model = ListDetail
	model = CoreList_2
	
	#readonly_fields = ('CoreList_2',)
	#readonly_fields=('author_id_2',)

class ZzzClass_2(admin.ModelAdmin):
	inlines = [Fullstructure]
	
	#class Meta:
		#model = CoreList_2
		
	def __str__(self):
		return self.num_of_action_2

	
	
admin.site.register(ListDetail, ZzzClass_2)		
		
class Authzzz(admin.TabularInline):
	model = Actionz

class ZzzClass(admin.ModelAdmin):
	inlines = [Authzzz]
	class Meta:
		model = CoreList
		
	def __str__(self):
		return self.num_of_action
		
#class ApplyAuthor(admin.TabularInline):
#	model = MegaSteps
	
#class ApplyAdminList(admin.TabularInline):
#	inlines = [ApplyAuthor]
#	class Meta:
#		model = MegaChecklist
		
admin.site.register(Author, ZzzClass)
admin.site.register(CoreList)
admin.site.register(RandomModel)	


#admin.site.register(MegaAuthor, ApplyAdminList)
	
#StackedInline):

	




