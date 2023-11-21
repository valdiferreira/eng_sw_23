# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import Material
from .models import Supplier
from .models import LocalStore



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
        fields = '__all__'