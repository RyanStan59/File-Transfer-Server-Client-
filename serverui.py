import customtkinter

def serverui(HOST, PORT):
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("File transfer App")

    title = customtkinter.CTkLabel(app, text=f"Server listening on {HOST}:{PORT}")
    title.pack(padx=10, pady=10)

    def on_close():
        print("Server is closing...")
        app.quit() 

    app.protocol("WM_DELETE_WINDOW", on_close)

    app.mainloop()
