#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:18:57 2023

@author: dinho
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("relatorio/", views.report, name="relatório"),
    path("material/<str:pk>/", views.material_item, name="material_item"),
    path("material/", views.material, name="material")

]