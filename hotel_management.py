from datetime import datetime

# Represents a hotel room with its number, type (Queen/Single), status, and booking date.
class Room:
    def __init__(self, room_no, room_type):
        self.room_no = room_no
        self.room_type = room_type
        self.status = "Available"
        self.booking_date = None

# Manages hotel room bookings and cancellations.
    # (Single Inheritance in RoomBooking, Multiple Inheritance in AdminPanel)

class HotelManagement:
    def __init__(self):
        self.rooms = {room_no: Room(room_no, "Queen" if room_no % 2 != 0 else "Single") for room_no in range(101, 111)}

    def book_room(self, room_no, customer_name, duration):
        if self.rooms[room_no].status == "Available":
            self.rooms[room_no].status = f"Booked by {customer_name} ({duration})"
            self.rooms[room_no].booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False

    def cancel_booking(self, room_no):
        if self.rooms[room_no].status != "Available":
            self.rooms[room_no].status = "Available"
            self.rooms[room_no].booking_date = None
            return True
        return False

    def get_available_rooms(self):
        return [room_no for room_no, room in self.rooms.items() if room.status == "Available"]
