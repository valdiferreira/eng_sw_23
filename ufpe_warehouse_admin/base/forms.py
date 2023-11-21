# -*- coding: utf-8 -*-

from django.forms import ModelForm
from .models import Material
from .models import Supplier


class MaterialForm (ModelForm):
    class Meta:
        model = Material
        fields = '__all__'

class SupplierForm (ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'