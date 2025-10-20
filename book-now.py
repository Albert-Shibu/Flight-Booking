# -----------------------------------------------------
# Project Name : Flight Ticket Booking System
# Subject      : Computer Science (Class 12 - CBSE)
# Developed By : (Your Name)
# Language     : Python
# GUI Library  : CustomTkinter & tkcalendar
# -----------------------------------------------------

# Import necessary libraries
import customtkinter as ctk
from tkcalendar import Calendar
from datetime import date

# ----------------------- MAIN WINDOW -----------------------
ctk.set_appearance_mode("dark")        # Appearance mode (dark/light)
ctk.set_default_color_theme("blue")    # Default color theme

root = ctk.CTk()
root.title("Flight Tickets")
root.state('zoomed')                   # Full-screen window

# Set all backgrounds to grey
root.configure(fg_color="#3a3a3a")

# ----------------------- FUNCTION SECTION -----------------------
def open_calendar(entry_widget):
    """Function to open calendar and select date"""
    top = ctk.CTkToplevel(root)
    top.title("Select Date")
    top.geometry("300x300")
    top.grab_set()  # Keeps popup on top

    cal = Calendar(top, selectmode="day", date_pattern="dd / mm / yyyy")
    cal.pack(pady=20)

    def pick_date():
        entry_widget.delete(0, "end")
        entry_widget.insert(0, cal.get_date())
        top.destroy()

    ctk.CTkButton(top, text="Confirm Date", command=pick_date).pack(pady=10)

# ----------------------- HEADING SECTION -----------------------
nav_frame = ctk.CTkFrame(root, height=60, corner_radius=0, fg_color="#3a3a3a")
nav_frame.pack(fill="x", pady=(0, 20))

# Title label with flight emoji
title_label = ctk.CTkLabel(nav_frame, text="✈️  Flight Tickets", font=("Arial", 26, "bold"))
title_label.place(relx=0.5, rely=0.5, anchor="center")

# ----------------------- TRIP TYPE SECTION -----------------------
trip_frame = ctk.CTkFrame(root, fg_color="#3a3a3a")
trip_frame.pack(pady=10)

ctk.CTkLabel(trip_frame, text="Trip Type:", font=("Arial", 18, "bold")).pack(pady=5)
trip_type = ctk.StringVar(value="One Way")

def update_return_date():
    """Show or hide Return Date according to Trip Type"""
    if trip_type.get() == "One Way":
        ret_label.grid_forget()
        ret_entry.grid_forget()
        ret_btn.grid_forget()
    else:
        ret_label.grid(row=1, column=0, padx=10, pady=5)
        ret_entry.grid(row=1, column=1, padx=10)
        ret_btn.grid(row=1, column=2, padx=10)

for t in ["One Way", "Round Trip", "Multi Way"]:
    ctk.CTkRadioButton(trip_frame, text=t, variable=trip_type, value=t, command=update_return_date).pack(side="left", padx=10)

# ----------------------- COUNTRY SELECTION -----------------------
country_frame = ctk.CTkFrame(root, fg_color="#3a3a3a")
country_frame.pack(pady=20)

countries = ["India", "USA", "UK", "Germany", "France", "Japan", "Canada", "Australia"]

ctk.CTkLabel(country_frame, text="From:").grid(row=0, column=0, padx=10, pady=5)
from_country = ctk.CTkOptionMenu(country_frame, values=countries, width=150)
from_country.grid(row=0, column=1, padx=10)

ctk.CTkLabel(country_frame, text="To:").grid(row=0, column=2, padx=10, pady=5)
to_country = ctk.CTkOptionMenu(country_frame, values=countries, width=150)
to_country.grid(row=0, column=3, padx=10)

# ----------------------- DATE SELECTION -----------------------
date_frame = ctk.CTkFrame(root, fg_color="#3a3a3a")
date_frame.pack(pady=20)

# Departure Date
ctk.CTkLabel(date_frame, text="Departure Date:").grid(row=0, column=0, padx=10, pady=5)
dep_entry = ctk.CTkEntry(date_frame, width=150)
dep_entry.grid(row=0, column=1, padx=10)
dep_entry.insert(0, date.today().strftime("%d/%m/%Y"))
ctk.CTkButton(date_frame, text="📅", command=lambda: open_calendar(dep_entry)).grid(row=0, column=2, padx=10)

# Return Date
ret_label = ctk.CTkLabel(date_frame, text="Return Date:")
ret_entry = ctk.CTkEntry(date_frame, width=150)
ret_btn = ctk.CTkButton(date_frame, text="📅", command=lambda: open_calendar(ret_entry))
update_return_date()

# ----------------------- PASSENGER SECTION -----------------------
passenger_frame = ctk.CTkFrame(root, fg_color="#3a3a3a")
passenger_frame.pack(pady=20)

ctk.CTkLabel(passenger_frame, text="Passenger Details", font=("Arial", 18, "bold")).pack(pady=5)
passenger_list_frame = ctk.CTkFrame(passenger_frame, fg_color="#3a3a3a")
passenger_list_frame.pack(pady=5)

passengers = []

def add_passenger():
    """Add a new passenger"""
    frame = ctk.CTkFrame(passenger_list_frame, fg_color="#4a4a4a", corner_radius=10)
    frame.pack(pady=5, padx=10, fill="x")

    p_type = ctk.StringVar(value="Adult (12+)")
    p_class = ctk.StringVar(value="Economy")

    ctk.CTkOptionMenu(frame, values=["Adult (12+)", "Child (0-12)"], variable=p_type, width=150).pack(side="left", padx=5)
    ctk.CTkOptionMenu(frame, values=["Economy", "Business", "First Class"], variable=p_class, width=150).pack(side="left", padx=5)

    # Cube-like red remove button
    remove_btn = ctk.CTkButton(
        frame, text="X", width=30, height=30, corner_radius=4,
        fg_color="#a83232", hover_color="#d64040", font=("Arial", 14, "bold"),
        command=lambda: frame.destroy()
    )
    remove_btn.pack(side="left", padx=8)

    passengers.append((p_type, p_class))

# Add one default passenger
add_passenger()

ctk.CTkButton(passenger_frame, text="Add Passenger", command=add_passenger).pack(pady=10)

# ----------------------- SEARCH BUTTON -----------------------
def search_flights():
    """Display flight details in console"""
    print("----- Flight Search Summary -----")
    print("Trip Type:", trip_type.get())
    print("From:", from_country.get(), "→ To:", to_country.get())
    print("Departure Date:", dep_entry.get())

    if trip_type.get() != "One Way":
        print("Return Date:", ret_entry.get())

    print("Passengers:")
    for p_type, p_class in passengers:
        print(f"  {p_type.get()} - {p_class.get()}")

    print("----------------------------------")

# Main action button
ctk.CTkButton(root, text="Search Flights", command=search_flights, width=200, height=40).pack(pady=20)

# ----------------------- RUN APPLICATION -----------------------
root.mainloop()
