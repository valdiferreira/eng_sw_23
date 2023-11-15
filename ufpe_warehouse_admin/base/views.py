from django.shortcuts import render
#from django.http import HttpResponse


from .models import Material

# materials = [{"id":1, "name":"caneta bic"},
#              {"id":2, "name":"folha A4"},
#              {"id":3, "name":"Toner HP"}
#             ]

# Create your views here.
def home(request):
    return render(request,"base/home.html")

def report (request):
    return render(request,).h


def material(request):
    materials= Material.objects.all()
    context={"materials":materials}
    return render(request,"base/material.html", context)

def material_item(request, pk):
    material= Material.objects.get(id=pk)
    context={"material":material}
    
    return render(request,"base/material_item.html", context)

