
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
   # return HttpResponse("Bonjour tout le monde ")
    return render(request,'home.html')


def contact_view(request):
    #return HttpResponse('Contactez nous')
    return render (request,'contact.html')

def articles_view(request):
   return render (request, 'articles.html')

#def accueil_view(request):
  #  return HttpResponse("Binevenue sur ma page")