from django.shortcuts import render, get_object_or_404, redirect
from home.models import Training, Events
import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


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

def home(request):
    return render(request, 'home/home.html')

@login_required
def display_trainings(request):
    trainings = Training.objects.all()
    return render(request, 'home/view_trainings.html', {'trainings': trainings})

@login_required
def display_training(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    return render(request, 'home/view_training.html', {'training': training})

@login_required
def display_calendar(request):
    all_events = Training.objects.all()
    get_event_types = Training.objects.only('event_type')

    # if filters applied then get parameter and filter based on condition else return object
    # code from graduaid app.
    if request.GET:  
        event_arr = []
        
        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.name
            start_date = datetime.datetime.strptime(str(i.date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,

    }
    return render(request,'home/calendar.html',context)

@login_required
def display_profile(request):
    return render(request, 'home/profile.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})