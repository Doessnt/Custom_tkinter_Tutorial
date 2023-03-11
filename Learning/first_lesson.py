from customtkinter import *

root = CTk()




# Creating a label Widgets 
myLabel1 = CTkLabel(root, text="Hello, World!")
myLabel2 = CTkLabel(root, text="My name is Hitler")
myLabel3 = CTkLabel(root, text="                             ")


# Showing  it onto the screen
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 3)
myLabel3.grid(row = 1, column = 1)










# For 
root.mainloop()
