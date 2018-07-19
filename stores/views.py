from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def store_create(request):
    store_form = StoreModelForm()
    if request.method == "POST":
        store_form = StoreModelForm(request.POST)
        if store_form.is_valid():
            store_form.save()
            return redirect('list')
    return render(request, 'store_create.html', {"store_form": store_form})

def store_detail(request, store_slug):
    context = {
        "store": Store.objects.get(slug=store_slug)
            }
    return render(request, 'store_details.html', context)



