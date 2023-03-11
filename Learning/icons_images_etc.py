import customtkinter as c 
import tkinter as t
from PIL import ImageTk, Image

# About application
app = c.CTk()
app.geometry("400x400")
app.title("icons, images, and exit buttons")
app.iconbitmap(r"C:\\Users\\BsRzz\\Python GUI\\images\\download.png")

my_image = ImageTk.PhotoImage(Image.open("images\download.png"))
my_label = t.Label(image=my_image)
my_label.pack()







# run the application
app.mainloop()