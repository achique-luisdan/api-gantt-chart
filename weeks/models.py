from django.db import models

class Sprint(models.Model):
    start = models.DateField()
    end = models.DateField()   
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Participant(models.Model):
    name = models.CharField(max_length=120)
    photo = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    since = models.DateField(blank=True, null=True)
    until = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=200)
    percent = models.FloatField(default=0.0)
    content = models.TextField(blank=True, null=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE,  blank=True, null=True,)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE,  blank=True, null=True,)
    
    def __str__(self):
        return self.title