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


def on_hover_menu_btn(event):
    menu_button.configure(
        fg_color="#90EE90",  # background when hovered
        text_color="black"   # text color when hovered
    )


def on_leave_menu_btn(event):
    menu_button.configure(
        fg_color="#3B8ED0",  # back to normal
        text_color="white"
    )


# --- Bind hover events ---
menu_button.bind("<Enter>", on_hover_menu_btn)
menu_button.bind("<Leave>", on_leave_menu_btn)


def on_hover_book_now_btn(event):
    book_now_button.configure(
        fg_color="#90EE90",  # background when hovered
        text_color="black"  # text color when hovered
    )


def on_leave_book_now_btn(event):
    book_now_button.configure(
        fg_color="#3B8ED0",  # back to normal
        text_color="white"
    )


book_now_button.bind("<Enter>", on_hover_book_now_btn)
book_now_button.bind("<Leave>", on_leave_book_now_btn)

# --- Main Content Area ---
main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()
