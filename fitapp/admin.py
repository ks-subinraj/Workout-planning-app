from django.contrib import admin

# Register your models here.
from .models import  Workout
# admin.site.register(Day)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name','Day','slug']
    prepopulated_fields = {'slug':('Day',)}
admin.site.register(Workout,WorkoutAdmin)