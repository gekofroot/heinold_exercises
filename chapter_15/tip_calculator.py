# tip calculator


from tkinter import *
from os import sys

main_window = Tk()
main_window.geometry("300x450")

BG_COLOUR = "#000011"
FG_COLOUR = "#ccffdd"



def calculate():
    meal_price = float(meal_price_entry.get())
    tip_percent = float(tip_percent_entry.get())
    tip_total = (tip_percent / 100) * meal_price
    meal_total = meal_price + tip_total
    output_label.configure(text = "meal total: {:.1f}".format(meal_total))
    meal_price_entry.delete(0, END)
    tip_percent_entry.delete(0, END)

def close_cmd():
    sys.exit()

display_usage = Label(text="tip calculator", font=("Verdana", 16), bg=BG_COLOUR, fg=FG_COLOUR) 
get_meal_price = Label(text="meal price: ", font=("Verdana", 16), bg=BG_COLOUR, fg=FG_COLOUR)
meal_price_entry = Entry(font=("Verdana", 16), bg=BG_COLOUR, fg=FG_COLOUR)
get_tip_percent = Label(text="tip percent: ", font=("Verdana", 16), bg=BG_COLOUR, fg=FG_COLOUR)
tip_percent_entry = Entry(font=("Verdana", 16), bg=BG_COLOUR, fg=FG_COLOUR)
button = Button(text="[ enter ]", font=("Verdana", 16), bg=BG_COLOUR, fg=FG_COLOUR, bd=2,
        command=calculate, relief=RAISED)
output_label = Label(font=("Verdana", 16), bg=BG_COLOUR, fg=FG_COLOUR)

display_usage.place(x=0, y=0, width=300, height=90)

get_meal_price.place(x=0, y=90, width=300, height=60)
meal_price_entry.place(x=0, y=150, width=300, height=60)

get_tip_percent.place(x=0, y=210, width=300, height=60)
tip_percent_entry.place(x=0, y=270, width=300, height=60)

button.place(x=0, y=330, width=300, height=60)
output_label.place(x=0, y=390, width=300, height=60)

top = Menu(main_window)
file = Menu(top)
file.add_command(label="close", command=close_cmd)
top.add_cascade(label="file", menu=file)
main_window.config(menu=top)

main_window.mainloop()
