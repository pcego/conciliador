from django.contrib import admin
from conciliador.models import  Package, State, City, Neighborhood

admin.site.register(Package)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)