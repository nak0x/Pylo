# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ #
# ██████    ██    ██  ██  ██████          ▒▒  ▒▒ #
# ██  ██  ██  ██  ████    ██  ██            ▒▒   #
# ██  ██  ██  ██  ██  ██  ██████  ██████  ▒▒  ▒▒ #
# ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡ #
# Written by Nak0_x - All Rights reserved - GNU V3

from datetime import datetime as dt
print("APP_STATUS : HOME_GUI : OK : "+str(dt.now()))

# Imports
import customtkinter as ctk
import core.core as core

class home_view(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pylo")
        self.geometry("650x550")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left_aside = ctk.CTkFrame(self)
        self.left_aside.grid(row=0, column=0, padx=(2,5), pady=2, sticky="nswe")
        
        self.home_btn = ctk.CTkButton(self.left_aside, text="Go home")
        self.home_btn.grid(row=0,column=0,padx=10,pady=10)
        self.label_1 = ctk.CTkLabel(self.left_aside, text="Hello World!")
        self.label_1.grid(row=1,column=0,padx=10,pady=(10,0), sticky="w")
        self.label_2 = ctk.CTkLabel(self.left_aside, text="My name is :")
        self.label_2.grid(row=2,column=0,padx=10, sticky="w")
        self.label_3 = ctk.CTkLabel(self.left_aside, text="Nak0_x")
        self.label_3.grid(row=3,column=0,padx=10, sticky="w")
        self.checkbox_aside = ctk.CTkCheckBox(self.left_aside, text="GUiS")
        self.checkbox_aside.grid(row=4,column=0,padx=10, pady=10)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0,column=1,padx=(5,2),pady=2, sticky="nswe")

        self.main_frame.grid_columnconfigure((0,1),weight=1)
        self.main_frame.grid_rowconfigure((0,1),weight=1)

        self.goto_frame = ctk.CTkFrame(self.main_frame)
        self.goto_frame.grid(row=0, column=0, padx=(10,5),pady=(10,5),sticky="nswe")

        self.goto_frame.grid_columnconfigure(0,weight=1)
        self.goto_frame.grid_rowconfigure((0,1),weight=1)

        self.goto_label = ctk.CTkLabel(self.goto_frame, text="Goto somewhere...")
        self.goto_label.grid(row=0, column=0, padx=10, pady=(10,5), sticky="s")
        self.goto_button = ctk.CTkButton(self.goto_frame, text="Goto !")
        self.goto_button.grid(row=1, column=0, padx=10, pady=(5,10), sticky="n")

        self.check_frame = ctk.CTkFrame(self.main_frame)
        self.check_frame.grid(row=0, column=1, padx=(5,10),pady=(10,5),sticky="nswe")

        self.check_frame.grid_columnconfigure(0,weight=1)
        self.check_frame.grid_rowconfigure((0,1),weight=1)

        self.check_label = ctk.CTkLabel(self.check_frame, text="Is your day good ?")
        self.check_label.grid(row=0, column=0, padx=10, pady=(10,5), sticky="s")
        self.check_check = ctk.CTkCheckBox(self.check_frame, text="Valid ?")
        self.check_check.grid(row=1, column=0, padx=10, pady=(5,10), sticky="n")

        self.text_frame = ctk.CTkFrame(self.main_frame)
        self.text_frame.grid(row=1,column=0, padx=10, pady=(5,10), sticky="nswe", columnspan=2)

        self.text_frame.grid_columnconfigure(0, weight=1)
        self.text_frame.grid_rowconfigure(1, weight=1)

        self.text_label = ctk.CTkLabel(self.text_frame, text="Write here ;)")
        self.text_label.grid(row=0, column=0, padx=10, pady=(10,5), sticky="nw")
        self.textbox = ctk.CTkTextbox(self.text_frame)
        self.textbox.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")


    def stop_exec(self):
        core._STOP_EXEC()