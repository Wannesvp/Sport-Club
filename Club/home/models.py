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


class Warm_up(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True)
    content_repeat = models.IntegerField(default=1)

class Core(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    content_1 = models.CharField(max_length=1000, blank=True)
    content_1_repeat = models.IntegerField(default=1)
    content_2 = models.CharField(max_length=1000, blank=True)
    content_2_repeat = models.IntegerField(default=1)

class Cool_down(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=200, blank=True)
    content_repeat = models.IntegerField(default=1)

class Training_program(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    warm_up = models.ForeignKey(Warm_up, on_delete=models.CASCADE, blank=True)
    core = models.ForeignKey(Core, on_delete=models.CASCADE, blank=True)
    cool_down = models.ForeignKey(Cool_down, on_delete=models.CASCADE, blank=True)
    
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


class Type_event(models.Model):
    type = models.CharField(max_length=30)
    
    def __str__(self):
        return self.type


class Events(models.Model):
    even_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255,null=True,blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    event_type = models.ForeignKey(Type_event, null=True,blank=True, on_delete=models.CASCADE,)

    def __str__(self):
        return self.event_name
