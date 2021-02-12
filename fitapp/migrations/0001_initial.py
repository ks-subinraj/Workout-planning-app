# Generated by Django 3.1.6 on 2021-02-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')], default=1, max_length=10)),
                ('slug', models.SlugField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sets', models.IntegerField(default=3)),
                ('reps', models.IntegerField(default=15)),
            ],
        ),
    ]
