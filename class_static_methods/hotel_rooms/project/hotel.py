from project.room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls,stars_count):
        name = f"{stars_count} stars Hotel"
        return cls(name)

    def add_room(self,room: Room):
        self.rooms.append(room)
    def take_room(self,room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)
        self.guests += people

    def free_room(self,room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        self.guests -= room.guests
        room.free_room()

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if r.is_taken == False]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken == True]
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)} "



