import tkinter as tk
from tkinter import messagebox, ttk
from hotel_management import HotelManagement

# RoomBooking (Single Inheritance from tk.Toplevel)
# This class only inherits from tk.Toplevel to create a separate booking window.
class RoomBooking(tk.Toplevel):
    def __init__(self, master, hotel):
        super().__init__(master)
        self.hotel = hotel
        self.title("Book a Room")
        self.geometry("400x400")
        self.configure(bg="#A37FCF")

        ttk.Label(self, text="Enter Name:", background="#E7C6FF", foreground="black").pack(pady=5)
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(pady=5)

        ttk.Label(self, text="Select Room Type:", background="#E7C6FF", foreground="black").pack(pady=5)
        self.room_type_var = tk.StringVar(self)
        self.room_type_menu = ttk.Combobox(self, textvariable=self.room_type_var, values=["Regular", "VIP"], state="readonly")
        self.room_type_menu.pack(pady=5)
        self.room_type_menu.bind("<<ComboboxSelected>>", self.update_room_list)

        ttk.Label(self, text="Select Room:", background="#E7C6FF", foreground="black").pack(pady=5)
        self.room_var = tk.StringVar(self)
        self.room_menu = ttk.Combobox(self, textvariable=self.room_var, values=[], state="readonly")
        self.room_menu.pack(pady=5)
        self.room_menu.bind("<<ComboboxSelected>>", self.show_vip_access)

        self.vip_access_label = ttk.Label(self, text="", background="#E7C6FF", foreground="black")
        self.vip_access_label.pack(pady=5)

        ttk.Label(self, text="Select Duration:", background="#E7C6FF", foreground="black").pack(pady=5)
        self.duration_var = tk.StringVar(self, "Overnight")
        self.duration_menu = ttk.Combobox(self, textvariable=self.duration_var, values=["Overnight", "Half-day"], state="readonly")
        self.duration_menu.pack(pady=5)

        ttk.Button(self, text="Book", command=self.book_room).pack(pady=10)

    def update_room_list(self, event=None):
        """Displays both Regular and VIP rooms based on user selection"""
        selected_type = self.room_type_var.get()
        available_rooms = []

        # Get both regular and VIP rooms from HotelManagement
        available_regular = [room_no for room_no, room in self.hotel.rooms.items() if room.status == "Available"]
        available_vip = [room_no for room_no, room in self.hotel.vip_rooms.items() if room.status == "Available"]

        if selected_type == "Regular":
            available_rooms = [f"{room_no} ({self.hotel.rooms[room_no].room_type})" for room_no in available_regular]
        elif selected_type == "VIP":
            available_rooms = [f"{room_no} (VIP)" for room_no in available_vip]

        self.room_menu["values"] = available_rooms

    def show_vip_access(self, event=None):
        """Displays VIP perks when a VIP room is selected"""
        selected_room = self.room_var.get()
        if not selected_room or "VIP" not in selected_room:
            self.vip_access_label.config(text="")
            return
        room_no = int(selected_room.split(" ")[0])
        access = self.hotel.get_vip_access(room_no)
        self.vip_access_label.config(text=f"VIP Access: {', '.join(access)}")

    def book_room(self):
        """Handles room booking"""
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
