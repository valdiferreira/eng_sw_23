from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse


from .models import Material
from .models import Supplier
from .models import LocalStore
from .forms import MaterialForm
from .forms import  SupplierForm
from .forms import  LocalForm
from django.contrib.auth.models import User



def login_page(request):
    
    if request.user.is_authenticated:
        return redirect("home")
    
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
    return render(request, "base/login_register.html", context)

@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect ("login")

@login_required(login_url="login")
def home(request):
    return render(request,"base/home.html")

def report (request):
    return render(request)

@login_required(login_url="login")
def local_stores (request):
    local_stores= LocalStore.objects.all()
    context={"local_stores":local_stores}
    return render(request,"base/local_stores.html", context)

@login_required(login_url="login")
def material(request):
    q=request.GET.get("q") if request.GET.get("q") != None else ''
    materials= Material.objects.filter(
        Q(name__contains=q) |
        Q(description__contains=q))
    #materials= Material.objects.all()
    context={"materials":materials}
    return render(request,"base/material.html", context)

@login_required(login_url="login")
def material_item(request, pk):
    material= Material.objects.get(id=pk)
    context={"material":material}
    
    return render(request,"base/material_item.html", context)

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
def delete_material(request, pk):
    material= Material.objects.get(id=pk)
    context = {'obj': material}
    if request.method=="POST":
        material.delete()
        return redirect("material")
    return render(request, "base/material_delete.html", context)

@login_required(login_url="login")
def supplier(request):
    q=request.GET.get("q") if request.GET.get("q") != None else ''
    suppliers= Supplier.objects.filter(
        Q(name__contains=q) |
        Q(description__contains=q))
    #materials= Material.objects.all()
    context={"suppliers":suppliers}
    return render(request,"base/supplier.html", context)

@login_required(login_url="login")
def supplier_item(request, pk):
    supplier= Supplier.objects.get(id=pk)
    context={"supplier":supplier}
    
    return render(request,"base/supplier_item.html", context)

@login_required(login_url="login")
def create_supplier(request):
    form = SupplierForm()
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            # print (request.POST)
            form.save()
            return redirect("supplier")
        
    context={"form":form}
    return render (request, "base/supplier_form.html", context)

@login_required(login_url="login")
def update_supplier(request, pk):
    supplier= Supplier.objects.get(id=pk)
    form = SupplierForm(instance=material)
    
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form .is_valid():
            form.save()
            return redirect("supplier")
    context = {'form': form}
    return render(request, "base/supplier_form.html", context)

@login_required(login_url="login")
def delete_supplier(request, pk):
    supplier= Supplier.objects.get(id=pk)
    context = {'obj': material}
    if request.method=="POST":
        supplier.delete()
        return redirect("supplier")
    return render(request, "base/supplier_delete.html", context)

@login_required(login_url="login")
def local(request):
    q=request.GET.get("q") if request.GET.get("q") != None else ''
    locales= LocalStore.objects.filter(
        Q(name__contains=q) |
        Q(description__contains=q))
    #materials= Material.objects.all()
    context={"locales":locales}
    return render(request,"base/local.html", context)

@login_required(login_url="login")
def local_item(request, pk):
    local= LocalStore.objects.get(id=pk)
    context={"local":local}
    
    return render(request,"base/local_item.html", context)

@login_required(login_url="login")
def create_local(request):
    form = LocalForm()
    if request.method == "POST":
        form = LocalForm(request.POST)
        if form.is_valid():
            # print (request.POST)
            form.save()
            return redirect("local")
        
    context={"form":form}
    return render (request, "base/local_form.html", context)

@login_required(login_url="login")
def update_local(request, pk):
    local= LocalStore.objects.get(id=pk)
    form = LocalForm(instance=material)
    
    if request.method == "POST":
        form = LocalForm(request.POST, instance=local)
        if form .is_valid():
            form.save()
            return redirect("local")
    context = {'form': form}
    return render(request, "base/local_form.html", context)

@login_required(login_url="login")
def delete_local(request, pk):
    local= LocalStore.objects.get(id=pk)
    context = {'obj': material}
    if request.method=="POST":
        local.delete()
        return redirect("local")
    return render(request, "base/slocal_delete.html", context)









def view_404(request, exception):
    return render(request, 'base/404.html', status=404)