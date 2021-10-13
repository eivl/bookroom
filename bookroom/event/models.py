from django.db import models
from model_utils.models import TimeFramedModel


class Room(TimeFramedModel):
    name = models.CharField('Room Name', max_length=255)

    def __str__(self):
        return self.name


class Event(TimeFramedModel):
    title = models.CharField('Event Title', max_length=255)
    all_day = models.BooleanField('All-Day event', default=False)
    start = models.DateTimeField('Event start')
    end = models.DateTimeField('Event end')
    editable = models.BooleanField('Make the event editable', default=True)
    overlap = models.BooleanField('Make the event overlapping', default=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
