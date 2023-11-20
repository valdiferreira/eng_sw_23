#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:18:57 2023

@author: dinho
"""

from django.urls import path
from . import views


urlpatterns = [
    path ("login/", views.login_page,name="login"),
    path ("logout/", views.logout_user,name="logout"),
    path("", views.home, name="home"),
    path("relatorio/", views.report, name="relatório"),
    path("material/<str:pk>/", views.material_item, name="material_item"),
    path("material/", views.material, name="material"),
    path("local_stores/", views.local_stores, name="local_stores"),
    path("cadastrar-material", views.create_material, name="create_material"),
    path("atualizar-material/<str:pk>/", views.update_material, name="update_material"),
    path("remover-material/<str:pk>/", views.delete_material, name="delete_material"),
]