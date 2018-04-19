from django.shortcuts import render, get_object_or_404
from home.models import Training
import datetime

'''def display(request):
    monday = []
    monday_riders = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saterday = []
    sunday = []
    trainings = Training.objects.all()
    for training in trainings:
        if training.day.lower() == "monday":
            monday.append(training)
            monday_riders = monday[0].riders.all()
        if training.day.lower() == "tuesday":
            tuesday.append(training)
        if training.day.lower() == "wednesday":
            wednesday.append(training)
        if training.day.lower() == "thursday":
            thursday.append(training)
        if training.day.lower() == "friday":
            friday.append(training)
        if training.day.lower() == "saterday":
            saterday.append(training)
        if training.day.lower() == "sunday":
            sunday.append(training)

    return render(request, 'home/view_training_old.html', {'monday': monday, 'monday_riders': monday_riders, 'tuesday':tuesday, 'wednesday':wednesday, 'thursday':thursday, 'friday':friday, 'saterday':saterday,'sunday': sunday})
'''

def display_trainings(request):
    trainings = Training.objects.all()
    return render(request, 'home/view_trainings.html', {'trainings': trainings})

def display_training(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    return render(request, 'home/view_training.html', {'training': training})

