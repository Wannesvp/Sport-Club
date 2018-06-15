from django.contrib import admin
from .models import (Profile, Location, Rider, Level_Trainer, Trainer, Warm_up, Core, Cool_down, Training_program,Training,
Type_event, Events)

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')
    filter_horizontal = ('trainers', 'riders')

class Warm_upAdmin(admin.ModelAdmin):
    list_display = ('name','content')

class CoreAdmin(admin.ModelAdmin):
    list_display = ('name','content_1_repeat','content_1','content_2_repeat', 'content_2')

class Cool_downAdmin(admin.ModelAdmin):
    list_display = ('name','content')

admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Rider)
admin.site.register(Level_Trainer)
admin.site.register(Trainer)
admin.site.register(Warm_up, Warm_upAdmin)
admin.site.register(Core, CoreAdmin)
admin.site.register(Cool_down, Cool_downAdmin)
admin.site.register(Training_program)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Type_event)
admin.site.register(Events)