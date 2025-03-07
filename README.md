# 🏨 Hotel_Booking_System

&nbsp;&nbsp;A GUI-based hotel management system built with Python (Tkinter). This system allows users to book rooms, manage reservations, and includes VIP rooms with exclusive perks.

## 📌 Features
✅ Book Regular & VIP Rooms
✅ Admin Panel for Managing Bookings
✅ VIP Rooms with Special Access Benefits
✅ Supports Different Stay Durations (Overnight/Half-day)


## 📂 Project Structure
📁 hotel-booking-system
│── HotelBookingApp.py      # Main application
│── booking_window.py       # Booking system GUI
│── admin_panel.py          # Admin dashboard
│── hotel_management.py     # Core room management (Regular & VIP)
│── README.md               # Project documentation

## 🛠 Technologies Used
- Python (Core logic)
- Tkinter (GUI)
- OOP Principles (Single & Multiple Inheritance)

## 🏨 Room Types
| Type | Room Numbers | Features |
| :-------------: | :-----: | :-----------: |
| Regular | 101 - 110 | Standard Queen/Single rooms |
| VIP | 201 - 210 | VIP access: Lounge, Spa, Free Breakfast, etc. |

Each VIP room has **two randomly assigned benefits**, such as:

- Lounge Access
- Free Breakfast
- Private Pool Access
- Luxury Car Service <br>
(see `hotel_management.py` for full list)

## 🔹 Inheritance Structure
**1️⃣ Single Inheritance** <br>
- `RoomBooking (tk.Toplevel)` → Handles the booking GUI <br>
- `VIPRoom` → Manages VIP rooms separately<br>

**2️⃣ Multiple Inheritance** <br>
- `HotelManagement (VIPRoom)` → Combines regular & VIP rooms <br>
- Calls VIP methods (book_vip_room, cancel_vip_booking)<br>
- Retrieves both regular & VIP rooms<br>

## 🚀 How to Run
**1️⃣ Install Python** <br>
- Make sure Python is installed (≥3.7).<br>

**2️⃣ Run the App**<br>
- bash - `python HotelBookingApp.py`<br>

**3️⃣ Use the Interface**
- Click `"Book a Room"` to book a regular or VIP room.
- Click `"Admin Panel"` to manage reservations.
