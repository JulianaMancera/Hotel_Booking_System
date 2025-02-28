import tkinter as tk
from tkinter import ttk
from hotel_management import HotelManagement
from booking_window import RoomBooking
from admin_panel import AdminPanel

#  Main application window that provides options to book a room or open the admin panel.
class HotelBookingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.hotel = HotelManagement()
        self.title("✰ Hotel Booking System ✰")
        self.geometry("500x300")
        self.configure(bg="#9370DB")

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14), padding=10)
        style.map("TButton", background=[("active", "#8A3CC5")])

        ttk.Label(self, text="✰ Hotel Booking System ✰ ", font=("Century Schoolbook", 24, "bold"), background="#9370DB", foreground="BLACK").pack(pady=10)
        ttk.Button(self, text="Book a Room", command=self.open_booking).pack(pady=7)
        ttk.Button(self, text="Admin Panel", command=self.open_admin).pack(pady=7)
        ttk.Button(self, text="Exit", command=self.quit).pack(pady=7)

    def open_booking(self):
        RoomBooking(self, self.hotel)

    def open_admin(self):
        AdminPanel(self, self.hotel)

if __name__ == "__main__":
    app = HotelBookingApp()
    app.mainloop()
