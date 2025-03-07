# 🏨 Hotel_Booking_System

&nbsp;&nbsp;&nbsp;&nbsp;A GUI-based hotel management system built with Python (Tkinter). This system allows users to book rooms, manage reservations, and includes VIP rooms with exclusive perks.

## 📌 Features
✅ Book Regular & VIP Rooms <br>
✅ Admin Panel for Managing Bookings <br>
✅ VIP Rooms with Special Access Benefits <br>
✅ Supports Different Stay Durations (Overnight/Half-day) <br>


## 📂 Project Structure
![image](https://github.com/user-attachments/assets/aae6d501-6162-4b5e-beb1-777f55e6e35e)


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
