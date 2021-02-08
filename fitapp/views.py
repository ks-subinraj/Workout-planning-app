from django.shortcuts import render
from .models import Workout
# Create your views here.


def main_page_view(request,slug=None):
    obj = None
    if slug is not None:
        obj = Workout.objects.all().filter(slug=slug)
    
    return render(request,'main_page.html',{'obj':obj})
    