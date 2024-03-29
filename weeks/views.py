from django.shortcuts import render
from django.http import JsonResponse

from .models import Sprint, Task, Participant

import datetime
NAME_DAYS = [
    {
        'value': 1,
        'name': 'Lun',
    }, 
    {
        'value': 2,
        'name': 'Mar',
    },
    {
        'value': 3,
        'name': 'Mié',
    }, 
    {
        'value': 4,
        'name': 'Jue',
    }, 
    {
        'value': 5,
        'name': 'Vie',
    }, 
    {
        'value': 6,
        'name': 'Sáb',
    },
    {
        'value': 7,
        'name': 'Dom',
    }
]

def get_sprints(request):
    sprints = list (Sprint.objects.values().order_by('start').reverse())
    for i, sprint in enumerate (sprints):
        start =  datetime.date(sprint.get('start').year, sprint.get('start').month, sprint.get('start').day)
        end =  datetime.date(sprint.get('end').year, sprint.get('end').month, sprint.get('end').day)
        interval = end - start 
        work_days = []
        for day in range (interval.days + 1):
            date = (start + datetime.timedelta(days = day))
            week_day = date.isoweekday()
            if (not  week_day in [6, 7]):
                work_days.append({'day': date.day, 'name': NAME_DAYS[week_day-1].get ('name'), 'date': date})
        sprint['workDays'] = work_days
    return JsonResponse(sprints, safe=False)


def get_sprint(request, sprint_id):
    sprint = Sprint.objects.get(id = sprint_id)
    tasks = list (Task.objects.filter(sprint = sprint).values())
    for i, task in enumerate (tasks):
        since =  datetime.date(task.get('since').year, task.get('since').month, task.get('since').day)
        until =  datetime.date(task.get('until').year, task.get('until').month, task.get('until').day)
        interval = until - since 
        duration = []
        for day in range (interval.days + 1):
            date = (since + datetime.timedelta(days = day))
            week_day = date.isoweekday()
            if (not  week_day in [6, 7]):
                duration.append({'day': date.day, 'name': NAME_DAYS[week_day-1].get ('name'), 'date': date})
        task['duration'] = duration
        if task.get('participant_id') != None:
           task['participant'] = Participant.objects.values().get(id = task.get('participant_id'))
           task.pop('participant_id')
    return JsonResponse(tasks, safe=False)