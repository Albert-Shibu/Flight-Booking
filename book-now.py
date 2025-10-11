import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from datetime import date

# --- Setup Window ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Flight Ticket Booking")
root.geometry("900x700")

# --- Function to open popup calendar ---
def open_calendar(entry_widget):
    # Popup window
    top = ctk.CTkToplevel(root)
    top.title("Select Date")
    top.geometry("300x300")
    top.grab_set()  # focus on popup

    # Calendar widget (from tkcalendar)
    cal = Calendar(top, selectmode="day", date_pattern="dd / mm / yyyy")
    cal.pack(pady=20)

    # Confirm button
    def pick_date():
        entry_widget.delete(0, "end")
        entry_widget.insert(0, cal.get_date())
        top.destroy()

    ctk.CTkButton(top, text="Confirm", command=pick_date).pack(pady=10)

# --- Top Navigation Bar ---
nav_frame = ctk.CTkFrame(root, height=60, corner_radius=0)
nav_frame.pack(fill="x", side="top")

menu_button = ctk.CTkButton(
    nav_frame, text="☰", width=50, height=40,
    font=("Segoe UI", 20, "bold"), corner_radius=10,
    hover_color="#90EE90"
)
menu_button.place(x=15, y=10)

title_label = ctk.CTkLabel(
    nav_frame, text="Flight Ticket Booking", font=("Segoe UI Semibold", 20)
)
title_label.place(relx=0.5, rely=0.5, anchor="center")

book_now_button = ctk.CTkButton(
    nav_frame, text="Book Now", width=50, height=40,
    font=("Segoe UI", 20, "bold"), corner_radius=10,
    hover_color="#90EE90"
)
book_now_button.place(relx=0.98, rely=0.5, anchor="e")

# Hover color handlers
def on_hover(btn): btn.configure(fg_color="#90EE90", text_color="black")
def on_leave(btn): btn.configure(fg_color="#3B8ED0", text_color="white")

menu_button.bind("<Enter>", lambda e: on_hover(menu_button))
menu_button.bind("<Leave>", lambda e: on_leave(menu_button))
book_now_button.bind("<Enter>", lambda e: on_hover(book_now_button))
book_now_button.bind("<Leave>", lambda e: on_leave(book_now_button))

# --- Main Frame ---
main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(expand=True, fill="both", padx=30, pady=30)

# --- Heading ---
heading = ctk.CTkLabel(main_frame, text="Flight Booking", font=("Segoe UI", 30, "bold"))
heading.pack(pady=(10, 25))

# --- Country Selection ---
country_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
country_frame.pack(pady=10)

countries = ["India", "USA", "UK", "Germany", "France", "Japan", "Canada", "Australia"]

from_label = ctk.CTkLabel(country_frame, text="From:", font=("Segoe UI", 18))
from_label.grid(row=0, column=0, padx=(0, 10))
from_country = ctk.CTkOptionMenu(country_frame, values=countries, width=200)
from_country.grid(row=0, column=1, padx=(0, 30))

to_label = ctk.CTkLabel(country_frame, text="To:", font=("Segoe UI", 18))
to_label.grid(row=0, column=2, padx=(0, 10))
to_country = ctk.CTkOptionMenu(country_frame, values=countries, width=200)
to_country.grid(row=0, column=3)

# --- Date Selection ---
date_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
date_frame.pack(pady=25)

date_label = ctk.CTkLabel(date_frame, text="Select Dates", font=("Segoe UI", 22, "bold"))
date_label.grid(row=0, column=0, columnspan=4, pady=(0, 20))

# Departure
dep_label = ctk.CTkLabel(date_frame, text="Departure:", font=("Segoe UI", 18))
dep_label.grid(row=1, column=0, padx=10, pady=5)
dep_entry = ctk.CTkEntry(date_frame, width=200)
dep_entry.grid(row=1, column=1, padx=10)
dep_entry.insert(0, date.today().strftime("%d / %m / %Y"))
dep_btn = ctk.CTkButton(date_frame, text="📅", width=40, command=lambda: open_calendar(dep_entry))
dep_btn.grid(row=1, column=2, padx=10)

# Return
ret_label = ctk.CTkLabel(date_frame, text="Return:", font=("Segoe UI", 18))
ret_label.grid(row=2, column=0, padx=10, pady=5)
ret_entry = ctk.CTkEntry(date_frame, width=200)
ret_entry.grid(row=2, column=1, padx=10)
ret_btn = ctk.CTkButton(date_frame, text="📅", width=40, command=lambda: open_calendar(ret_entry))
ret_btn.grid(row=2, column=2, padx=10)

# --- Travellers Section ---
traveller_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
traveller_frame.pack(pady=25)

traveller_label = ctk.CTkLabel(
    traveller_frame, text="Travellers", font=("Segoe UI", 22, "bold")
)
traveller_label.grid(row=0, column=0, columnspan=5, pady=(0, 20))

adult_count = ctk.IntVar(value=1)
child_count = ctk.IntVar(value=0)

# Adult section
adult_label = ctk.CTkLabel(traveller_frame, text="Adults (12+):", font=("Segoe UI", 18))
adult_label.grid(row=1, column=0, padx=10, pady=5)
adult_minus = ctk.CTkButton(
    traveller_frame, text="-", width=35, height=35, corner_radius=8,
    command=lambda: adult_count.set(max(0, adult_count.get() - 1))
)
adult_minus.grid(row=1, column=1, padx=5)
adult_display = ctk.CTkLabel(traveller_frame, textvariable=adult_count, width=40, font=("Segoe UI", 18))
adult_display.grid(row=1, column=2, padx=5)
adult_plus = ctk.CTkButton(
    traveller_frame, text="+", width=35, height=35, corner_radius=8,
    command=lambda: adult_count.set(adult_count.get() + 1)
)
adult_plus.grid(row=1, column=3, padx=5)

# Child section
child_label = ctk.CTkLabel(traveller_frame, text="Children (0 - 12):", font=("Segoe UI", 18))
child_label.grid(row=2, column=0, padx=10, pady=10)
child_minus = ctk.CTkButton(
    traveller_frame, text="-", width=35, height=35, corner_radius=8,
    command=lambda: child_count.set(max(0, child_count.get() - 1))
)
child_minus.grid(row=2, column=1, padx=5)
child_display = ctk.CTkLabel(traveller_frame, textvariable=child_count, width=40, font=("Segoe UI", 18))
child_display.grid(row=2, column=2, padx=5)
child_plus = ctk.CTkButton(
    traveller_frame, text="+", width=35, height=35, corner_radius=8,
    command=lambda: child_count.set(child_count.get() + 1)
)
child_plus.grid(row=2, column=3, padx=5)

# --- Final Button ---
final_button = ctk.CTkButton(
    main_frame, text="Search Flights", height=45,
    font=("Segoe UI", 20, "bold"), corner_radius=12,
    hover_color="#90EE90"
)
final_button.pack(pady=30)

root.mainloop()
