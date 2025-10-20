import tkinter as tk
from tkinter import messagebox

# Sample flight data
flights = [
    {"flight_no": "AI202", "flight_name": "Air India Express", "company": "Air India", "time": "10:00", "destination": "Mumbai"},
    {"flight_no": "6E305", "flight_name": "IndiGo Jet", "company": "IndiGo", "time": "14:30", "destination": "Chennai"},
    {"flight_no": "UK101", "flight_name": "Vistara Sky", "company": "Vistara", "time": "09:15", "destination": "Delhi"}
]

booked_flights = []

# GUI setup
root = tk.Tk()
root.title("Flight Booking System")
root.geometry("700x600")

# 🔍 Search Section
search_frame = tk.LabelFrame(root, text="Search Details", padx=10, pady=10)
search_frame.pack(padx=10, pady=10, fill="x")

search_var = tk.StringVar()

tk.Label(search_frame, text="Flight No:").grid(row=0, column=0)
search_entry = tk.Entry(search_frame, textvariable=search_var)
search_entry.grid(row=0, column=1)

def search_flight():
    query = search_var.get().strip().upper()
    for flight in flights:
        if flight["flight_no"] == query:
            show_flight_details(flight)

            return
    messagebox.showinfo("Search Result", "Flight not found!")

tk.Button(search_frame, text="Search", command=search_flight).grid(row=0, column=2)

# ✈️ Flight Details Section
details_frame = tk.LabelFrame(root, text="Flight Details", padx=10, pady=10)
details_frame.pack(padx=10, pady=10, fill="x")

def show_flight_details(flight):
    for widget in details_frame.winfo_children():
        widget.destroy()
    tk.Label(details_frame, text=f"Flight No: {flight['flight_no']}").pack()
    tk.Label(details_frame, text=f"Flight Name: {flight['flight_name']}").pack()
    tk.Label(details_frame, text=f"Company: {flight['company']}").pack()
    tk.Label(details_frame, text=f"Time: {flight['time']}").pack()
    tk.Label(details_frame, text=f"Destination: {flight['destination']}").pack()
    tk.Button(details_frame, text="Book", command=lambda: book_flight(flight)).pack(pady=5)

# ✅ Booking Logic
def book_flight(flight):
    if flight not in booked_flights:
        booked_flights.append(flight)
        messagebox.showinfo("Booking", f"{flight['flight_no']} Booked!")
    else:
        messagebox.showinfo("Booking", "Already Booked!")

# 📋 View Bookings Section
booking_frame = tk.LabelFrame(root, text="View Bookings", padx=10, pady=10)
booking_frame.pack(padx=10, pady=10, fill="x")

def view_bookings():
    for widget in booking_frame.winfo_children():
        widget.destroy()
    if not booked_flights:
        tk.Label(booking_frame, text="No bookings yet.").pack()
        return
    for flight in booked_flights:
        frame = tk.Frame(booking_frame)
        frame.pack(fill="x", pady=2)
        tk.Label(frame, text=f"{flight['flight_no']} - {flight['flight_name']} ({flight['company']})").pack(side="left")
        tk.Button(frame, text="Cancel", command=lambda f=flight: cancel_booking(f)).pack(side="right")

    def cancel_booking(flight):
        booked_flights.remove(flight)
        view_bookings()

    tk.Button(root, text="View Bookings", command=view_bookings).pack(pady=10)

    root.mainloop()
