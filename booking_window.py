import tkinter as tk
from tkinter import messagebox, ttk
from hotel_management import HotelManagement

# Booking window (Single Inheritance from tk.Toplevel)

    #Handles the GUI for booking a room.
    # Inherits from tk.Toplevel (Single Inheritance).

class RoomBooking(tk.Toplevel):
    def __init__(self, master, hotel):
        super().__init__(master)
        self.hotel = hotel
        self.title("Book a Room")
        self.geometry("400x300")
        self.configure(bg="#A37FCF")

        ttk.Label(self, text="Enter Name:", background="#E7C6FF", foreground="black").pack(pady=5)
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)

        ttk.Label(self, text="Select Room:", background="#E7C6FF", foreground="black").pack(pady=5)
        self.room_var = tk.StringVar(self)
        available_rooms = [f"{room_no} ({self.hotel.rooms[room_no].room_type})" for room_no in self.hotel.get_available_rooms()]
        self.room_menu = ttk.Combobox(self, textvariable=self.room_var, values=available_rooms, state="readonly")
        self.room_menu.pack(pady=5)

        ttk.Label(self, text="Select Duration:", background="#E7C6FF", foreground="black").pack(pady=5)
        self.duration_var = tk.StringVar(self, "Overnight")
        self.duration_menu = ttk.Combobox(self, textvariable=self.duration_var, values=["Overnight", "Half-day"], state="readonly")
        self.duration_menu.pack(pady=5)

        ttk.Button(self, text="Book", command=self.book_room).pack(pady=10)

    def book_room(self):
        name = self.name_entry.get()
        selected_room = self.room_var.get()
        if not selected_room:
            messagebox.showerror("Error", "No room selected")
            return
        room_no = int(selected_room.split(" ")[0])
        duration = self.duration_var.get()
        if self.hotel.book_room(room_no, name, duration):
            messagebox.showinfo("Success", f"Room {room_no} booked for {duration}!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Room not available")