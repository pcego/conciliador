from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from conciliador.models import  Package, State, City, ProductPurchaser
from conciliador.models import Neighborhood, Company, Employee
from conciliador.models import SalePackage, Purchaser, Flag
from conciliador.models import TypeContact, Department, Contact
from django.contrib.auth.models import User

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employees'

class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Package)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Company)
admin.site.register(SalePackage)
admin.site.register(Purchaser)
admin.site.register(Flag)
admin.site.register(ProductPurchaser)
admin.site.register(TypeContact)
admin.site.register(Department)
admin.site.register(Contact)