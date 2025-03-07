from datetime import datetime
import random

# Represents a hotel room with its number, type (Queen/Single/VIP), status, and booking date.
class Room:
    def __init__(self, room_no, room_type):
        self.room_no = room_no
        self.room_type = room_type
        self.status = "Available"
        self.booking_date = None

# VIPRoom Class (Single Inheritance)
# This class manages VIP rooms separately.
class VIPRoom:
    def __init__(self):
        self.vip_rooms = {room_no: Room(room_no, "VIP") for room_no in range(201, 211)}

        # Possible VIP benefits
        self.vip_benefits = [
            "Lounge Access", "Free Breakfast", "Spa Services", "Late Checkout", 
            "Personal Butler", "Private Pool Access", "Exclusive Gym Access", 
            "Luxury Car Service", "Complimentary Drinks", "Priority Check-in"
        ]

        # Assign random benefits
        self.vip_access = {room_no: random.sample(self.vip_benefits, 2) for room_no in self.vip_rooms}

    def get_vip_access(self, room_no):
        return self.vip_access.get(room_no, [])

    def book_vip_room(self, room_no, customer_name, duration):
        if room_no in self.vip_rooms and self.vip_rooms[room_no].status == "Available":
            self.vip_rooms[room_no].status = f"Booked by {customer_name} ({duration})"
            self.vip_rooms[room_no].booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False

    def cancel_vip_booking(self, room_no):
        if room_no in self.vip_rooms and self.vip_rooms[room_no].status != "Available":
            self.vip_rooms[room_no].status = "Available"
            self.vip_rooms[room_no].booking_date = None
            return True
        return False

# HotelManagement (Multiple Inheritance)
# This class combines both regular rooms and VIP rooms by inheriting from VIPRoom.
class HotelManagement(VIPRoom):  
    def __init__(self):
        super().__init__()  # Calls VIPRoom's constructor
        self.rooms = {room_no: Room(room_no, "Queen" if room_no % 2 != 0 else "Single") for room_no in range(101, 111)}

    def book_room(self, room_no, customer_name, duration):
        if room_no in self.rooms and self.rooms[room_no].status == "Available":
            self.rooms[room_no].status = f"Booked by {customer_name} ({duration})"
            self.rooms[room_no].booking_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return self.book_vip_room(room_no, customer_name, duration)  # Calls VIPRoom method

    def cancel_booking(self, room_no):
        if room_no in self.rooms and self.rooms[room_no].status != "Available":
            self.rooms[room_no].status = "Available"
            self.rooms[room_no].booking_date = None
            return True
        return self.cancel_vip_booking(room_no)  # Calls VIPRoom method

    def get_available_rooms(self):
        """Returns a combined list of available regular and VIP rooms"""
        regular_rooms = [room_no for room_no, room in self.rooms.items() if room.status == "Available"]
        vip_rooms = [room_no for room_no, room in self.vip_rooms.items() if room.status == "Available"]
        return regular_rooms + vip_rooms
