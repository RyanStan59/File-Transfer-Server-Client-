import tkinter as tk
from tkinter import filedialog
import customtkinter

def clientui():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("File Transfer App")

    title = customtkinter.CTkLabel(app, text="Select a file for transfer") 
    title.pack(padx=10, pady=10)

    button = customtkinter.CTkButton(app, text="Select File", command=select_file)
    button.pack(padx=10, pady=10) 

    app.mainloop()

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")
