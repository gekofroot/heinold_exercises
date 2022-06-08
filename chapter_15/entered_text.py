from tkinter import *

main_window = Tk()
main_window.geometry("400x270")

def print_text():
    get_input = float(enter_input.get())
    print_text_output.configure(text="text is {}".format(get_input))
    enter_input.delete(0, END)

buttonframe = LabelFrame(main_window, font=("Verdana", 16), fg="#ffffff", bg="#777777", bd=4, relief=GROOVE)

enter_input_frame = LabelFrame(main_window, text="enter input frame", font=("Verdana", 16), fg="#ffffff", bg="#777777", bd=2, relief=RAISED)
enter_input = Entry(enter_input_frame, font=("Verdana", 16), fg="#ffffff", bg="#777777", bd=4, relief=GROOVE)
enter_input.place(x=0, y=0)
print_button = Button(text="print text", font=("Verdana", 16), fg="#ffffff", bg="#777777", bd=4, relief=GROOVE,
        command=print_text)
print_text_output = Label(font=("Verdana", 16), fg="#ffffff", bg="#777777", bd=4, relief=GROOVE)

#buttonframe.place(x=0, y=0)
enter_input_frame.place(x=0, y=0, width=400, height=90)
print_button.place(x=0, y=90, width=400, height=90)
print_text_output.place(x=0, y=180, width=400, height=90)

main_window.mainloop()
