from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .form import ListForm
from .models import Product
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method=='POST':
      form= ListForm(request.POST or None)
      if form.is_valid():
          form.save()
          all_items=Product.objects.all
          messages.success(request,('Item Has Been Added to List!'))
          return render(request,'home.html',{'all_items':all_items})
    else:
        all_items=Product.objects.all
    return render(request,'home.html',{'all_items':all_items})

def delete(request,list_id):
    item=Product.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item Has been Deleted!'))
    return redirect('home')

def cross_off(request,list_id):
    item=Product.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('home')

def uncross(request,list_id):
    item=Product.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('home')
