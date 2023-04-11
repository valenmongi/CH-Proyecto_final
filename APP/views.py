from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.db.models import Q
# Create your views here.

def index(request):
    params = {}

    return render(request,'APP/index.html',params)


def publications(request):
    if request.method == 'POST':
        form = PublicationsForm(request.POST) 
        if form.is_valid():
            publ = Publications()
            publ.user_name = form.cleaned_data['user_name']
            publ.date_publication = form.cleaned_data['date_publication']
            publ.publication = form.cleaned_data['publication']
            publ.price_publication = form.cleaned_data['price_publication']
            publ.publication_sell = form.cleaned_data['publication_sell']
            publ.save()
            form = PublicationsForm()
        else:
            pass
    else:
        form = PublicationsForm()
    
    publications = Publications.objects.all()
    context = {"publications":publications, "form":form}
    return render(request, 'APP/publications.html', context)



def users(request):
    if request.method == 'POST':
        form = UsersForm(request.POST) 
        if form.is_valid():
            user = Users()
            user.user_name = form.cleaned_data['user_name']
            user.password = form.cleaned_data['password']
            user.name = form.cleaned_data['name']
            user.surname = form.cleaned_data['surname']
            user.save()
            form = UsersForm()
        else:
            pass
    else:
        form = UsersForm()
    
    user = Users.objects.all()
    context = {"users":user, "form":form}
    return render(request, 'APP/users.html', context)


def purchases(request):
    if request.method == 'POST':
        form = PurchasesForm(request.POST) 
        if form.is_valid():
            purch = Purchases()
            purch.user_name = form.cleaned_data['user_name']
            purch.date_purchase = form.cleaned_data['date_purchase']
            purch.purchase = form.cleaned_data['purchase']
            purch.price_purchase = form.cleaned_data['price_purchase']
            purch.save()
            form = PurchasesForm()
        else:
            pass
    else:
        form = PurchasesForm()
    
    purchases = Purchases.objects.all()
    context = {"purchases":purchases, "form":form}
    return render(request, 'APP/purchase.html', context)

