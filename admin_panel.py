import tkinter as tk
from tkinter import messagebox, ttk
from hotel_management import HotelManagement

# Admin panel (Multiple Inheritance from tk.Toplevel and HotelManagement)
class AdminPanel(tk.Toplevel, HotelManagement):
    def __init__(self, master, hotel):
        tk.Toplevel.__init__(self, master)
        self.hotel = hotel

        self.title("Admin Panel")
        self.geometry("800x600")
        self.configure(bg="#B09AFF")

        ttk.Label(self, text="ROOM STATUS", font=("Century Schoolbook", 14), background="#B09AFF", foreground="black").pack(pady=5)
        self.tree = ttk.Treeview(self, columns=("Room", "Type", "Status", "Booking Date"), show="headings")
        self.tree.heading("Room", text="Room No")
        self.tree.heading("Type", text="Room Type")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Booking Date", text="Booking Date")
        self.tree.pack(pady=5, fill=tk.BOTH, expand=True)

        ttk.Button(self, text="Refresh", command=self.update_list).pack(pady=5)
        ttk.Button(self, text="Cancel Booking", command=self.cancel_booking).pack(pady=5)
        self.update_list()

    def update_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for room_no, room in {**self.hotel.rooms, **self.hotel.vip_rooms}.items():
            self.tree.insert("", "end", values=(room_no, room.room_type, room.status, room.booking_date or "N/A"))

    def cancel_booking(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No room selected")
            return
        room_no = int(self.tree.item(selected_item, "values")[0])
        if self.hotel.cancel_booking(room_no):
            messagebox.showinfo("Success", f"Booking for Room {room_no} canceled")
            self.update_list()
        else:
            messagebox.showerror("Error", "Room is already available")
