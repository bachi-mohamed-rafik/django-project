# django-project
This project is made based on this tutorial
https://www.youtube.com/channel/UCqEQv6icm6fl2CLe0PLFtTw 

mkdir Project / cd Project
python -m venv env
set-executionpolicy unrestricted
cd env/Scripts.\activate
django-admin startproject Project	
pyhton manage.py runserver
python manage.py createsuperuser
python manage.py startapp notaire
add app notaire into installed apps

from django.db import models

# Create your models here.
class Notaire(models.Model):
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Telephone = models.IntegerField(max_length=100)
    Fax = models.IntegerField(max_length=100)
    Email = models.CharField(max_length=100)

    def __str__(self):
        return self.Nom

makemigrations+migrate

//register the model in app/admin

from django.contrib import admin
from .models import Notaire 
# Register your models here.
admin.site.register(Notaire)

//Create folder templates inside app 
// create page.html

a//app views add 
from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request, 'page.html')

//in project urls  add
from django.contrib import admin
from django.urls import path,include
from notaire.views import page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', page)   
]


//Add variables

// app/views
from django.shortcuts import render

# Create your views here.
def page(request):
    Test="gdfd"
    return render(request, 'page.html',  {'form': Test})   
//home.html
{{form}}

//render from model
from django.shortcuts import render
from .models import Notaire

# Create your views here.
def page(request):
    Test=Notaire.objects.all()
    return render(request, 'page.html',  {'form': Test})   



//DELETE
//add into html
<td><a href="{% url 'delete' item.id %}">DELETE</a></td>         

//add into views
def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("index")

//add into urls
    path('delete/<int:id>/', delete, name='delete'),


//UPDATE DATA
//add into html
<td><a href="{% url 'edit' item.id %}">EDIT</a></td>
//add into views
def edit (request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form' : form})
//add into urls
path('edit /<int:id>/', edit, name='edit')



