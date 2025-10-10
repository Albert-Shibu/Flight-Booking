import customtkinter as ctk
from tkinter import StringVar

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
    hover_color=("#2a2a2a", "#d0d0d0"),
)
menu_button.place(x=15, y=10)

# --- Center: App Title ---
title_label = ctk.CTkLabel(
    nav_frame,
    text="Flight Ticket Booking",
    font=("Segoe UI Semibold", 20),
)
title_label.place(relx=0.5, rely=0.5, anchor="center")

# --- Right: Search Entry + Icon ---
search_var = StringVar()

search_entry = ctk.CTkButton(
    nav_frame,
    text="Book Now",
    width=50,
    height=40,
    font=("Segoe UI", 20, "bold"),
    corner_radius=10,
    hover_color=("#2a2a2a", "#d0d0d0"),
)
search_entry.place(relx=0.92, rely=0.5, anchor="e")

# --- Main Content Area ---
main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()
