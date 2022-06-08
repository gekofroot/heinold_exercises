from tkinter import *

main_window = Tk()


WIDTH=300
HEIGHT=480
FG_COLOUR = "#ccffdd"
BG_COLOUR = "#000011"
FONT = ("Verdana", 16)

main_window.geometry(f"{WIDTH}x{HEIGHT}")

def calculate():

    price = float(price_entry.get())
    discount = float(discount_entry.get())
    discount_total = (discount / 100) * price
    price_total = price - discount_total
    output_discount.configure(text = "discount amount: {:1.2f}".format(discount_total))
    output_price.configure(text = "discount price: {:1.2f}".format(price_total))
    price_entry.delete(0, END)
    discount_entry.delete(0, END)

display_title = Label(text="discount calculator", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
get_price = Label(text="price: ", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
price_entry = Entry(font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)

get_discount = Label(text="percent discount: ", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
discount_entry = Entry(font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)

enter_button = Button(text="[ enter ]", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=RAISED,
        command=calculate)
output_discount = Label(font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
output_price = Label(font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)

display_title.place(x=0, y=0, width=WIDTH, height=60)
get_price.place(x=0, y=60, width=WIDTH, height=60)
price_entry.place(x=0, y=120, width=WIDTH, height=60)
get_discount.place(x=0, y=180, width=WIDTH, height=60)
discount_entry.place(x=0, y=240, width=WIDTH, height=60)
enter_button.place(x=0, y=300, width=WIDTH, height=60)
output_discount.place(x=0, y=360, width=WIDTH, height=60)
output_price.place(x=0, y=420, width=WIDTH, height=60)

main_window.mainloop()
