from django.db import models

# Create your models here.
# class Day(models.Model):
#     day = models.
# class Day(models.Model):
  
#     DAY_CHOICES = [
#         (1, 'Monday'),
#         (2, 'Tuesday'),
#         (3, 'Wednesday'),
#         (4, 'Thursday'),
#         (5, 'Friday'),
#         (6, 'Saturday')
#     ]
#     Day = models.CharField(
#         max_length=2,
#         choices=DAY_CHOICES,
#         default=1,
#     )

class Workout(models.Model):
    # day = models.ForeignKey('Day',on_delete=models.CASCADE)
    Monday = 'mon'
    Tuesday = 'Tue'
    Wednesday = 'Wed'
    Thursday = 'Thur'
    Friday = 'Fri'
    Saturday = 'Sat'
    DAY_CHOICES = [
        (Monday, 'Monday'),
        (Tuesday, 'Tuesday'),
        (Wednesday, 'Wednesday'),
        (Thursday, 'Thursday'),
        (Friday, 'Friday'),
        (Saturday, 'Saturday')
    ]
    Day = models.CharField(
        max_length=4,
        choices=DAY_CHOICES,
        default=1,
    )
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    sets = models.IntegerField(default=3)
    reps = models.IntegerField(default=15) 