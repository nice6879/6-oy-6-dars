from django.shortcuts import render
from .models import Food

def home(request):
    foods = Food.objects.all()
    return render(request, 'base.html', context={"foods":foods})
