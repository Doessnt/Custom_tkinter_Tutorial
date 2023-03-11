import tkinter
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")

def button_function():
    label = ctk.CTkLabel(master = app, text = "YOU CLİCKED THE FUCKİNG BUTTON YOU IDIOT")
    
    label.pack()

# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=app, text="CTkButton", command=button_function, bg_color= "#000000")
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
