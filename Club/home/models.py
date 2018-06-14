from django.db import models
import datetime

class Location(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Rider(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self. last_name
    
    class Meta:
        ordering = ['first_name']


class Level_Trainer(models.Model):
    level = models.CharField(max_length=30)
    
    def __str__(self):
        return self.level


class Trainer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField(blank=True)
    level = models.ForeignKey(Level_Trainer, on_delete=models.CASCADE,)

    def __str__(self):
        return self.first_name + ' ' + self. last_name

    class Meta:
        ordering = ['first_name']


class Training_program(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    warm_up = models.CharField(max_length=200, blank=True)
    core = models.CharField(max_length=1000, blank=True)
    cool_down = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Training(models.Model):
    name = models.CharField(max_length=60, default='AddName')
    date = models.DateField((u"Date"), default=datetime.date.today, blank=True)
    start_time = models.TimeField((u"Start Time"), blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    trainers = models.ManyToManyField(Trainer, blank=True)
    riders = models.ManyToManyField(Rider, blank=True)
    program = models.ForeignKey(Training_program, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class type_event(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return self.level


class Events(models.Model):
    even_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255,null=True,blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    event_type = models.ForeignKey(type_event, on_delete=models.CASCADE,)

    def __str__(self):
        return self.event_name
