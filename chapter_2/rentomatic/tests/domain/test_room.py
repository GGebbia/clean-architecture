import uuid
from rentomatic.domain import room as r

def test_room_model_init():
    code = uuid.uuid4()
    room = r.Room(code, size=200, price=10,
            latitude=500, longitude=300)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.latitude == 500
    assert room.longitude == 300


def test_room_from_dict():
    code = uuid.uuid4()
    room = r.Room.from_dict(
            {
                'code': code,
                'size': 200,
                'price': 10,
                'latitude': 500,
                'longitude': 300
            }
   )

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.latitude == 500
    assert room.longitude == 300

def test_room_to_dict():
    
    code = uuid.uuid4()
    room_dict = {
            'code': code,
            'size': 200,
            'price': 10,
            'latitude': 500,
            'longitude': 300
        }
    room = r.Room.from_dict(room_dict)

    assert room.to_dict() == room_dict

def test_room_comparison():

    code = uuid.uuid4()
    room_dict = {
            'code': code,
            'size': 200,
            'price': 10,
            'latitude': 500,
            'longitude': 300
        }
    room1 = r.Room.from_dict(room_dict)
    room2 = r.Room.from_dict(room_dict)

    assert room1 == room2


