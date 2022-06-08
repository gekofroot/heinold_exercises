from tkinter import *

main_window = Tk()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def callback(x):
    label.configure(text="Button {} clicked".format(alphabet[x]))

label = Label()
label.grid(row=1, column=0, columnspan=26)

buttons = [0] * 26
for i in range(26):
    buttons[i] = Button(text=alphabet[i],
            command=lambda x=i: callback(x))
    buttons[i].grid(row=0, column=i)

main_window.mainloop()
