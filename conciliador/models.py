# coding:utf-8
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
	
	name = models.CharField(max_length=100, blank=False)
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10,  decimal_places=2)
	over_price = models.DecimalField(max_digits=10, decimal_places=2)
	amount_conciliations = models.IntegerField()
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Pacote'



class Company(models.Model):

	company_name = models.CharField(max_length=100, blank=False)
	cnpj = models.CharField(max_length=30)
	state_registration = models.CharField(max_length=50)
	cpf = models.CharField(max_length=20)
	fantasy_name = models.CharField(max_length=100)
	boss = models.ForeignKey(User, blank=False)
	street = models.CharField(max_length=100)
	number = models.CharField(max_length=10)
	complement = models.CharField(max_length=100)
	neighborhood = models.ForeignKey(Neighborhood)
	concil_id_branch = models.CharField(max_length=100)
	concil_id_customer = models.CharField(max_length=100)
	parent_company = models.ForeignKey( 'self', null=True, blank=True, help_text='Empresa Matriz', related_name='branch_parent_company' )
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.company_name

	class Meta:
		verbose_name='Empresa'
 
class SalePackage(models.Model):
	company = models.ForeignKey(Company, blank=False)
	package = models.ForeignKey(Package, blank=False)
	sale_date = models.DateField(help_text='Ex: 29/07/2015')
	active = models.BooleanField(default=True)

	def __str__(self):
		return 'Venda'

	class Meta:
		verbose_name='VendadePacote'

class Purchaser(models.Model):

	company = models.ForeignKey(Company)
	contract = models.CharField(max_length = 100, blank=False)
	name = models.CharField(max_length = 100, blank=False)
	device_rent_value = models.DecimalField(max_digits=10, decimal_places=2)
	antecipation_tax = models.DecimalField(max_digits=10, decimal_places=2)
	validate = models.DateField(help_text='Formato: dd/MM/aaaa')
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Adquirente'

class Flag(models.Model):

	name = models.CharField(max_length=100, blank=False)
	product_type = models.CharField(max_length=100, blank=False)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Bandeira'

class ProductPurchaser(models.Model):

	purchaser = models.ForeignKey(Purchaser)
	flag = models.ForeignKey(Flag)
	name = models.CharField(max_length=100, blank=False)
	service_tax = models.DecimalField(max_digits=10, decimal_places=2)
	receipt_forecast = models.IntegerField()
	bank = models.CharField(max_length=100, blank=False)
	agency = models.CharField(max_length=10, blank=False)
	account = models.CharField(max_length=100, blank=False)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Produto Adquirente'

class Employee(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=100)
    neighborhood = models.ForeignKey(Neighborhood)
    birth_date = models.DateField()
    company = models.ManyToManyField(Company)
    active = models.BooleanField()