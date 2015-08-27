from django.db import models

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