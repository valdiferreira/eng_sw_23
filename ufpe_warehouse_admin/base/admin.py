from django.contrib import admin

# Register your models here.

from .models import Material, LocalStore, Sector, Supplier, Moviment, MaterialQuantityStore

admin.site.register(Material)
admin.site.register(LocalStore)
admin.site.register(Sector)
admin.site.register(Supplier)
admin.site.register(Moviment)
admin.site.register(MaterialQuantityStore)