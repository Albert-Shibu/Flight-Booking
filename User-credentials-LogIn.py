import customtkinter as ctk

# Initialize the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Login Page")
app.geometry("500x400")

# Function to open sign-in page
def open_signin_page():
    signin_window = ctk.CTkToplevel(app)
    signin_window.title("Sign In Page")
    signin_window.geometry("400x300")

    label = ctk.CTkLabel(signin_window, text="Sign In Page", font=("Arial", 24))
    label.pack(pady=20)


# Title at top-center
login_label = ctk.CTkLabel(app, text="LogIn", font=("Arial", 32, "bold"))
login_label.pack(pady=40)

# Frame for center inputs
outer_frame = ctk.CTkFrame(app, fg_color="transparent")
outer_frame.pack()

frame = ctk.CTkFrame(outer_frame)
frame.pack(padx=20, pady=20)


# Username entry
username_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Username")
username_entry.pack(padx=10, pady=10)

# Password entry
password_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Password", show="*")
password_entry.pack(padx=10, pady=10)

# Login button
login_button = ctk.CTkButton(frame, text="Log In")
login_button.pack(pady=20)

# Bottom-right clickable sign-in text
bottom_frame = ctk.CTkFrame(app, fg_color="transparent")
bottom_frame.pack(fill="both", expand=True)

signin_label = ctk.CTkLabel(bottom_frame, text="Didn't logged in yet? Sign in by clicking here", cursor="hand2", text_color="#4ea8de")
signin_label.pack(anchor="center", padx=10, pady=10)
signin_label.bind("<Button-1>", lambda event: open_signin_page())

app.mainloop()
