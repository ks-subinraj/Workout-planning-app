from .models import Workout
from django import forms

class WorkoutForm(forms.ModelForm):
    
    class Meta:
        model = Workout
        fields = ("name","sets","reps")
