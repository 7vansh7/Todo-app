from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import itemForm

# Create your views here.

def item(request):
    item = Item.objects.all()
    context = {'item':item}
    form = itemForm()

    if request.method == 'POST':
        form = itemForm(request.POST)   
        if form.is_valid():
           form.save()


    return render(request,'base/index.html',context)


def updateItem(request,pk):
    item = Item.objects.get(id=pk)
    form = itemForm(instance=item)

    if request.method == 'POST':
        form = itemForm(request.POST,instance=item)
        if form.is_valid:
            form.save()
            return redirect('/')
        
    context={'form':form}

    return render(request,'base/update.html',context)


def deleteItem(request,pk):
    item = Item.objects.get(id=pk)
    context = {'item':item}
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request,'base/delete.html',context)
    


           
