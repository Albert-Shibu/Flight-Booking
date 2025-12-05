import customtkinter as ctk
from PIL import Image, ImageFilter
import os
import calendar
from datetime import datetime


class FlightBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Flight")

        BLUE = {"fg": "#1E79B5", "hover": "#248ECF"}
        self.BLUE = BLUE

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ---------- Background ----------
        IMAGE_PATH = "flight-ticket-booking-service.jpg"
        if os.path.exists(IMAGE_PATH):
            self.root.state("zoomed")
            w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            img = Image.open(IMAGE_PATH).resize((w, h)).filter(ImageFilter.GaussianBlur(5))
            bg_img = ctk.CTkImage(img, size=(w, h))
            ctk.CTkLabel(self.root, image=bg_img, text="").place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.root.configure(fg_color="#1E1E1E")

        # ==========================================================
        #                     TOP NAVIGATION BAR
        # ==========================================================
        nav_frame = ctk.CTkFrame(self.root, height=60, corner_radius=0)
        nav_frame.place(relx=0, rely=0, relwidth=1)

        # --- Menu Button ---
        menu_button = ctk.CTkButton(
            nav_frame,
            text="☰",
            width=50,
            height=40,
            font=("Segoe UI", 20, "bold"),
            corner_radius=10,
            fg_color="#3B8ED0",
            hover_color="#90EE90"
        )
        menu_button.place(x=15, y=10)

        # --- Title ---
        title_label = ctk.CTkLabel(
            nav_frame,
            text="Flight Ticket Booking",
            font=("Segoe UI Semibold", 20)
        )
        title_label.place(relx=0.5, rely=0.5, anchor="center")

        # ==========================================================
        #                     SLIDE-OUT MENU PANEL
        # ==========================================================
        menu_width = 250
        self.is_menu_open = False

        menu_frame = ctk.CTkFrame(self.root, width=menu_width, fg_color="#353935", corner_radius=12)
        menu_frame.place(x=-menu_width, y=60)

        # --- Menu Buttons ---
        menu_items = {
            "Home": lambda: print("Home clicked"),
            "My Bookings": lambda: print("Bookings clicked"),
            "LogIn": lambda: print("Login clicked"),
            "SignIn": lambda: print("SignIn clicked"),
        }

        for text, action in menu_items.items():
            btn = ctk.CTkButton(
                menu_frame,
                text=text,
                corner_radius=12,
                height=40,
                fg_color="transparent",
                hover_color="#4A4A4A",
                anchor="w",
                font=("Segoe UI", 15),
                command=action
            )
            btn.pack(fill="x", pady=3, padx=10)

        # --- Menu Animation Function ---
        def animate_menu(target_x):
            current_x = menu_frame.winfo_x()
            step = 20 if target_x > current_x else -20

            def slide():
                nonlocal current_x
                if (step > 0 and current_x < target_x) or (step < 0 and current_x > target_x):
                    current_x += step
                    menu_frame.place(x=current_x, y=60)
                    self.root.after(10, slide)
                else:
                    menu_frame.place(x=target_x, y=60)

            slide()

        # --- Toggle Function ---
        def toggle_menu():
            if self.is_menu_open:
                animate_menu(-menu_width)
                self.is_menu_open = False
            else:
                menu_frame.lift()
                animate_menu(0)
                self.is_menu_open = True

        menu_button.configure(command=toggle_menu)

        # ---------- Main Frame ----------
        self.main = ctk.CTkFrame(
            self.root, width=900, height=600, corner_radius=20,
            fg_color="#1F1F1F", border_width=2, border_color="#444"
        )
        self.main.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            self.main, text="Search for Flights",
            font=("Segoe UI Semibold", 33, "bold"),
            text_color="#FFDFA6"
        ).pack(pady=(25, 10))

        # ---------- Trip Type ----------
        self.trip_var = ctk.StringVar(value="One Way")

        trip_frame = ctk.CTkFrame(self.main, fg_color="#2D2D2D", corner_radius=30)
        trip_frame.pack(pady=10)

        ctk.CTkRadioButton(
            trip_frame, text="One Way", variable=self.trip_var,
            value="One Way", command=self.update_layout
        ).pack(side="left", padx=30, pady=10)

        ctk.CTkRadioButton(
            trip_frame, text="Round Trip", variable=self.trip_var,
            value="Round Trip", command=self.update_layout
        ).pack(side="left", padx=30, pady=10)

        # ---------- Inputs Frame ----------
        self.input_frame = ctk.CTkFrame(self.main, fg_color="#2D2D2D", corner_radius=15)
        self.input_frame.pack(pady=10, padx=20, fill="x")
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=1)

        cities = [
            "New York (JFK)", "London (LHR)", "Paris (CDG)",
            "Tokyo (HND)", "Dubai (DXB)", "Singapore (SIN)", "Sydney (SYD)"
        ]

        # ----- From / To Tags -----
        ctk.CTkLabel(self.input_frame, text="From", font=("Segoe UI Semibold", 14),
                     text_color="#dcdcdc").grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")

        ctk.CTkLabel(self.input_frame, text="To", font=("Segoe UI Semibold", 14),
                     text_color="#dcdcdc").grid(row=0, column=1, padx=20, pady=(10, 0), sticky="w")

        self.from_dropdown = ctk.CTkOptionMenu(self.input_frame, values=cities)
        self.to_dropdown = ctk.CTkOptionMenu(self.input_frame, values=cities)

        self.from_dropdown.grid(row=1, column=0, padx=20, pady=(0, 15), sticky="ew")
        self.to_dropdown.grid(row=1, column=1, padx=20, pady=(0, 15), sticky="ew")

        # ----- Date Buttons -----
        self.departure_date_text = ctk.StringVar(value="Departure Date")
        self.return_date_text = ctk.StringVar(value="Return Date")

        self.departure = ctk.CTkButton(
            self.input_frame, textvariable=self.departure_date_text,
            fg_color="#3C3C3C", hover_color="#4F4F4F",
            corner_radius=14,
            command=lambda: self.open_calendar(lambda d: self.departure_date_text.set(d))
        )

        self.return_date = ctk.CTkButton(
            self.input_frame, textvariable=self.return_date_text,
            fg_color="#3C3C3C", hover_color="#4F4F4F",
            corner_radius=14,
            command=lambda: self.open_calendar(lambda d: self.return_date_text.set(d))
        )

        self.departure.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        # ---------- Passengers & Class ----------
        self.adults = ctk.IntVar(value=1)
        self.children = ctk.IntVar(value=0)
        self.infants = ctk.IntVar(value=0)
        self.class_var = ctk.StringVar(value="Economy")

        self.pc_text = ctk.StringVar()

        self.overlay = None

        ctk.CTkLabel(
            self.input_frame, text="Passengers & Class",
            font=("Segoe UI Semibold", 14), text_color="#dcdcdc"
        ).grid(row=4, column=0, padx=20, pady=(5, 0), sticky="w")

        self.pc_btn = ctk.CTkButton(
            self.input_frame, textvariable=self.pc_text,
            fg_color="#3C3C3C", hover_color="#4F4F4F",
            corner_radius=14, anchor="w", command=self.toggle_overlay
        )

        self.pc_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        self.refresh_pc_label()
        self.update_layout()

        # ---------- Search Button ----------
        ctk.CTkButton(
            self.main, text="Search Flights",
            width=250, height=45,
            corner_radius=30,
            fg_color=BLUE["fg"], hover_color=BLUE["hover"],
            font=("Segoe UI", 18, "bold")
        ).pack(pady=25)

        self.make_round(self.root, radius=20)


    # -----------------------------------------------------------
    #                 Calendar Popup
    # -----------------------------------------------------------
    def open_calendar(self, callback):
        top = ctk.CTkToplevel(self.root)
        top.grab_set()
        top.title("Select Date")
        top.geometry("380x350")
        top.resizable(False, False)

        year = datetime.now().year
        month = datetime.now().month

        header_frame = ctk.CTkFrame(top)
        header_frame.pack(pady=5)

        month_label = ctk.CTkLabel(header_frame, text="", font=("Segoe UI", 20, "bold"))
        month_label.pack()

        nav = ctk.CTkFrame(top)
        nav.pack(pady=5)

        ctk.CTkButton(nav, text="<", width=40,
                      command=lambda: change_month(-1)).pack(side="left", padx=5)
        ctk.CTkButton(nav, text=">", width=40,
                      command=lambda: change_month(+1)).pack(side="left", padx=5)

        cal_frame = ctk.CTkFrame(top)
        cal_frame.pack()

        def build_calendar(y, m):
            month_label.configure(text=f"{calendar.month_name[m]} {y}")

            for w in cal_frame.winfo_children():
                w.destroy()

            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            header = ctk.CTkFrame(cal_frame)
            header.pack()
            for d in days:
                ctk.CTkLabel(header, text=d, width=48).pack(side="left")

            dates = calendar.monthcalendar(y, m)

            for week in dates:
                row = ctk.CTkFrame(cal_frame)
                row.pack()
                for day in week:
                    if day == 0:
                        ctk.CTkLabel(row, text=" ", width=45).pack(side="left", padx=1)
                    else:
                        btn = ctk.CTkButton(
                            row, text=str(day), width=45,
                            command=lambda d=day: select_date(y, m, d)
                        )
                        btn.pack(side="left", padx=1)

        def select_date(y, m, d):
            formatted = f"{d:02d}-{m:02d}-{y}"
            callback(formatted)
            top.destroy()

        def change_month(delta):
            nonlocal month, year
            month += delta
            if month < 1:
                month, year = 12, year - 1
            elif month > 12:
                month, year = 1, year + 1
            build_calendar(year, month)

        build_calendar(year, month)

    # -----------------------------------------------------------
    #          Passengers & Class Overlay
    # -----------------------------------------------------------
    def refresh_pc_label(self):
        parts = [f"{self.adults.get()} Adult{'s' if self.adults.get() > 1 else ''}"]
        if self.children.get():
            parts.append(f"{self.children.get()} Child")
        if self.infants.get():
            parts.append(f"{self.infants.get()} Infant")
        self.pc_text.set(", ".join(parts) + f" · {self.class_var.get()}")

    def adjust(self, var, step, min_val, max_val):
        val = var.get() + step
        if var is self.infants:
            val = max(0, min(val, self.adults.get()))
        else:
            val = max(min_val, min(val, max_val))
        var.set(val)
        self.refresh_pc_label()

    def counter(self, frame, label, desc, var, min_v, max_v, row):
        ctk.CTkLabel(frame, text=label, font=("Segoe UI Semibold", 14)).grid(
            row=row, column=0, sticky="w", padx=10)
        ctk.CTkLabel(frame, text=desc, font=("Segoe UI", 11)).grid(
            row=row+1, column=0, sticky="w", padx=10)

        ctr = ctk.CTkFrame(frame, fg_color="transparent")
        ctr.grid(row=row, column=1, rowspan=2, sticky="e", padx=10)

        ctk.CTkButton(ctr, text="—", width=30,
                      command=lambda: self.adjust(var, -1, min_v, max_v)).pack(side="left")
        ctk.CTkLabel(ctr, textvariable=var, width=40).pack(side="left", padx=5)
        ctk.CTkButton(ctr, text="+", width=30,
                      command=lambda: self.adjust(var, +1, min_v, max_v)).pack(side="left")

    def toggle_overlay(self):
        if self.overlay and self.overlay.winfo_exists():
            self.overlay.destroy()
            self.overlay = None
            return

        self.overlay = ctk.CTkFrame(
            self.root, fg_color="#2A2A2A",
            corner_radius=16, border_width=1, border_color="#444"
        )
        self.overlay.place(relx=0.5, rely=0.52, anchor="n")

        row = 0
        ctk.CTkLabel(
            self.overlay, text="Passengers",
            font=("Segoe UI Semibold", 16)
        ).grid(row=row, column=0, sticky="w", padx=10, pady=8)
        row += 1

        self.counter(self.overlay, "Adults", "12+ years", self.adults, 1, 9, row); row += 2
        self.counter(self.overlay, "Children", "2-11 years", self.children, 0, 9, row); row += 2
        self.counter(self.overlay, "Infants", "<2 years", self.infants, 0, 9, row); row += 2

        ctk.CTkLabel(
            self.overlay, text="Class",
            font=("Segoe UI Semibold", 16)
        ).grid(row=row, column=0, sticky="w", padx=10, pady=8)
        row += 1

        for text in ["Economy", "Premium(First/Business)"]:
            ctk.CTkRadioButton(
                self.overlay, text=text,
                variable=self.class_var, value=text,
                fg_color=self.BLUE["fg"], hover_color=self.BLUE["hover"],
                command=self.refresh_pc_label
            ).grid(row=row, column=0, sticky="w", padx=10, pady=2)
            row += 1

        ctk.CTkButton(
            self.overlay, text="Confirm",
            fg_color=self.BLUE["fg"], hover_color=self.BLUE["hover"],
            command=lambda: (self.refresh_pc_label(), self.toggle_overlay())
        ).grid(row=row, column=0, padx=10, pady=12)

    # -----------------------------------------------------------
    #              Layout Update (One Way / Round Trip)
    # -----------------------------------------------------------
    def update_layout(self, *_):
        self.return_date.grid_forget()
        self.departure.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        if self.trip_var.get() == "Round Trip":
            self.return_date.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

        self.pc_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

    def make_round(self, widget, radius=20):
        try:
            widget.configure(corner_radius=radius)
        except:
            pass

        for child in widget.winfo_children():
            self.make_round(child, radius)


# ===================================================================
#                                RUN APP
# ===================================================================
if __name__ == "__main__":
    root = ctk.CTk()
    app = FlightBookingApp(root)
    root.mainloop()
