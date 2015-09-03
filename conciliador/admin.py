from django.contrib import admin
from conciliador.models import Package, State, City, Neighborhood, Company, SalePackage, Purchaser, Flag, ProductPurchaser

admin.site.register(Package)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Company)
admin.site.register(SalePackage)
admin.site.register(Purchaser)
admin.site.register(Flag)
admin.site.register(ProductPurchaser)

