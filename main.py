import customtkinter as ctk

# --- Setup Window ---
ctk.set_appearance_mode("dark")  # or "light"
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Flight Ticket Booking")
root.geometry("900x600")

# --- Top Navigation Bar Frame ---
nav_frame = ctk.CTkFrame(root, height=60, corner_radius=0)
nav_frame.pack(fill="x", side="top")

# --- Left: Menu Button ---
menu_button = ctk.CTkButton(
    nav_frame,
    text="☰",
    width=50,
    height=40,
    font=("Segoe UI", 20, "bold"),
    corner_radius=10,
    hover_color="#90EE90",
)
menu_button.place(x=15, y=10)

# --- Center: App Title ---
title_label = ctk.CTkLabel(
    nav_frame,
    text="Flight Ticket Booking",
    font=("Segoe UI Semibold", 20),
)
title_label.place(relx=0.5, rely=0.5, anchor="center")

# --- Right: Book Now Button ---
book_now_button = ctk.CTkButton(
    nav_frame,
    text="Book Now",
    width=50,
    height=40,
    font=("Segoe UI", 20, "bold"),
    corner_radius=10,
    hover_color="#90EE90",
)
book_now_button.place(relx=0.98, rely=0.5, anchor="e")


# --- Hover Effects for Nav Buttons ---
def on_hover_menu_btn(event):
    menu_button.configure(fg_color="#90EE90", text_color="black")

def on_leave_menu_btn(event):
    menu_button.configure(fg_color="#3B8ED0", text_color="white")

def on_hover_book_now_btn(event):
    book_now_button.configure(fg_color="#90EE90", text_color="black")

def on_leave_book_now_btn(event):
    book_now_button.configure(fg_color="#3B8ED0", text_color="white")

menu_button.bind("<Enter>", on_hover_menu_btn)
menu_button.bind("<Leave>", on_leave_menu_btn)
book_now_button.bind("<Enter>", on_hover_book_now_btn)
book_now_button.bind("<Leave>", on_leave_book_now_btn)

# --- Main Content Area ---
main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

# ---------- HEADER ROW ----------
header_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
header_frame.pack(fill="x", padx=20, pady=(10, 5))

# Left side label
upcoming_label = ctk.CTkLabel(header_frame, text="Upcoming Flights", font=("Segoe UI", 22, "bold"))
upcoming_label.pack(side="left")

# Right side: "Show Flight's" + dropdown
dropdown_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
dropdown_frame.pack(side="right")

show_label = ctk.CTkLabel(dropdown_frame, text="Show Flight's", font=("Segoe UI", 16))
show_label.pack(side="left", padx=(0, 10))

num_var = ctk.StringVar(value="3")
dropdown = ctk.CTkOptionMenu(
    dropdown_frame, values=["3", "5", "7", "9"], variable=num_var,
    width=60, command=lambda val: generate_flights(int(val))
)
dropdown.pack(side="right")

# ---------- FLIGHTS CONTAINER ----------
flights_container = ctk.CTkScrollableFrame(main_frame, fg_color="transparent")
flights_container.pack(fill="both", expand=True, padx=20, pady=(5, 15))


# Dummy data generator
def generate_dummy_flights(n):
    return [{
        "flight_no": f"AI-{100 + i}",
        "from": f"City {i+1}",
        "to": f"City {i+2}",
        "date": f"12 Oct 2025",
        "time": f"{10 + i}:00"
    } for i in range(n)]


# Clear and regenerate flight frames
def generate_flights(count):
    for widget in flights_container.winfo_children():
        widget.destroy()
    for flight in generate_dummy_flights(count):
        create_flight_frame(flight)


def create_flight_frame(flight_data):
    frame = ctk.CTkFrame(
        flights_container,
        corner_radius=12,
        fg_color="#252525",
        border_color="#1a1a1a",
        border_width=2,
        height=90
    )
    frame.pack(fill="x", pady=12, padx=5)

    # --- Inside Frame ---
    flight_label = ctk.CTkLabel(frame, text=f"Flight No: {flight_data['flight_no']}", font=("Segoe UI", 18, "bold"))
    flight_label.place(relx=0.02, rely=0.3, anchor="w")

    route_label = ctk.CTkLabel(frame, text=f"{flight_data['from']}  →  {flight_data['to']}", font=("Segoe UI", 16))
    route_label.place(relx=0.98, rely=0.25, anchor="e")

    datetime_label = ctk.CTkLabel(frame, text=f"Date: {flight_data['date']}   Time: {flight_data['time']}", font=("Segoe UI", 14))
    datetime_label.place(relx=0.98, rely=0.65, anchor="e")

    frame.bind("<Button-1>", lambda e: print(f"Flight clicked: {flight_data['flight_no']}"))


# Smooth scroll behavior
def smooth_scroll(event, scrollable_frame):
    canvas = scrollable_frame._parent_canvas
    direction = -1 if event.delta > 0 else 1
    pixels = 30

    def step_scroll(step=0):
        if step < pixels:
            canvas.yview_scroll(direction, "units")
            canvas.after(5, lambda: step_scroll(step + 1))

    step_scroll()


flights_container.bind("<MouseWheel>", lambda event: smooth_scroll(event, flights_container))

# Generate initial flights
generate_flights(3)

root.mainloop()
