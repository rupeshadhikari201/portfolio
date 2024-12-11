from django.shortcuts import render
from .models import Experience

# Create your views here.
def experience(request):
    experience = Experience.objects.all
    return render(request, 'experience/experience.html', {'experiences': experience})