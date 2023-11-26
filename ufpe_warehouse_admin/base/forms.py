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

class SupplierForm (ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        
class LocalForm (ModelForm):
    class Meta:
        model = LocalStore
        fields = ["sector", "sala", "section", "description"]
        
class MovimentForm (ModelForm):
    class Meta:
        model = Moviment
        fields = ["sector","supplier", "local_store", "material", "status", "quantity"]