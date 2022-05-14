from tkinter import Place
from django.shortcuts import render
from .models import Places

# Create your views here.
def index(request):

    dest1 = Places()
    dest1.name = 'chennai'
    dest1.price = 700
    dest1.img = 'f3.jpg'
    dest1.days = 7
    dest1.rev = False
    


    dest2=Places()
    dest2.name = 'Mangalore'
    dest2.price = 1000
    dest2.img = 'f2.jpg'
    dest2.days = 10
    dest2.rev = False
    

    dest3=Places()
    dest3.name ='Kerala'
    dest3.price = 20000
    dest3.img = 'f1.jpg'
    dest3.days = 15
    dest3.rev = True



    dests=[dest1,dest2,dest3]




    return render(request, 'index.html' , {'dests': dests})