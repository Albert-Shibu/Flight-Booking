import customtkinter as ctk

class SignInPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        root = ctk.CTkFrame(self)
        root.pack(expand=True, fill="both")

        center = ctk.CTkFrame(root, fg_color="transparent")
        center.place(relx=0.5, rely=0.5, anchor="center")

        content = ctk.CTkFrame(center)
        content.pack(padx=20, pady=20)

        title = ctk.CTkLabel(content, text="Sign In", font=("Arial", 32, "bold"))
        title.pack(pady=(0, 20))

        self.user = ctk.CTkEntry(content, width=280, placeholder_text="Username")
        self.user.pack(pady=10)

        self.pass1 = ctk.CTkEntry(content, width=280, placeholder_text="Password", show="*")
        self.pass1.pack(pady=10)

        self.pass2 = ctk.CTkEntry(content, width=280, placeholder_text="Re-enter Password", show="*")
        self.pass2.pack(pady=10)

        sign_btn = ctk.CTkButton(content, text="Create Account", width=280)
        sign_btn.pack(pady=20)

        link = ctk.CTkLabel(
            content,
            text="Already have an account? Login",
            cursor="hand2",
            text_color="#4ea8de"
        )
        link.pack()
        link.bind("<Button-1>", lambda e: controller.show_page("LoginPage"))
