import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

placeholder_img = "C:\\Users\\mhmts\\PycharmProjects\\qr_code\\qr+progress\\1 qr\\1 intro\\Placeholder.png"

class App(ctk.CTk):
    def __init__(self):
        # window setup
        ctk.set_appearance_mode("light")
        super().__init__(fg_color="white")

        # customization
        self.geometry("400x400")
        self.iconbitmap("C:\\Users\\mhmts\\PycharmProjects\\qr_code\\qr+progress\\1 qr\\1 intro\\empty.ico")
        self.title("")

        # Entry field
        EntryField(self)

        # QR code
        image = Image.open(placeholder_img).resize((200,200))
        image_tk = ImageTk.PhotoImage(image)
        self.qr_image = QrImage(self)
        self.qr_image.update_image(image_tk)

        # running the app
        self.mainloop()
        

class EntryField(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, corner_radius=20, fg_color="#021FB3")
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")

        # grid layout
        self.rowconfigure((0,1), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")

        # widgets
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.columnconfigure(0, weight=1, uniform="b")
        self.frame.columnconfigure(1, weight=4, uniform="b")
        self.frame.columnconfigure(2, weight=2, uniform="b")
        self.frame.columnconfigure(3, weight=1, uniform="b")
        self.frame.grid(row=0, column=0)

        entry = ctk.CTkEntry(self.frame, fg_color="#2E54E8", border_width=0,text_color="white")
        entry.grid(row=0, column=1, sticky="nsew")

        button = ctk.CTkButton(self.frame, text="Save", fg_color="#2E54E8", hover_color="#4266f1")
        button.grid(row=0, column=2, sticky="nsew", padx=10)

class QrImage(tk.Canvas):
    def __init__(self, parent):
        super().__init__(master=parent, background="red", bd=0,highlightthickness=0,relief="ridge")
        self.place(relx=0.5, rely=0.4, width=200, height=200, anchor="center")
    
    def update_image(self, image_tk):
        self.create_image(0,0, image=image_tk,anchor="nw")


App()