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


class TypeContact(models.Model):

    type_contact = models.CharField(max_length=100)
    masks = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.type_contact

    class Meta:
        verbose_name = 'Departamento'

class Department(models.Model):

    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.type_contact

    class Meta:
        verbose_name = 'Tipo Contato'

class Contact(models.Model):

    type_contact = models.ForeignKey(TypeContact)
    value = models.CharField(max_length=200)
    company = models.ForeignKey(Company)
    department = models.ForeignKey(Department)
    talk_with = models.CharField(max_length=100)
    active = models.BooleanField(default=True)    

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Contato'

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

class Venda(models.Model):
    clienteId =models.IntegerField()
    filialId =models.IntegerField()
    adquirente = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=150)
    bandeira = models.CharField(max_length=150)
    produto = models.CharField(max_length=150)
    numeroDaParcela =models.IntegerField()
    quantidadeDeParcelas =models.IntegerField()
    NSU =models.IntegerField()
    autorizacao =models.IntegerField()
    TID =models.IntegerField()
    valorBruto =models.FloatField()
    valorLiquido =models.FloatField()
    cliente = models.CharField(max_length=150)
    dataVenda = models.DateField()
    origem = models.CharField(max_length=150)
    key = models.CharField(max_length=150)
    dataPrevisaoVencimento = models.DateField()
    notaFiscal = models.CharField(max_length=150)


    def __str__(self):
        return str(self.clienteId)

class ConciliacoesVendas(models.Model):
    quantidadeLancamentosConta = models.IntegerField()
    quantidadeLancamentosContrapartida = models.IntegerField()
    valorConta = models.FloatField()
    valorContraPartida = models.FloatField()
    diferenca = models.FloatField()
    bandeira = models.CharField(max_length=150)
    adquirente = models.CharField(max_length=150)

    def __str__(self):
        return str(self.quantidadeLancamentosConta)

class ConciliacoesVendasFiliais(models.Model):
    quantidadeLancamentosConta = models.IntegerField()
    quantidadeLancamentosContrapartida = models.IntegerField()
    valorConta = models.FloatField()
    valorContraPartida = models.FloatField()
    diferenca = models.FloatField()
    bandeira = models.CharField(max_length=150)
    adquirente = models.CharField(max_length=150)
    nomeFilial = models.CharField(max_length=150)
    filialCodigo = models.CharField(max_length=150)
    filialId = models.IntegerField()

    def __str__(self):
        return str(self.nomeFilial)

class ConciliacoesVendasFiliaisID(models.Model):
    quantidadeLancamentosConta = models.IntegerField()
    quantidadeLancamentosContrapartida = models.IntegerField()
    valorConta = models.FloatField()
    valorContraPartida = models.FloatField()
    diferenca = models.FloatField()
    bandeira = models.CharField(max_length=150)
    adquirente = models.CharField(max_length=150)
    nomeFilial = models.CharField(max_length=150)
    filialCodigo = models.CharField(max_length=150)
    filialId = models.IntegerField()

    def __str__(self):
        return str(self.nomeFilial)

class ConciliacoesRecebimentos(models.Model):
    quantidadeLancamentosConta = models.IntegerField()
    quantidadeLancamentosContrapartida = models.IntegerField()
    valorConta = models.FloatField()
    valorContraPartida = models.FloatField()
    diferenca = models.FloatField()
    bandeira = models.CharField(max_length=150)
    adquirente = models.CharField(max_length=150)

    def __str__(self):
        return str(self.quantidadeLancamentosConta)


class ConciliacoesRecebimentosFiliais(models.Model):
    quantidadeLancamentosConta = models.IntegerField()
    quantidadeLancamentosContrapartida = models.IntegerField()
    valorConta = models.FloatField()
    valorContraPartida = models.FloatField()
    diferenca = models.FloatField()
    bandeira = models.CharField(max_length=150)
    adquirente = models.CharField(max_length=150)
    nomeFilial = models.CharField(max_length=150)
    filialCodigo = models.CharField(max_length=150)
    filialId = models.IntegerField()

    def __str__(self):
        return str(self.nomeFilial)


class ConciliacoesRecebimentosFiliaisID(models.Model):
    quantidadeLancamentosConta = models.IntegerField()
    quantidadeLancamentosContrapartida = models.IntegerField()
    valorConta = models.FloatField()
    valorContraPartida = models.FloatField()
    diferenca = models.FloatField()
    bandeira = models.CharField(max_length=150)
    adquirente = models.CharField(max_length=150)
    nomeFilial = models.CharField(max_length=150)
    filialCodigo = models.CharField(max_length=150)
    filialId = models.IntegerField()

    def __str__(self):
        return str(self.nomeFilial)

class LancamentoRecebimento(models.Model):

    adquirente = models.CharField(max_length=150)
    bandeira = models.CharField(max_length = 150)
    quant_lanc_conta = models.IntegerField()
    quant_lançamentos_contra = models.IntegerField()
    valor_total_conta = models.FloatField()
    valor_contra_partida = models.FloatField()
    dif_conc = models.FloatField()

    def __str__(self):
        return str(self.adquirente)