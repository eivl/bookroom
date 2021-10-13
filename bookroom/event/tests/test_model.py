import datetime

import pytest
from ..models import Event, Room


pytestmark = pytest.mark.django_db


def test__str__():
    room = Room.objects.create(
        name='Bedroom'
    )
    assert room.__str__() == 'Bedroom'
    assert str(room) == 'Bedroom'

    event = Event.objects.create(
        title='Status meeting',
        start=datetime.datetime.now(),
        end=datetime.datetime.now(),
        room=room,
    )

    assert event.__str__() == 'Status meeting'
    assert str(event) == 'Status meeting'
