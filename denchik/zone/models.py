from django.db import models
from django.forms import MultiValueField
import jsonfield
from multiselectfield import MultiSelectField # pip install django-multiselectfield


#MY_CHOICES = (('item_key1', 'No Result'),
#          ('item_key2', 'Pass'),
#          ('item_key3', 'Failed'),)

#MultiSelectField(choices=MY_CHOICES) #models.NullBooleanField()

class CheckList(models.Model):
	checklist_id = models.AutoField(primary_key=True)
	checklist_name = models.CharField(max_length=30, blank=True)
	
	def __str__(self):
		return self.checklist_name
	
class Actionz(models.Model):
	action_id = models.AutoField(primary_key=True, default = 1) 
	cl = models.ForeignKey(CheckList, on_delete=models.CASCADE)
	creator = models.CharField(max_length=30, default='Admin')
	#default = models.CharField(max_length=200)
	action = models.CharField(max_length=200, default='Empty field')
	result = models.CharField(max_length=256, choices=[('None', 'None'), ('Pass', 'Pass'), ('Fail', 'Fail')])
	comment = models.CharField(max_length=300, blank=True)
	

	def __str__(self):
		return self.action

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=30)
	checkl = models.ForeignKey(CheckList, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.user_name

