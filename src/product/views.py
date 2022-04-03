from django.shortcuts import redirect, render
from .models import Product
from .form import ProductForm
# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request, 'index.html',{'products':products})

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form' : form})    

