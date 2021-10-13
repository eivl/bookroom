from django.urls import path
from . import views

app_name = 'event'
urlpatterns = [
    path(
        route='',
        view=views.EventListView.as_view(),
        name='list'
    ),
    path(
        route='',
        view=views.RoomListView.as_view(),
        name='room'
    ),
]
