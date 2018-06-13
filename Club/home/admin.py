from django.contrib import admin
from .models import Location, Rider, Level_Trainer, Trainer, Training_program, Training, Events

class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date')
    filter_horizontal = ('trainers', 'riders')

admin.site.register(Location)
admin.site.register(Rider)
admin.site.register(Level_Trainer)
admin.site.register(Trainer)
admin.site.register(Training_program)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Events)