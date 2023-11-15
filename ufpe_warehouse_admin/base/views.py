from django.shortcuts import render
#from django.http import HttpResponse



materials = [{"id":1, "name":"caneta bic"}
            ]

# Create your views here.
def home(request):
    return render(request,"base/home.html")

def report (request):
    return render(request,).h


def material(request):
    context={"materials": materials}
    return render(request,"base/material.html", context)

def material_item(request, pk):

    return render(request,"base/material.html")

