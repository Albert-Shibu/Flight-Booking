import customtkinter as ctk


class DashboardPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # ---- MAIN WINDOW FRAME (ROOT REPLACED WITH self) ----
        root = self  # So all your code works exactly the same

        # --- Top Navigation Bar Frame ---
        nav_frame = ctk.CTkFrame(root, height=60, corner_radius=0)
        nav_frame.pack(fill="x", side="top")

        # --- Left Menu Button ---
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

        # --- Title ---
        title_label = ctk.CTkLabel(
            nav_frame,
            text="Flight Ticket Booking",
            font=("Segoe UI Semibold", 20),
        )
        title_label.place(relx=0.5, rely=0.5, anchor="center")

        # --- Back Button (go to login page) ---
        back_button = ctk.CTkButton(
            nav_frame,
            text="Back",
            width=60,
            height=40,
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            hover_color="#90EE90",
            command=lambda: controller.show_page("LoginPage")
        )
        back_button.place(relx=0.98, rely=0.5, anchor="e")

        # --- Hover effects ---
        def on_hover_btn(btn, fg, tc):
            btn.configure(fg_color=fg, text_color=tc)

        def on_leave_btn(btn):
            btn.configure(fg_color="#3B8ED0", text_color="white")

        menu_button.bind("<Enter>", lambda e: on_hover_btn(menu_button, "#90EE90", "black"))
        menu_button.bind("<Leave>", lambda e: on_leave_btn(menu_button))
        back_button.bind("<Enter>", lambda e: on_hover_btn(back_button, "#90EE90", "black"))
        back_button.bind("<Leave>", lambda e: on_leave_btn(back_button))

        # --- Sliding Menu ---
        menu_width = 300
        is_menu_open = False

        menu_frame = ctk.CTkFrame(root, width=menu_width, corner_radius=12, fg_color="#353935")
        menu_frame.place(x=-menu_width, y=60, anchor="nw")

        menu_items = ["Home", "My Bookings", "Offers", "Support", "LogIn", "SignIn"]
        for item in menu_items:
            btn = ctk.CTkButton(
                menu_frame,
                text=item,
                corner_radius=12,
                height=40,
                fg_color="transparent",
                hover_color="#333333",
                anchor="w",
                font=("Segoe UI", 15),
            )
            btn.pack(fill="x", pady=2, padx=10)

        def animate_menu(target_x):
            current_x = menu_frame.winfo_x()
            step = 20 if target_x > current_x else -20

            def slide():
                nonlocal current_x
                if (step > 0 and current_x < target_x) or (step < 0 and current_x > target_x):
                    current_x += step
                    menu_frame.place(x=current_x, y=60)
                    root.after(10, slide)
                else:
                    menu_frame.place(x=target_x, y=60)

            slide()

        def toggle_menu():
            nonlocal is_menu_open
            if is_menu_open:
                animate_menu(-menu_width)
                is_menu_open = False
            else:
                menu_frame.lift()
                animate_menu(0)
                is_menu_open = True

        menu_button.configure(command=toggle_menu)

        # --- Main Content ---
        main_frame = ctk.CTkFrame(root, corner_radius=15)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        header_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        header_frame.pack(fill="x", padx=20, pady=(10, 5))

        upcoming_label = ctk.CTkLabel(header_frame, text="Results", font=("Segoe UI", 22, "bold"))
        upcoming_label.pack(side="left")

        dropdown_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        dropdown_frame.pack(side="right")

        show_label = ctk.CTkLabel(dropdown_frame, text="Show Flight's", font=("Segoe UI", 16))
        show_label.pack(side="left", padx=(0, 10))

        num_var = ctk.StringVar(value="3")

        flights_container = ctk.CTkScrollableFrame(main_frame, fg_color="transparent")
        flights_container.pack(fill="both", expand=True, padx=20, pady=(5, 15))

        def generate_dummy_flights(n):
            return [{
                "flight_no": f"AI-{100 + i}",
                "from": f"City {i+1}",
                "to": f"City {i+2}",
                "date": f"12 Oct 2025",
                "time": f"{10 + i}:00"
            } for i in range(n)]

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

            ctk.CTkLabel(frame, text=f"Flight No: {flight_data['flight_no']}",
                         font=("Segoe UI", 18, "bold")
                         ).place(relx=0.02, rely=0.3, anchor="w")

            ctk.CTkLabel(frame, text=f"{flight_data['from']}  →  {flight_data['to']}",
                         font=("Segoe UI", 16)
                         ).place(relx=0.98, rely=0.25, anchor="e")

            ctk.CTkLabel(frame, text=f"Date: {flight_data['date']}   Time: {flight_data['time']}",
                         font=("Segoe UI", 14)
                         ).place(relx=0.98, rely=0.65, anchor="e")

        def generate_flights(count):
            for widget in flights_container.winfo_children():
                widget.destroy()
            for flight in generate_dummy_flights(count):
                create_flight_frame(flight)

        dropdown = ctk.CTkOptionMenu(
            dropdown_frame, values=["3", "5", "7", "9"], variable=num_var,
            width=60, command=lambda val: generate_flights(int(val))
        )
        dropdown.pack(side="right")

        generate_flights(3)
