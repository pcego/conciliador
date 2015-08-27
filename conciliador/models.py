from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
	
	name = models.CharField(max_length=100, blank=False)
	state = models.ForeignKey(State)
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Cidade'

class neighborhood(models.Model):
		
	name = models.CharField(max_length=100, blank=False)
	city_id = models.ForeignKey(City)
	active = models.BooleanField(default=True)	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Bairro'

class State(models.Model):
		
	name = models.CharField(max_length=100, blank=False)
	tag = models.CharField(max_length=2, blank=False)	
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Estado'