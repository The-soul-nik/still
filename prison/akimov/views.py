from django.shortcuts import render
from .models import New 
from affer.models import Tag 



def home(request):
	
	news = New.objects.all()
	return render(request, 'akimov/home.html', {'news':news},)

def detail(request, slug):
	new = New.objects.get(slug=slug)
	return render(request, 'akimov/detail.html', {'new':new})
