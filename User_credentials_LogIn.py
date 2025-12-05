import customtkinter as ctk

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # full area
        root = ctk.CTkFrame(self)
        root.pack(expand=True, fill="both")

        # center container
        center = ctk.CTkFrame(root, fg_color="transparent")
        center.place(relx=0.5, rely=0.5, anchor="center")

        # content frame
        content = ctk.CTkFrame(center)
        content.pack(padx=20, pady=20)

        title = ctk.CTkLabel(content, text="Login", font=("Arial", 32, "bold"))
        title.pack(pady=(0, 20))

        self.username = ctk.CTkEntry(content, width=280, placeholder_text="Username")
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(content, width=280, placeholder_text="Password", show="*")
        self.password.pack(pady=10)

        login_btn = ctk.CTkButton(
            content, text="Log In", width=280,
            command=lambda: controller.show_page("DashboardPage")
        )
        login_btn.pack(pady=20)

        link = ctk.CTkLabel(
            content,
            text="Don't have an account? Sign In",
            cursor="hand2",
            text_color="#4ea8de"
        )
        link.pack()
        link.bind("<Button-1>", lambda e: controller.show_page("SignInPage"))
