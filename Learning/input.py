import tkinter
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")



app = ctk.CTk() 
app.geometry("400x240")
app.title("HEIL HITLER")


# input widget
e = ctk.CTkEntry(app, width=150, fg_color="#03305A", border_color="black")
e.pack()


def button_function():
    label = ctk.CTkLabel(master = app, text = f"Welcom {e.get()}") #.get() for get text in the input widget
     
    label.pack()


button = ctk.CTkButton(master=app, text="Enter what you want", command=button_function, bg_color= "#000000")
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
