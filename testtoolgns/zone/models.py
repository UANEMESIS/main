from django.db import models
from django.forms import MultiValueField
import jsonfield

#class MyModel(models.Model):
	#the_json = jsonfield.JSONField()

# class MegaAuthor(models.Model):
	# mega_auth_id = models.AutoField(primary_key=True)
	# mega_author_name = models.CharField(max_length=40)
	
	# #def __str__(self):
		# #return self.mega_author_name
	
# class MegaChecklist(models.Model):
	# mega_list_id = models.AutoField(primary_key=True)
	# mega_checklist_name = models.CharField(max_length=40)
	
	# #def __str__(self):
		# #return self.mega_checklist_name
		
# class MegaSteps(models.Model):
	# actions_id = models.AutoField(primary_key=True)
	# actions = models.CharField(max_length=200)
	# bound_author = models.ForeignKey(MegaAuthor, blank=True, on_delete=models.CASCADE)
	# bound_checklist = models.ForeignKey(MegaChecklist, blank=True, on_delete=models.CASCADE)
	# mega_result = models.NullBooleanField()
	# mega_comment = models.CharField(max_length=300, blank=True)
	
	#def __str__(self):
		#return self.actions

class ListDetail(models.Model):
	author_id_2 = models.AutoField(primary_key=True)
	author_name_2 = models.CharField(max_length=40)
	check_list_name_2 = models.CharField(max_length=40)
	
	def __str__(self):
		return self.author_name_2
		
	#class Admin:
	#	list_display = ('author_id_2',)
	#	search_fields = ('author_id_2',)

class Actionz_2(models.Model):
	doings_id_2 = models.AutoField(primary_key=True)
	doings_2 = models.CharField(max_length=200)
	torrent_2 = models.ForeignKey(ListDetail, blank=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.doings_2
		
	#class Admin:
	#	list_display = ('doings_id_2',)
	#	search_fields = ('doings_id_2',)

class CoreList_2(models.Model):
	creator_2 = models.ForeignKey(ListDetail, blank=True, on_delete=models.CASCADE)
	#name_of_list_2 = models.CharField(max_length=40)
	num_of_action_2 = models.AutoField(primary_key=True)
	action_2 = models.CharField(max_length=300)
	result_2 = models.NullBooleanField()
	comment_2 = models.CharField(max_length=300, blank=True)
	
	def __str__(self):
		return self.name_of_list_2












		
class Author(models.Model):
	author_id = models.AutoField(primary_key=True)
	author_name = models.CharField(max_length=40)
	
	def __str__(self):
		return self.author_name

class Actionz(models.Model):
	doings = models.CharField(max_length=200)
	torrent = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.doings

class CoreList(models.Model):
	creator = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE)
	name_of_list = models.CharField(max_length=40)
	num_of_action = models.AutoField(primary_key=True)
	action = models.CharField(max_length=300)
	result = models.NullBooleanField()
	comment = models.CharField(max_length=300, blank=True)
	
	def __str__(self):
		return self.name_of_list
	
class RandomModel(models.Model):
	user_details = jsonfield.JSONField(unique=True)
	user = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE)
	zozo = models.CharField(max_length=40)


