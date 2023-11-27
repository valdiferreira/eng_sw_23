from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#from django.http import HttpResponse


from .models import Material
from .models import Supplier
from .models import LocalStore
from .models import Moviment
from .models import MaterialQuantityStore

from .forms import MaterialForm
from .forms import  SupplierForm
from .forms import  LocalForm
from .forms import MovimentForm
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
    #suppliers= Supplier.objects.all()
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
            print (request.POST)
            form.save()
            return redirect("supplier")
        
    context={"form":form}
    return render (request, "base/supplier_form.html", context)

@login_required(login_url="login")
def update_supplier(request, pk):
    supplier= Supplier.objects.get(id=pk)
    form = SupplierForm(instance=supplier)
    
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
    context = {'obj':supplier}
    if request.method=="POST":
        supplier.delete()
        return redirect("supplier")
    return render(request, "base/supplier_delete.html", context)


# def material(request):
#     q=request.GET.get("q") if request.GET.get("q") != None else ''
#     materials= Material.objects.filter(
#         Q(name__contains=q) |
#         Q(description__contains=q))
#     #materials= Material.objects.all()
#     context={"materials":materials}
#     return render(request,"base/material.html", context)



@login_required(login_url="login")
def local(request):
    q=request.GET.get("q") if request.GET.get("q") != None else ''
    locales=LocalStore.objects.filter(
        Q(sala__contains=q))
    #locales= LocalStore.objects.all()
    context={"locales":locales}
    return render(request,"base/local.html", context)

@login_required(login_url="login")
def home(request):
    
    materialquantitystores = MaterialQuantityStore.objects.filter(quantity_material__lte=30)
    context={"materialquantitystores":materialquantitystores}
    return render(request,"base/home.html", context)



@login_required(login_url="login")
def local_item(request, pk):
    local= LocalStore.objects.get(id=pk)
    materialquantitystores = MaterialQuantityStore.objects.filter(local_store=local)

    context={"local":local, "materialquantitystores":materialquantitystores}
    
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
        if form.is_valid():
            form.save()
            return redirect("local")
    context = {'form': form}
    return render(request, "base/local_form.html", context)

@login_required(login_url="login")
def delete_local(request, pk):
    local= LocalStore.objects.get(id=pk)
    context = {'obj': local}
    if request.method=="POST":
        local.delete()
        return redirect("local")
    return render(request, "base/local_delete.html", context)


@login_required(login_url="login")
def moviment(request):
    q=request.GET.get("q") if request.GET.get("q") != None else ''
    moviments=Moviment.objects.filter(
        Q(status__contains=q) | 
        Q(material__name__contains=q) |
        Q(material__description__contains=q) |
        Q(local_store__sala__contains=q) |
        Q(created__date__contains=q)
         )
    #moviments= Moviment.objects.all()
    context={"moviments":moviments}
    return render(request,"base/moviment.html", context)

@login_required(login_url="login")
def moviment_item(request, pk):
    moviments= Moviment.objects.get(id=pk)
    context={"moviments":moviments}
    
    return render(request,"base/moviment_item.html", context)

@login_required(login_url="login")
def create_moviment(request):
    form = MovimentForm()
    if request.method == "POST":
        form = MovimentForm(request.POST)
        if form.is_valid():
            materialquantitystore = MaterialQuantityStore.objects.filter(material=form.instance.material
                                              ,local_store=form.instance.local_store )
           
           #ok
            if  form['status'].value() == "saída" and not materialquantitystore:
                print ("error")
                return redirect("moviment")
            #ok
            if  form['status'].value() == "saída" and materialquantitystore:
                materialquantitystore = MaterialQuantityStore.objects.get(material=form.instance.material
                                                  ,local_store=form.instance.local_store )
                #ok
                if materialquantitystore.quantity_material < int(form['quantity'].value()):
                    print ("error")
                
                #ok
                else:
                    materialquantitystore.quantity_material=materialquantitystore.quantity_material-int(form['quantity'].value())
                    materialquantitystore.save()
                    obj = form.save(commit=False)
                    obj.user = request.user
                     #print (form)
                    obj.save()
            
            if  form['status'].value() == "entrada" and materialquantitystore:
                materialquantitystore = MaterialQuantityStore.objects.get(material=form.instance.material
                                                  ,local_store=form.instance.local_store)
                materialquantitystore.quantity_material=materialquantitystore.quantity_material+int(form['quantity'].value())
                materialquantitystore.save()
                obj = form.save(commit=False)
                obj.user = request.user
                #print (form)
                obj.save()
                    
            if  form['status'].value() == "entrada" and not materialquantitystore:
                MaterialQuantityStore.objects.create(material=form.instance.material
                                                  ,local_store=form.instance.local_store,quantity_material=form['quantity'].value())
                #print (form['material'].value())
                #print (form.instance.material)
                obj = form.save(commit=False)
                obj.user = request.user
                #print (form)
                obj.save()
                
        
    context={"form":form}
    return render (request, "base/moviment_form.html", context)

@login_required(login_url="login")
def update_moviment(request, pk):
    moviment= Moviment.objects.get(id=pk)
    form = MovimentForm(instance=moviment)
    
    if request.method == "POST":
        form = MovimentForm(request.POST, instance=moviment)
        if form.is_valid():
            form.save()
            return redirect("moviment")
    context = {'form': form}
    return render(request, "base/moviment_form.html", context)

@login_required(login_url="login")
def delete_moviment(request, pk):
    moviment= Moviment.objects.get(id=pk)
    context = {'obj': material}
    if request.method=="POST":
        moviment.delete()
        return redirect("moviment")
    return render(request, "base/moviment_delete.html", context)


import plotly.express as px
from .forms import DateForm
from django_pandas.io import read_frame



@login_required(login_url="login")

def dashboard(request):
    
   
    start = request.GET.get("start")
    end = request.GET.get("end")
    status_form = request.GET.get("status")
    local_form = request.GET.get("local")
    moviments=Moviment.objects.all()
    if start and start <= end:
        moviments=moviments.filter(created__date__gte=start)
    if end and end >= start:
        moviments=moviments.filter(created__date__lte=end)
    if status_form:
        moviments=moviments.filter(status=status_form)
    if local_form:
        moviments=moviments.filter(local_store__sala=local_form)
       
    df = read_frame(moviments)
    
    fig = px.line (
        df,
        x="created",
        y="quantity",
        title="Entrada de Material",
        labels={"created": "Tempo", "quantity":"Quantidade"}
        
    )
    
    chart = fig.to_html()
    

    
    fig = px.pie(
        df,
        values="quantity",
        names="material",
        title="Distribuição de Material",
        labels={"material": "Material", "quantity":"Quantidade"}
        )
    
    chart_pie = fig.to_html()
    
    fig = px.bar(df, x='material', y='quantity', barmode="group", 
             hover_data=['sector'], color='status',
             
             title="Distribuição de Material por Status (Entrada/Saída)",
             labels={"material": "Material", "quantity":"Quantidade"}
             )
    
    chart_bar = fig.to_html()
    
    context = {"chart":chart, "form": DateForm(), "chart_bar":chart_bar, "chart_pie":chart_pie}
    
    return render (request, "base/dashboard.html", context)


@login_required(login_url="login")

def report(request):
    
    
    start = request.GET.get("start")
    end = request.GET.get("end")
    status_form = request.GET.get("status")
    local_form = request.GET.get("local")
    moviments=Moviment.objects.all()
    
    if start and start <= end:
        moviments=moviments.filter(created__date__gte=start)
    if end and end >= start:
        moviments=moviments.filter(created__date__lte=end)
    if status_form:
        moviments=moviments.filter(status=status_form)
    if local_form:
        moviments=moviments.filter(local_store__sala=local_form)
    
    df = read_frame(moviments)
    if not df.empty:
        df=df[['status', 'material', 'local_store', 'sector','created']]
        
        
        df['created'] = df['created'].dt.date
        df.columns = ['status', 'material', 'local', 'setor','data']
        
        df = df.to_html(classes='w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white', index=False)
    
    
        context = {"form": DateForm(), "table_report":df}
        return render (request, "base/report.html", context)
    
    moviments=Moviment.objects.all()
    df = read_frame(moviments)
    df=df[['status', 'material', 'local_store', 'sector','created']]
        
        
    df['created'] = df['created'].dt.date
    df.columns = ['status', 'material', 'local', 'setor','data']
        
    df = df.to_html(classes='w3-table w3-striped w3-bordered w3-border w3-hoverable w3-white', index=False)
    
    
    context = {"form": DateForm(), "table_report":df}
    return render (request, "base/report.html", context)
    
    
    
    
    


def view_404(request, exception):
    return render(request, 'base/404.html', status=404)