from django.shortcuts import render, redirect
#from django.http import HttpResponse


from .models import Material
from .models import LocalStore
from .forms import MaterialForm

def home(request):
    return render(request,"base/home.html")

def report (request):
    return render(request)

def local_stores (request):
    local_stores= LocalStore.objects.all()
    context={"local_stores":local_stores}
    return render(request,"base/local_stores.html", context)


def material(request):
    materials= Material.objects.all()
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
    context = {'form': form}
    return render(request, "base/material_form.html", context)
