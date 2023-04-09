from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.


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

def inicio(request):
    return HttpResponse("Bienvenido a la pagina principal")

def inicioApp(request):
    return render(request, "APP/inicio.html")