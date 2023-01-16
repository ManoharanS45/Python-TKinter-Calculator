from tkinter import *

root = Tk()  #creating root window 

def button(): #creating a function called button where when we click the button the label text will be displayed.
    label = Label(root, text="You have clicked this button")
    label.pack()       # displaying label when we clicked the button

#creating buttons
button = Button(root, text="click this button", command=button)

button.pack()

root.mainloop()
