import tkinter as tk
import requests as req
import os
from tkinter import filedialog
import customtkinter
from customtkinter import *

# Initialize Tkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = CTk()
app.geometry("720x480")
app.title("File Transfer App")

# Global variables to store file path and text box reference
text_box = None
file_path = None



def fileSelectui():  
    global text_box

    # UI title
    title = customtkinter.CTkLabel(app, text="Select a file for transfer") 
    title.pack(padx=10, pady=10)

    # Button to select file
    button = customtkinter.CTkButton(app, text="Select File", command=select_file)
    button.pack(padx=10, pady=0) 

    # Text box for entering IP address
    textbox_title_label = CTkLabel(app, text="Enter Server IP Address")
    textbox_title_label.pack()
    
    text_box = CTkEntry(app, height=1, width=200)
    text_box.pack()

    # Button to send file
    sendFile_button = customtkinter.CTkButton(app, text="Send File", command=sendFile)
    sendFile_button.pack(pady=10)

    app.mainloop()

def select_file():  #where you select the file to send
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        print(f"Selected file: {file_path}")

def sendFile():  #sending the file to the server
    global text_box, file_path
    if text_box is None:
        print("Text box is not initialized!")
        return

    server_ip = text_box.get("1.0", "end-1c").strip()
    if not server_ip or not file_path:
        print("Server IP or file path missing!")
        return

    server_url = f"http://{server_ip}/upload"
    print(f"Sending file to: {server_url}")

    try:
        with open(file_path, 'rb') as file:
            files = {'file': (os.path.basename(file_path), file)}
            response = req.post(server_url, files=files)

            if response.status_code == 200:
                print("File sent successfully!")
            else:
                print(f"Failed to send file: {response.status_code}, Response: {response.text}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    fileSelectui()  # Ensure the UI launches properly
