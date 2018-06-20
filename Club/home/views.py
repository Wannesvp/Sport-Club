from django.shortcuts import render, get_object_or_404, redirect
from home.models import Training, Event
import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from home.forms import UserForm, ProfileForm, TrainingForm, Warm_upForm, CoreForm, Cool_downForm
from django.db import transaction
from django.contrib import messages


def home(request):
    return render(request, 'home/home.html')

@login_required
def display_trainings(request):
    trainings = Training.objects.filter(is_standard=True)
    return render(request, 'home/view_trainings.html', {'trainings': trainings})

@login_required
def display_training(request, training_id):
    training = get_object_or_404(Training, pk=training_id)
    trainers = training.trainers.all()
    riders = training.riders.all()
    return render(request, 'home/view_training.html', {'training': training, 'trainers': trainers, 'riders': riders })


@login_required
def create_training(request):
    if request.method == 'POST':
        warm_upform = Warm_upForm(request.POST, prefix="warm")
        coreform = CoreForm(request.POST, prefix="core")
        cool_downform = Cool_downForm(request.POST, prefix="cool")
        if warm_upform.is_valid() and coreform.is_valid() and cool_downform.is_valid():  
            warm_upform.save()
            coreform.save()
            cool_downform.save()
            messages.success(request, 'The new training was succesfully created!')
            return redirect('/all-trainings/')
        else:
            messages.error(request, 'Please correct the error bellow')
    else:
        warm_upform = Warm_upForm(prefix="warm")
        coreform = CoreForm(prefix="core")
        cool_downform = Cool_downForm(prefix="cool")
    context = {
        'warm_upform': warm_upform,
        'coreform': coreform,
        'cool_downform': cool_downform,
    }
    return render(request, 'home/create_training.html', context)


@login_required
def create_warm_up(request):
    if request.method == 'POST':
        warm_upform = Warm_upForm(request.POST)
        if warm_upform.is_valid():  
            warm_upform.save()
            messages.success(request, 'The new training was succesfully created!')
            return redirect('/all-trainings/')
        else:
            messages.error(request, 'Please correct the error bellow')
    else:
        warm_upform = Warm_upForm()
    context = {
        'warm_upform': warm_upform,
    }
    return render(request, 'home/create_warm-up.html', context)


@login_required
def create_core(request):
    if request.method == 'POST':
        coreform = CoreForm(request.POST)
        if coreform.is_valid():
            coreform.save()
            messages.success(request, 'The new core was succesfully created!')
            return redirect('/all-trainings/')
        else:
            messages.error(request, 'Please correct the error bellow')
    else:
        coreform = CoreForm()
    context = {
        'coreform': coreform,
    }
    return render(request, 'home/create_core.html', context)


@login_required
def create_cool_down(request):
    if request.method == 'POST':
        cool_downform = Cool_downForm(request.POST)
        if cool_downform.is_valid():  
            cool_downform.save()
            messages.success(request, 'The new training was succesfully created!')
            return redirect('/all-trainings/')
        else:
            messages.error(request, 'Please correct the error bellow')
    else:
        cool_downform = Cool_downForm()
    context = {
        'cool_downform': cool_downform,
    }
    return render(request, 'home/create_cool-down.html', context)


@login_required
def plan_training(request):
    if request.method == 'POST':
        training_form = TrainingForm(request.POST)
        if training_form.is_valid():
            training_form.save()
            messages.success(request, 'The new training was succesfully created!')
            return redirect('/all-trainings/')
        else:
            messages.error(request, 'Please correct the error bellow')
    else:
        training_form = TrainingForm()
    context = {
        'training_form': training_form,
    }
    return render(request, 'home/update_training.html', context)


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
    all_events = Event.objects.all()
    get_event_types = Training.objects.only('event_type')
    all_trainings = Training.objects.filter(is_standard=False)

    # if filters applied then get parameter and filter based on condition else return object
    # code from graduaid app.
    if request.GET:  
        event_arr = []
        training_arr= []
        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.event_name
            start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

        for i in all_trainings:
            training_sub_arr = {}
            training_sub_arr['title'] = i.name
            start_date = datetime.datetime.strptime(str(i.date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            end_date = datetime.datetime.strptime(str(i.date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            training_sub_arr['start'] = start_date
            training_sub_arr['end'] = end_date
            training_arr.append(training_sub_arr)
        return HttpResponse(json.dumps(training_arr))

    context = {
        "events": all_events,
        "trainings": all_trainings,
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

    