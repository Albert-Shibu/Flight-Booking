import customtkinter as ctk
from User_credentials_LogIn import LoginPage
from User_Credentials_SignIn import SignInPage
from dashboard import DashboardPage
from book_now import FlightBookingApp

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Flight Ticket App")
        self.geometry("900x600")

        self.frames = {}

        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        # ⭐ FIX: allow pages to expand fully
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Register pages
        for PageClass in (LoginPage, SignInPage, DashboardPage):
            page_name = PageClass.__name__
            frame = PageClass(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Start with
        self.show_page("DashboardPage")

    def show_page(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    ctk.set_widget_scaling(1.0)
    ctk.set_window_scaling(1.0)

    app = App()
    app.geometry("900x600")  # SAME SIZE ALWAYS
    app.minsize(900, 600)  # Prevent shrinking
    app.mainloop()
