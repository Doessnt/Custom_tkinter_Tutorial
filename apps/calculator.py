import customtkinter as c
from tkinter import END, BOTH, LEFT

# application
app = c.CTk()
app.title("Calculator")


#functions
def button_click(number):
    
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)

def button_add():
  first_number = e.get()
  global f_num
  f_num = int(first_number)
  e.delete(0, END)
  
def button_equal():
    print("Clicked")
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))

# e = Input top of the screen
e = c.CTkEntry(master = app, width=300, border_width=5)
e.grid(row = 0, column =0, columnspan=3)





#  Define Buttons 
button_1 = c.CTkButton(app, text = "1", command=lambda: button_click(1))
button_2 = c.CTkButton(app, text = "2", command=lambda: button_click(2))
button_3 = c.CTkButton(app, text = "3", command=lambda: button_click(3))
button_4 = c.CTkButton(app, text = "4", command=lambda: button_click(4))
button_5 = c.CTkButton(app, text = "5", command=lambda: button_click(5))
button_6 = c.CTkButton(app, text = "6", command=lambda: button_click(6))
button_7 = c.CTkButton(app, text = "7", command=lambda: button_click(7))
button_8 = c.CTkButton(app, text = "8", command=lambda: button_click(8))
button_9 = c.CTkButton(app, text = "9", command=lambda: button_click(9))
button_0 = c.CTkButton(app, text = "0", command=lambda: button_click(0))
button_add = c.CTkButton(app, text = "+", command=button_add)
button_equal = c.CTkButton(app, text = "=", command=button_equal)
button_clear = c.CTkButton(app, text = "C", command= button_clear)

# Put the button on the screen

button_1.grid(row = 3, column =0, padx = 40, pady = 20)
button_2.grid(row = 3, column =1, padx = 40, pady = 20)
button_3.grid(row = 3, column =2, padx = 40, pady = 20)

button_4.grid(row = 2, column =0, padx = 40, pady = 20)
button_5.grid(row = 2, column =1, padx = 40, pady = 20)
button_6.grid(row = 2, column =2, padx = 40, pady = 20)

button_7.grid(row = 1, column =0, padx = 40, pady = 20)
button_8.grid(row = 1, column =1, padx = 40, pady = 20)
button_9.grid(row = 1, column =2, padx = 40, pady = 20)

button_0.grid(row = 4, column =0, padx = 40, pady = 20)

button_add.grid(row = 5, column = 0, padx = 39, pady = 20)
button_equal.grid(row = 5, column =2, padx = 40, pady = 20, columnspan=2)
button_clear.grid(row = 4, column =2, padx = 40, pady = 20, columnspan=2) 




# run 
app.mainloop()
