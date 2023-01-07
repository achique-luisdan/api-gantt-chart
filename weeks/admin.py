from django.contrib import admin

from .models import Sprint, Task, Participant

admin.site.register(Sprint)

admin.site.register(Task)

admin.site.register(Participant)