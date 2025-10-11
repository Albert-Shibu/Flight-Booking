import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from datetime import date

# --- Setup ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Flight Ticket Booking")
root.state('zoomed')  # Fullscreen window

# --- Scrollable Canvas ---
main_canvas = tk.Canvas(root, bg="#1a1a1a", highlightthickness=0)
scrollbar = ctk.CTkScrollbar(root, orientation="vertical", command=main_canvas.yview)
scrollable_frame = ctk.CTkFrame(main_canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
)

main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
main_canvas.configure(yscrollcommand=scrollbar.set)

main_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


# --- Calendar Popup ---
def open_calendar(entry_widget):
    top = ctk.CTkToplevel(root)
    top.title("Select Date")
    top.geometry("300x300")
    top.grab_set()
    cal = Calendar(top, selectmode="day", date_pattern="dd / mm / yyyy")
    cal.pack(pady=20)

    def pick_date():
        entry_widget.delete(0, "end")
        entry_widget.insert(0, cal.get_date())
        top.destroy()

    ctk.CTkButton(top, text="Confirm", command=pick_date).pack(pady=10)


# --- Navigation Bar ---
nav_frame = ctk.CTkFrame(scrollable_frame, height=60, corner_radius=0)
nav_frame.pack(fill="x", side="top", pady=(0, 20))

menu_button = ctk.CTkButton(
    nav_frame, text="☰", width=50, height=40,
    font=("Segoe UI", 20, "bold"), corner_radius=10,
    hover_color="#90EE90"
)
menu_button.place(x=15, y=10)

title_label = ctk.CTkLabel(
    nav_frame, text="Flight Ticket Booking", font=("Segoe UI Semibold", 22)
)
title_label.place(relx=0.5, rely=0.5, anchor="center")


# Hover color handlers
def on_hover(btn): btn.configure(fg_color="#90EE90", text_color="black")


def on_leave(btn): btn.configure(fg_color="#3B8ED0", text_color="white")


menu_button.bind("<Enter>", lambda e: on_hover(menu_button))
menu_button.bind("<Leave>", lambda e: on_leave(menu_button))

# --- Main Frame ---
main_frame = ctk.CTkFrame(scrollable_frame, corner_radius=15)
main_frame.pack(expand=True, fill="both", padx=30, pady=30)

# --- Trip Type ---
trip_type_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
trip_type_frame.pack(pady=15)
ctk.CTkLabel(trip_type_frame, text="Trip Type", font=("Segoe UI", 22, "bold")).pack(pady=5)
trip_type = ctk.StringVar(value="One Way")
for t in ["One Way", "Two Way", "Multi Way"]:
    ctk.CTkRadioButton(trip_type_frame, text=t, variable=trip_type, value=t, font=("Segoe UI", 18)).pack(side="left",
                                                                                                         padx=15)

# --- Country Selection ---
country_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
country_frame.pack(pady=20)
countries = ["India", "USA", "UK", "Germany", "France", "Japan", "Canada", "Australia"]

ctk.CTkLabel(country_frame, text="From:", font=("Segoe UI", 18)).grid(row=0, column=0, padx=10, pady=5)
from_country = ctk.CTkOptionMenu(country_frame, values=countries, width=200)
from_country.grid(row=0, column=1, padx=10)

ctk.CTkLabel(country_frame, text="To:", font=("Segoe UI", 18)).grid(row=0, column=2, padx=10, pady=5)
to_country = ctk.CTkOptionMenu(country_frame, values=countries, width=200)
to_country.grid(row=0, column=3, padx=10)

# --- Dates ---
date_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
date_frame.pack(pady=20)
ctk.CTkLabel(date_frame, text="Select Dates", font=("Segoe UI", 22, "bold")).grid(row=0, column=0, columnspan=4,
                                                                                  pady=10)

ctk.CTkLabel(date_frame, text="Departure:", font=("Segoe UI", 18)).grid(row=1, column=0, padx=10)
dep_entry = ctk.CTkEntry(date_frame, width=200)
dep_entry.grid(row=1, column=1, padx=10)
dep_entry.insert(0, date.today().strftime("%d / %m / %Y"))
ctk.CTkButton(date_frame, text="📅", width=40, command=lambda: open_calendar(dep_entry)).grid(row=1, column=2, padx=10)

ret_label = ctk.CTkLabel(date_frame, text="Return:", font=("Segoe UI", 18))
ret_label.grid(row=2, column=0, padx=10)
ret_entry = ctk.CTkEntry(date_frame, width=200)
ret_entry.grid(row=2, column=1, padx=10)
ctk.CTkButton(date_frame, text="📅", width=40, command=lambda: open_calendar(ret_entry)).grid(row=2, column=2, padx=10)

# --- Passengers ---
passenger_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
passenger_frame.pack(pady=20, fill="x")

ctk.CTkLabel(passenger_frame, text="Passengers", font=("Segoe UI", 22, "bold")).pack(pady=10)

passenger_list_frame = ctk.CTkFrame(passenger_frame, fg_color="transparent")
passenger_list_frame.pack()

passengers = []


def add_passenger():
    frame = ctk.CTkFrame(passenger_list_frame)
    frame.pack(pady=5, fill="x")

    passenger_type = ctk.StringVar(value="Adult (12+)")
    ticket_class = ctk.StringVar(value="Economy")

    ctk.CTkOptionMenu(frame, values=["Adult (12+)", "Child (0-12)"], variable=passenger_type, width=200).pack(
        side="left", padx=10)
    ctk.CTkOptionMenu(frame, values=["Economy", "Business", "First Class"], variable=ticket_class, width=200).pack(
        side="left", padx=10)

    remove_btn = ctk.CTkButton(frame, text="❌ Remove", width=80, command=lambda: remove_passenger(frame))
    remove_btn.pack(side="right", padx=10)

    passengers.append((passenger_type, ticket_class))


def remove_passenger(frame):
    frame.destroy()


add_passenger()  # Add one default passenger
ctk.CTkButton(passenger_frame, text="+ Add Passenger", command=add_passenger, width=200, height=40).pack(pady=10)


# --- Final Search Button ---
def search_flights():
    print("Trip:", trip_type.get())
    print("From:", from_country.get(), "→ To:", to_country.get())
    print("Departure:", dep_entry.get())
    print("Return:", ret_entry.get())
    print("Passengers:")
    for p_type, t_class in passengers:
        print(f"  {p_type.get()} - {t_class.get()}")
    print("Search initiated...")


final_button = ctk.CTkButton(
    main_frame, text="🔍 Search Flights", height=50,
    font=("Segoe UI", 20, "bold"), command=search_flights, hover_color="#90EE90"
)
final_button.pack(pady=30)

root.mainloop()
