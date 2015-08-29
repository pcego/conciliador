from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
		
	name = models.CharField(max_length=100, blank=False)
	tag = models.CharField(max_length=2, blank=False)	
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Estado'


class City(models.Model):
	
	name = models.CharField(max_length=100, blank=False)
	state = models.ForeignKey(State)
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Cidade'

class Neighborhood(models.Model):
		
	name = models.CharField(max_length=100, blank=False)
	city = models.ForeignKey(City)
	active = models.BooleanField(default=True)	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Bairro'

#Product Package
class Package(models.Model):
	
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10,  decimal_places=2)
	over_price = models.DecimalField(max_digits=10, decimal_places=2)
	amount_conciliations = models.IntegerField()
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Pacotes'

