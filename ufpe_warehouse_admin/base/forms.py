# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import Material
from .models import Supplier
from .models import LocalStore
from .models import Moviment




from django import forms

class DateForm(forms.Form):
    start = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))




class MaterialForm (ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        labels = {
            "name": ("Nome"),
            "description": ("Descrição"),
            "measureUnit": ("Unidade de Medida"),
        }


from localflavor.br.forms import BRCNPJField

class SupplierForm (ModelForm):
    cnpj = BRCNPJField(label=u'CNPJ')
    class Meta:
        model = Supplier
        fields = '__all__'
        labels = {
            "name": ("Nome"),
            "description": ("Descrição"),
           
        }
        
class LocalForm (ModelForm):
    class Meta:
        model = LocalStore
        fields = ["sector", "sala", "section", "description"]
        labels = {
            "sector": ("Setor"),
            "description": ("Descrição"),
            "sala": ("Sala"),
            "section":("Seção")
           
        }
        
   
class MovimentForm (ModelForm):
    class Meta:
        model = Moviment
        fields = ["sector","supplier", "local_store", "material", "status", "quantity"]
        labels = {
            "sector": ("Setor"),
            "local_store": ("Local"),
            "supplier": ("Fornecedor"),
            "material": ("Material"),
            "status": ("Status"),
            "quantity": ("Quantidade"),
        }
       
        
        
        
        
        
        
        
        
        
        
        