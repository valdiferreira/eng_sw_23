import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import LocalStore,Material,MaterialQuantityStore,Moviment,Supplier,Sector

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    username = first_name
    password = make_password("password")
    is_staff = True

import random
class MaterialFactory (DjangoModelFactory):
    l=["Caneta Bic","Caneta Compaq","Mouse Multilaser"]
    name = random.choice(l)
    
    description = factory.Faker(
        "sentence",
        nb_words=3,
        variable_nb_words=True
    )
    measureUnit = "unidade"
    
class LocalFactory (DjangoModelFactory):
    l=["14,22"]
    name = random.choice(l)
    
    description = factory.Faker(
        "sentence",
        nb_words=3,
        variable_nb_words=True
    )
    measureUnit = "unidade"
   


