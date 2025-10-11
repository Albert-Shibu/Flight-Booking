import customtkinter as ctk
from tkcalendar import Calendar
from datetime import date

# ---------------- Setup Window ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Flight Ticket Booking")
root.state('zoomed')  # Full screen window

# ---------------- Function: Calendar Popup ----------------
def open_calendar(entry_widget):
    top = ctk.CTkToplevel(root)
    top.title("Select Date")
    top.geometry("300x300")
    top.grab_set()  # focus on popup

    cal = Calendar(top, selectmode="day", date_pattern="dd / mm / yyyy")
    cal.pack(pady=20)

    def pick_date():
        entry_widget.delete(0, "end")
        entry_widget.insert(0, cal.get_date())
        top.destroy()

    ctk.CTkButton(top, text="Confirm", command=pick_date).pack(pady=10)

# ---------------- Navigation Bar ----------------
nav_frame = ctk.CTkFrame(root, height=60, corner_radius=0)
nav_frame.pack(fill="x", side="top", pady=(0, 20))

menu_button = ctk.CTkButton(nav_frame, text="☰", width=50, height=40, font=("Segoe UI", 20, "bold"))
menu_button.place(x=15, y=10)

title_label = ctk.CTkLabel(nav_frame, text="Flight Ticket Booking", font=("Segoe UI Semibold", 22))
title_label.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- Trip Type ----------------
trip_frame = ctk.CTkFrame(root)
trip_frame.pack(pady=10)

ctk.CTkLabel(trip_frame, text="Trip Type", font=("Segoe UI", 22, "bold")).pack()
trip_type = ctk.StringVar(value="One Way")

def update_return_date():
    """Show or hide return date based on trip type"""
    if trip_type.get() == "One Way":
        ret_label.grid_forget()
        ret_entry.grid_forget()
        ret_btn.grid_forget()
    else:
        ret_label.grid(row=1, column=0, padx=10, pady=5)
        ret_entry.grid(row=1, column=1, padx=10)
        ret_btn.grid(row=1, column=2, padx=10)

for t in ["One Way", "Two Way", "Multi Way"]:
    ctk.CTkRadioButton(trip_frame, text=t, variable=trip_type, value=t, command=update_return_date).pack(side="left", padx=10)

# ---------------- Country Selection ----------------
country_frame = ctk.CTkFrame(root)
country_frame.pack(pady=20)

countries = ["India", "USA", "UK", "Germany", "France", "Japan", "Canada", "Australia"]

ctk.CTkLabel(country_frame, text="From:").grid(row=0, column=0, padx=10)
from_country = ctk.CTkOptionMenu(country_frame, values=countries, width=150)
from_country.grid(row=0, column=1, padx=10)

ctk.CTkLabel(country_frame, text="To:").grid(row=0, column=2, padx=10)
to_country = ctk.CTkOptionMenu(country_frame, values=countries, width=150)
to_country.grid(row=0, column=3, padx=10)

# ---------------- Dates ----------------
date_frame = ctk.CTkFrame(root)
date_frame.pack(pady=20)

ctk.CTkLabel(date_frame, text="Departure Date:").grid(row=0, column=0, padx=10, pady=5)
dep_entry = ctk.CTkEntry(date_frame, width=150)
dep_entry.grid(row=0, column=1, padx=10)
dep_entry.insert(0, date.today().strftime("%d/%m/%Y"))
ctk.CTkButton(date_frame, text="📅", command=lambda: open_calendar(dep_entry)).grid(row=0, column=2, padx=10)

# Return Date (will be hidden if One Way)
ret_label = ctk.CTkLabel(date_frame, text="Return Date:")
ret_entry = ctk.CTkEntry(date_frame, width=150)
ret_btn = ctk.CTkButton(date_frame, text="📅", command=lambda: open_calendar(ret_entry))

update_return_date()  # Initialize visibility based on default trip type

# ---------------- Passengers ----------------
passenger_frame = ctk.CTkFrame(root)
passenger_frame.pack(pady=20)

ctk.CTkLabel(passenger_frame, text="Passengers", font=("Segoe UI", 22, "bold")).pack(pady=10)
passenger_list_frame = ctk.CTkFrame(passenger_frame)
passenger_list_frame.pack()

passengers = []

def add_passenger():
    frame = ctk.CTkFrame(passenger_list_frame)
    frame.pack(pady=5)

    p_type = ctk.StringVar(value="Adult (12+)")
    p_class = ctk.StringVar(value="Economy")

    ctk.CTkOptionMenu(frame, values=["Adult (12+)", "Child (0-12)"], variable=p_type, width=150).pack(side="left", padx=5)
    ctk.CTkOptionMenu(frame, values=["Economy", "Business", "First Class"], variable=p_class, width=150).pack(side="left", padx=5)
    ctk.CTkButton(frame, text="x", command=lambda: frame.destroy()).pack(side="left", padx=5)

    passengers.append((p_type, p_class))

add_passenger()  # default passenger

ctk.CTkButton(passenger_frame, text="Add Passenger", command=add_passenger).pack(pady=10)

# ---------------- Search Button ----------------
def search_flights():
    print("Trip Type:", trip_type.get())
    print("From:", from_country.get(), "→ To:", to_country.get())
    print("Departure:", dep_entry.get())
    if trip_type.get() != "One Way":
        print("Return:", ret_entry.get())
    print("Passengers:")
    for p_type, p_class in passengers:
        print(f"  {p_type.get()} - {p_class.get()}")

ctk.CTkButton(root, text="Search Flights", command=search_flights, width=200, height=40).pack(pady=20)

root.mainloop()
