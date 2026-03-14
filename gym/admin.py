from django.contrib import admin
from .models import User, TrainerProfile, ClientProfile, Workout, WorkoutAssignment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['role']



class TrainerProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'trainer']


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'difficulty']


class WorkoutAssignmentAdmin(admin.ModelAdmin):
    list_display = ['client', 'trainer', 'workout']


admin.site.register(User, UserAdmin)
admin.site.register(TrainerProfile, TrainerProfileAdmin)
admin.site.register(ClientProfile, ClientProfileAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutAssignment, WorkoutAssignmentAdmin)