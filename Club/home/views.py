from django.shortcuts import render, get_object_or_404, redirect
from home.models import Training, Events
import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from home.forms import UserForm, ProfileForm, TrainingForm
from django.db import transaction
from django.contrib import messages

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
@transaction.atomic
def update_training(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    if request.method == 'POST':
        training_form = TrainingForm(request.POST, instance=training)
        if training_form.is_valid():
            training_form.save()
            messages.success(request, 'The training was succesfully updated!')
            return redirect('/training-detail/'+ str(training.id) +'/')
        else:
            messages.error(request, 'Please correct the error bellow')
    else:
        training_form = TrainingForm(instance=training)
    context = {
        'training_form': training_form,
    }
    return render(request, 'home/update_training.html', context)


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


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was succesfully updated!')
            return redirect('/profile/')
        else:
            messages.error(request, 'Please correct the error bellow')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'home/update_profile.html', context)

    