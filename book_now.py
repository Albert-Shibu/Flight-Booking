import customtkinter as ctk
from PIL import Image, ImageFilter
import os

# ---------------- CONFIG ----------------
BLUE = {"fg": "#1E79B5", "hover": "#248ECF"}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Book Flight")

IMAGE_PATH = "flight-ticket-booking-service.jpg"
has_bg = os.path.exists(IMAGE_PATH)

# ---------------- BACKGROUND ----------------
if has_bg:
    root.state("zoomed")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    img = Image.open(IMAGE_PATH).resize((w, h)).filter(ImageFilter.GaussianBlur(5))
    bg_img = ctk.CTkImage(img, size=(w, h))
    ctk.CTkLabel(root, image=bg_img, text="").place(relx=0.5, rely=0.5, anchor="center")
else:
    root.configure(fg_color="#1E1E1E")

# ---------------- MAIN FRAME ----------------
main = ctk.CTkFrame(root, width=900, height=600, corner_radius=50, fg_color="#1F1F1F",
                    border_width=2, border_color="#444")
main.place(relx=0.5, rely=0.5, anchor="center")

ctk.CTkLabel(main, text="Search for Flights",
             font=("Segoe UI Semibold", 33, "bold"),
             text_color="#FFDFA6").pack(pady=(25, 10))

# ---------------- TRIP TYPE ----------------
trip_var = ctk.StringVar(value="One Way")

def update_layout(*_):
    departure.grid_forget()
    return_date.grid_forget()
    pc_btn.grid_forget()

    # Always show departure date on row 1
    departure.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    if trip_var.get() == "One Way":
        # Show Passenger/Class on its own line (row 2)
        pc_btn.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    else:
        # Show return date next to departure
        return_date.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        # Passenger/Class on next line
        pc_btn.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

trip_frame = ctk.CTkFrame(main, fg_color="#2D2D2D", corner_radius=30)
trip_frame.pack(pady=10)
ctk.CTkRadioButton(trip_frame, text="One Way", variable=trip_var,
                   value="One Way", command=update_layout).pack(side="left", padx=30, pady=10)
ctk.CTkRadioButton(trip_frame, text="Round Trip", variable=trip_var,
                   value="Round Trip", command=update_layout).pack(side="left", padx=30, pady=10)

# ---------------- INPUT FRAME ----------------
input_frame = ctk.CTkFrame(main, fg_color="#2D2D2D", corner_radius=15)
input_frame.pack(pady=10, padx=20, fill="x")
input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=1)

cities = ["New York (JFK)", "London (LHR)", "Paris (CDG)",
          "Tokyo (HND)", "Dubai (DXB)", "Singapore (SIN)", "Sydney (SYD)"]

from_dropdown = ctk.CTkOptionMenu(input_frame, values=cities)
to_dropdown = ctk.CTkOptionMenu(input_frame, values=cities)

from_dropdown.grid(row=0, column=0, padx=20, pady=15, sticky="ew")
to_dropdown.grid(row=0, column=1, padx=20, pady=15, sticky="ew")

departure = ctk.CTkEntry(input_frame, placeholder_text="Departure Date (DD-MM-YYYY)")
return_date = ctk.CTkEntry(input_frame, placeholder_text="Return Date (DD-MM-YYYY)")

# ---------------- PASSENGERS & CLASS ----------------
adults = ctk.IntVar(value=1)
children = ctk.IntVar(value=0)
infants = ctk.IntVar(value=0)
class_var = ctk.StringVar(value="Economy")

pc_text = ctk.StringVar()

def refresh_pc_label():
    parts = [f"{adults.get()} Adult{'s' if adults.get() > 1 else ''}"]
    if children.get(): parts.append(f"{children.get()} Child")
    if infants.get(): parts.append(f"{infants.get()} Infant")
    pc_text.set(", ".join(parts) + f" · {class_var.get()}")

def adjust(var, step, min_val, max_val):
    val = var.get() + step
    if var is infants:
        val = max(0, min(val, adults.get()))
    else:
        val = max(min_val, min(val, max_val))
    var.set(val)
    refresh_pc_label()

def counter(frame, label, desc, var, min_v, max_v, row):
    ctk.CTkLabel(frame, text=label, font=("Segoe UI Semibold", 14)).grid(row=row, column=0, sticky="w", padx=10)
    ctk.CTkLabel(frame, text=desc, font=("Segoe UI", 11)).grid(row=row+1, column=0, sticky="w", padx=10)

    ctr = ctk.CTkFrame(frame, fg_color="transparent")
    ctr.grid(row=row, column=1, rowspan=2, sticky="e", padx=10)

    ctk.CTkButton(ctr, text="—", width=30, command=lambda: adjust(var, -1, min_v, max_v)).pack(side="left")
    ctk.CTkLabel(ctr, textvariable=var, width=40).pack(side="left", padx=5)
    ctk.CTkButton(ctr, text="+", width=30, command=lambda: adjust(var, +1, min_v, max_v)).pack(side="left")

overlay = None

def toggle_overlay():
    global overlay
    if overlay and overlay.winfo_exists():
        overlay.destroy()
        overlay = None
        return

    overlay = ctk.CTkFrame(root, fg_color="#2A2A2A", corner_radius=16, border_width=1, border_color="#444")
    overlay.place(relx=0.5, rely=0.52, anchor="n")

    row = 0
    ctk.CTkLabel(overlay, text="Passengers", font=("Segoe UI Semibold", 16)).grid(row=row, column=0, sticky="w", padx=10, pady=8)
    row += 1

    counter(overlay, "Adults", "12+ years", adults, 1, 9, row); row += 2
    counter(overlay, "Children", "2-11 years", children, 0, 9, row); row += 2
    counter(overlay, "Infants", "<2 years", infants, 0, 9, row); row += 2

    ctk.CTkLabel(overlay, text="Class", font=("Segoe UI Semibold", 16)).grid(row=row, column=0, sticky="w", padx=10, pady=8)
    row += 1

    # BLUE radio buttons
    for text in ["Economy", "Premium Economy"]:
        ctk.CTkRadioButton(
            overlay, text=text, variable=class_var, value=text,
            fg_color=BLUE["fg"], hover_color=BLUE["hover"],
            command=refresh_pc_label
        ).grid(row=row, column=0, sticky="w", padx=10, pady=2)
        row += 1

    ctk.CTkButton(
        overlay, text="Confirm",
        fg_color=BLUE["fg"], hover_color=BLUE["hover"],
        command=lambda: (refresh_pc_label(), toggle_overlay())
    ).grid(row=row, column=0, padx=10, pady=12)

pc_btn = ctk.CTkButton(
    input_frame, textvariable=pc_text,
    fg_color="#3C3C3C", hover_color="#4F4F4F",
    corner_radius=14, anchor="w",
    command=toggle_overlay
)

refresh_pc_label()
update_layout()

# ---------------- SEARCH BUTTON ----------------
ctk.CTkButton(
    main, text="Search Flights",
    width=250, height=45,
    fg_color=BLUE["fg"], hover_color=BLUE["hover"],
    font=("Segoe UI", 18, "bold")
).pack(pady=25)

root.mainloop()