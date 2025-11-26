import customtkinter as ctk
import subprocess
import sys

# Initialize the app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("SignIn Page")
app.geometry("600x500")

# Title at top-center
login_label = ctk.CTkLabel(app, text="SignIn", font=("Arial", 32, "bold"))
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

password_entry2 = ctk.CTkEntry(frame, width=250, placeholder_text="Re-Enter Password", show="*")
password_entry2.pack(padx=10, pady=10)

# Login button
login_button = ctk.CTkButton(frame, text="Sign In")
login_button.pack(pady=20)

# Bottom-right clickable sign-in text
bottom_frame = ctk.CTkFrame(app, fg_color="transparent")
bottom_frame.pack(fill="both", expand=True)

signin_label = ctk.CTkLabel(bottom_frame, text="Already Logged in? Log in by clicking here", cursor="hand2", text_color="#4ea8de")
signin_label.pack(anchor="center", padx=10, pady=10)
signin_label.bind("<Button-1>", lambda event: open_login_page())


def open_login_page():
    subprocess.Popen([sys.executable, "User-credentials-Login.py"])  # or "python3" on mac/linux

app.mainloop()
