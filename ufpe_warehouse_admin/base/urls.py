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
    path("local_stores/", views.local_stores, name="local_stores"),

    path("material/<str:pk>/", views.material_item, name="material_item"),
    path("material/", views.material, name="material"),
    path("local_stores/", views.local_stores, name="local_stores"),
    path("cadastrar-material", views.create_material, name="create_material"),
    path("atualizar-material/<str:pk>/", views.update_material, name="update_material"),
    path("remover-material/<str:pk>/", views.delete_material, name="delete_material"),

    path("fornecedor/<str:pk>/", views.supplier_item, name="supplier_item"),
    path("fornecedor/", views.supplier, name="supplier"),
    path("cadastrar-fornecedor", views.create_supplier, name="create_supplier"),
    path("atualizar-fornecedor/<str:pk>/", views.update_supplier, name="update_supplier"),
    path("remover-fornecedor/<str:pk>/", views.delete_supplier, name="delete_supplier"),

    path("local/<str:pk>/", views.local_item, name="local_item"),
    path("local/", views.local, name="local"),
    path("cadastrar-local", views.create_local, name="create_local"),
    path("atualizar-local/<str:pk>/", views.update_local, name="update_local"),
    path("remover-local/<str:pk>/", views.delete_local, name="delete_local"),

    path("movimentacao/<str:pk>/", views.moviment_item, name="moviment_item"),
    path("movimentacao/", views.moviment, name="moviment"),
    path("cadastrar-movimentacao", views.create_moviment, name="create_moviment"),
    path("atualizar-movimentacao/<str:pk>/", views.update_moviment, name="update_moviment"),
    path("remover-movimentacao/<str:pk>/", views.delete_moviment, name="delete_moviment"),

    path ("dashboard",views.dashboard, name="dashboard"),
    path ("relatório",views.report, name="report"),
    # path("assistencia/<str:pk>/", views.assistent_item, name="assistentitem"),
    # path("assistencia/", views.assistent, name="assistent"),
    # path("cadastrar-assistencia", views.create_assistent, name="create_assistent"),
    # path("remover-assistencia/<str:pk>/", views.delete_assistent, name="delete_assistent"),


]

