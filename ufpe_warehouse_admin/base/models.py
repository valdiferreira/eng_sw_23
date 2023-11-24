from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Material (models.Model):
    
    name = models.CharField(unique=True, max_length=100, null=False)
    
    description = models.TextField(unique=False, null=True)
    measureUnit = models.CharField(unique=False, max_length=30, null=False)
      
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["name"]
        
    
    def __str__(self):
        return self.name

class Supplier (models.Model):
    name = models.CharField(unique=True, max_length=100, null=False)
    description = models.TextField(unique=False, null=True)
    cnpj = models.CharField(unique=True, max_length=100, null=False)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Sector (models.Model):
    
    name = models.CharField(unique=True, max_length=100, null=False)
    sigla = models.CharField(unique=False, max_length=20, null=True)
    description = models.TextField(unique=False, null=True)
    user_manager = models.ForeignKey(User, on_delete=models.RESTRICT)
      
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class LocalStore (models.Model):
    
    sector = models.ForeignKey(Sector, on_delete=models.RESTRICT)
    sala = models.CharField(unique=True, max_length=10, null=False)
    section = models.CharField(unique=False, max_length=10, null=True)
    description = models.TextField(unique=False, null=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    materials = models.ManyToManyField(Material, through='MaterialQuantityStore')
    def __str__(self):
        return self.sala
    
class MaterialQuantityStore(models.Model):
    material = models.ForeignKey(Material, on_delete=models.RESTRICT)
    local_store = models.ForeignKey(LocalStore, on_delete=models.RESTRICT)
    quantity_material = models.IntegerField(null=False, blank=False)  
    
    def __str__(self):
        return self.quantity_material

    
class Moviment (models.Model):
    status_choices = [("entrada","entrada"),("saída","saída")]

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    sector = models.ForeignKey(Sector, on_delete=models.RESTRICT)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)
    local_store = models.ForeignKey(LocalStore, on_delete=models.RESTRICT)
    material = models.ForeignKey(Material, on_delete=models.RESTRICT)
    
    status = models.CharField(unique=False, max_length=10, null=False
                              , choices=status_choices)
    
    quantity = models.IntegerField(null=False, blank=False)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.status
    
    
    