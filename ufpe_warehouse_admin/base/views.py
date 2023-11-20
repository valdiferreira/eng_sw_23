from django.shortcuts import render, redirect
from django.db.models import Q
from djnago.contrib import messages
from djnago.contrib.auth import authenticate, login, logout
#from django.http import HttpResponse


from .models import Material
from .models import LocalStore
from .forms import MaterialForm
from django.contrib.auth.models import User



def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Usuário não encontrado")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuário ou senha não encontrado")
            
        
    context={}
    return render(request, "base/login_register", context)

def home(request):
    return render(request,"base/home.html")

def report (request):
    return render(request)

def local_stores (request):
    local_stores= LocalStore.objects.all()
    context={"local_stores":local_stores}
    return render(request,"base/local_stores.html", context)


def material(request):
    q=request.GET.get("q") if request.GET.get("q") != None else ''
    materials= Material.objects.filter(
        Q(name__contains=q) |
        Q(description__contains=q))
    #materials= Material.objects.all()
    context={"materials":materials}
    return render(request,"base/material.html", context)

def material_item(request, pk):
    material= Material.objects.get(id=pk)
    context={"material":material}
    
    return render(request,"base/material_item.html", context)

def create_material (request):
    form = MaterialForm()
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            # print (request.POST)
            form.save()
            return redirect("material")
        
    context={"form":form}
    return render (request, "base/material_form.html", context)

def update_material(request, pk):
    material= Material.objects.get(id=pk)
    form = MaterialForm(instance=material)
    
    if request.method == "POST":
        form = MaterialForm(request.POST, instance=material)
        if form .is_valid():
            form.save()
            return redirect("material")
    context = {'form': form}
    return render(request, "base/material_form.html", context)

def delete_material(request, pk):
    material= Material.objects.get(id=pk)
    context = {'obj': material}
    if request.method=="POST":
        material.delete()
        return redirect("material")
    return render(request, "base/material_delete.html", context)


