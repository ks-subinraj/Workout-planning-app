from django.shortcuts import render, redirect
from .models import Workout
from .forms import WorkoutForm
# Create your views here.


def main_page_view(request,slug=None):
    obj = None
    if slug is not None:
        obj = Workout.objects.all().filter(slug=slug)
    
    return render(request,'main_page.html',{'obj':obj,'slug':slug})
    
def add_workout(request):
    if request.method=='POST':
        day = request.POST.get('day')
        name = request.POST.get('name')
        sets = request.POST.get('sets')
        reps = request.POST.get('reps')
        f = Workout(Day=day,slug=day,name=name,sets=sets,reps=reps)
        f.save()
        obj =Workout.objects.all().filter(slug=day)
    return render(request,'main_page.html',{'obj':obj,'slug':day})

def update(request,id):
    obj=Workout.objects.get(id=id)
    form=WorkoutForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'obj':obj})

def delete(request,id):
    if request.method == 'POST':
        obj = Workout.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
