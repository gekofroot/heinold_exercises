# import modules
from tkinter import *
import sys

main_window = Tk()
main_window.geometry("400x300")

# variables
FONT=("Verdana", 16)
FG_COLOUR="#eeeeee"
BG_COLOUR="#777777"


# command functions
def calculate():
    temp = float(temperature_input.get())
    temp = (temp * 9 / 5) + 32
    display_temperature.configure(text = "{:.1f} degrees F".format(temp))
    temperature_input.delete(0, END)

def close_cmd():
    sys.exit()

# create widgets
display_title = Label(text="temperature converter", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
get_temperature = Label(text="enter temperature", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
temperature_input = Entry(font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
convert_button = Button(text="[ enter ]", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=RAISED, command=calculate)
display_temperature = Label(font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)

# display widgets
display_title.place(x=0, y=0, width=400, height=60)
get_temperature.place(x=0, y=60, width=400, height=60)
temperature_input.place(x=0, y=120, width=400, height=60)
convert_button.place(x=0, y=180, width=400, height=60)
display_temperature.place(x=0, y=240, width=400, height=60)

# create menu
top = Menu(main_window)
file = Menu(top)
file.add_command(label="Close", command=close_cmd)
top.add_cascade(label="File", menu=file)
main_window.config(menu=top)


main_window.mainloop()
