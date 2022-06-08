from tkinter import *
import sys

main_window = Tk()

FONT=("Verdana", 16)
FG_COLOUR="#eeeeee"
BG_COLOUR="#777777"

# command functions
def calculate():
    temp = float(temperature_input.get())
    temp = (temp * 9 / 5) + 32
    display_temperature.configure(text="temperature in Fahrenheit: {:.1f}".format(temp))
    temperature_input.delete(0, END)

def close_cmd():
    sys.exit()

# create widgets
display_title = Label(text="temperature converter", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
get_temperature = Label(text="enter temperature", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
temperature_input = Entry(font=FONT, fg="#aaaaaa", bg=BG_COLOUR)
convert_temperature = Button(text="[ enter ]", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR,
        command=calculate)
display_temperature = Label(font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, width=32)

# place widgets
display_title.grid(row=0, column=0, columnspan=4)
get_temperature.grid(row=1, column=1)
temperature_input.grid(row=1, column=2)
convert_temperature.grid(row=2, column=0, columnspan=4)
display_temperature.grid(row=3, column=0, columnspan=4)

# create menu
top = Menu(main_window)
file = Menu(top)
file.add_command(label="Close", command=close_cmd)
top.add_cascade(label="File", menu=file)
main_window.config(menu=top)

main_window.mainloop()
