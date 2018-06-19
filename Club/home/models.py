from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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


class Level_Trainer(models.Model):
    level = models.CharField(max_length=30)
    
    def __str__(self):
        return self.level


class Warm_up(models.Model):
    name = models.CharField(max_length=50, default="warmup")
    content = models.TextField(max_length=200, blank=True)
    content_repeat = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return self.name


class Core(models.Model):
    name = models.CharField(max_length=50, default="core")
    content_1 = models.TextField(max_length=1000, blank=True)
    content_1_repeat = models.IntegerField(default=1, blank=True, null=True, verbose_name="aantal keer")
    content_2 = models.TextField(max_length=1000, blank=True, null=True)
    content_2_repeat = models.IntegerField(default=1, blank=True, null=True, verbose_name="aantal keer")

    def __str__(self):
        return self.name


class Cool_down(models.Model):
    name = models.CharField(max_length=50, default="cooldown")
    content = models.TextField(max_length=200, blank=True)
    content_repeat = models.IntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return self.name


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
    is_standard = models.BooleanField(default=True)
    date = models.DateField((u"Date"), default=datetime.date.today, blank=True, null=True)
    start_time = models.TimeField((u"Start Time"), blank=True, null=True)
    end_time = models.TimeField((u"End Time"), blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    trainers = models.ManyToManyField(Profile, blank=True, related_name='trainer')
    riders = models.ManyToManyField(Profile, blank=True, related_name='athlete')
    program = models.ForeignKey(Training_program, on_delete=models.CASCADE, blank=True, null=True)
    warm_up = models.ForeignKey(Warm_up, on_delete=models.CASCADE, blank=True, null=True)
    core = models.ForeignKey(Core, on_delete=models.CASCADE, blank=True, null=True)
    cool_down = models.ForeignKey(Cool_down, on_delete=models.CASCADE, blank=True, null=True)

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
