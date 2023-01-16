
from tkinter import * #importing tkinter package

root = Tk() #creating Root window

label = Label(root, text="Hello, World!")         #creating label 1
label1 = Label (root, text="Label 2")          #creating label 2

# we can add the label usig pack() and grid() function.
# By using grid() function we can place the label in specific area (x,y points)
label.grid(row=0, column=0)     
label1.grid (row=1, column=1)


root.mainloop()
