from tkinter import *

main_window = Tk()

def callback():
    global num_clicks
    num_clicks += 1
    if num_clicks == 1:
        label.configure(text="clicked {} time".format(num_clicks))
    else:
        label.configure(text="clicked {} times".format(num_clicks))

num_clicks = 0

label = Label(text="not clicked", width=20)
button = Button(text="click me", width=10, bd=3, relief=RAISED, command=callback)

label.grid(row=0, column=0)
button.grid(row=0, column=1)


main_window.mainloop()
