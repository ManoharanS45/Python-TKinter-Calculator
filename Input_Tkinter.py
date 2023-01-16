from tkinter import * 

root = Tk()

input = Entry(root, width = 50)  #input and entry function is used to obtain input from the user
input.pack() # packing the input to the display


def buttonclick():
    label = Label(root, text=input.get())  # here we need to display the user entered text. so input.get() function is used for it.
    label.pack()

button = Button(root, text="click this button",command=buttonclick) #add the buttonclick function to the button's command
button.pack()

root.mainloop()       #finally run everything in a loop


















