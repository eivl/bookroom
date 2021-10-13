from django.views.generic import ListView, DetailView

from .models import Event, Room

class EventListView(ListView):
    model = Event


class RoomListView(ListView):
    model = Room

