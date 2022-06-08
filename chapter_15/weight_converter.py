from tkinter import *
import sys


def main():
    main_window = Tk()


    WIDTH = 860
    HEIGHT = 700
    FONT = ("Verdana", 16)
    FG_COLOUR="#000011"
    BG_COLOUR="#eeeeff"

    main_window.geometry(f"{WIDTH}x{HEIGHT}")

    # command functions
    def convert_to_pounds():
        """convert kilograms to pounds"""
        
        weight_kg = float(weight_kg_input.get())
        weight_in_pounds = weight_kg / 2.204
        display_weight_lbs.configure(text = "{:1.2f} kilograms is {:1.2f} pounds".format(weight_kg, weight_in_pounds))
        #weight_kg_input.delete(0, END)

    def convert_to_kilograms():
        """convert pounds to kilograms"""

        weight_lbs = float(weight_lbs_input.get())
        weight_in_kilograms = weight_lbs * 2.204
        display_weight_kg.configure(text = "{:1.2f} pounds is {:1.2f} kilograms".format(weight_lbs, weight_in_kilograms))
        #weight_lbs_input.delete(0, END)

    def clear_left_cmd():
        """clear left input/output fields"""

        weight_kg_input.delete(0, END)
        display_weight_lbs.configure(text = "")

    def clear_right_cmd():
        """clear right input/output fields"""
        
        weight_lbs_input.delete(0, END)
        display_weight_kg.configure(text = "")

    def clear_all_cmd():
        """clear all input/output fields"""

        weight_kg_input.delete(0, END)
        weight_lbs_input.delete(0, END)
        display_weight_lbs.configure(text = "")
        display_weight_kg.configure(text = "")

    def close_cmd():
        sys.exit()

    def toggle_title():
        pass

    def title_show():
        """show frame title"""

        display_title_frame.configure(text="weight converter")
        display_weight_lbs_frame.configure(text="display weight lbs")
        display_weight_kg_frame.configure(text="display weight kg")

        get_weight_kg_frame.configure(text="get weight kg")
        weight_kg_input_frame.configure(text="input weight kg")

        get_weight_lbs_frame.configure(text="get weight lbs")
        weight_lbs_input_frame.configure(text="input weight lbs")

        weight_lbs_button_frame.configure(text="convert weight to pounds")
        weight_kg_button_frame.configure(text="convert weight to kilograms")

        clear_left_button_frame.configure(text="clear")
        clear_right_button_frame.configure(text="clear")
        clear_all_button_frame.configure(text="clear all")

    def title_hide():
        """hide frame title"""

        display_title_frame.configure(text="")
        display_weight_lbs_frame.configure(text="")
        display_weight_kg_frame.configure(text="")

        get_weight_kg_frame.configure(text="")
        weight_kg_input_frame.configure(text="")

        get_weight_lbs_frame.configure(text="")
        weight_lbs_input_frame.configure(text="")

        weight_lbs_button_frame.configure(text="")
        weight_kg_button_frame.configure(text="")

        clear_left_button_frame.configure(text="")
        clear_right_button_frame.configure(text="")
        clear_all_button_frame.configure(text="")

    def change_bg_colour(colour):
        """change bg colour"""
        
        BG_COLOUR=colour
        display_title.configure(bg=BG_COLOUR)
        display_weight_lbs.configure(bg=BG_COLOUR)
        display_weight_kg.configure(bg=BG_COLOUR)

        get_weight_kg.configure(bg=BG_COLOUR)
        weight_kg_input.configure(bg=BG_COLOUR)

        get_weight_lbs.configure(bg=BG_COLOUR)
        weight_lbs_input.configure(bg=BG_COLOUR)

        weight_lbs_button.configure(bg=BG_COLOUR)
        weight_kg_button.configure(bg=BG_COLOUR)

        clear_left_button.configure(bg=BG_COLOUR)
        clear_right_button.configure(bg=BG_COLOUR)
        clear_all_button.configure(bg=BG_COLOUR)

    def change_bd_bg_colour(colour):
        """change bg colour"""
        
        BG_COLOUR=colour
        display_title_frame.configure(bg=BG_COLOUR)
        display_weight_lbs_frame.configure(bg=BG_COLOUR)
        display_weight_kg_frame.configure(bg=BG_COLOUR)

        get_weight_kg_frame.configure(bg=BG_COLOUR)
        weight_kg_input_frame.configure(bg=BG_COLOUR)

        get_weight_lbs_frame.configure(bg=BG_COLOUR)
        weight_lbs_input_frame.configure(bg=BG_COLOUR)

        weight_lbs_button_frame.configure(bg=BG_COLOUR)
        weight_kg_button_frame.configure(bg=BG_COLOUR)

        clear_left_button_frame.configure(bg=BG_COLOUR)
        clear_right_button_frame.configure(bg=BG_COLOUR)
        clear_all_button_frame.configure(bg=BG_COLOUR)

    def change_fg_colour(colour):
        """change fg colour"""

        FG_COLOUR=colour
        display_title.configure(fg=FG_COLOUR)
        display_weight_lbs.configure(fg=FG_COLOUR)
        display_weight_kg.configure(fg=FG_COLOUR)

        get_weight_kg.configure(fg=FG_COLOUR)
        weight_kg_input.configure(fg=FG_COLOUR)

        get_weight_lbs.configure(fg=FG_COLOUR)
        weight_lbs_input.configure(fg=FG_COLOUR)

        weight_lbs_button.configure(fg=FG_COLOUR)
        weight_kg_button.configure(fg=FG_COLOUR)

        clear_left_button.configure(fg=FG_COLOUR)
        clear_right_button.configure(fg=FG_COLOUR)
        clear_all_button.configure(fg=FG_COLOUR)

    def change_bd_fg_colour(colour):
        """change fg colour"""

        FG_COLOUR=colour
        display_title_frame.configure(fg=FG_COLOUR)
        display_weight_lbs_frame.configure(fg=FG_COLOUR)
        display_weight_kg_frame.configure(fg=FG_COLOUR)

        get_weight_kg_frame.configure(fg=FG_COLOUR)
        weight_kg_input_frame.configure(fg=FG_COLOUR)

        get_weight_lbs_frame.configure(fg=FG_COLOUR)
        weight_lbs_input_frame.configure(fg=FG_COLOUR)

        weight_lbs_button_frame.configure(fg=FG_COLOUR)
        weight_kg_button_frame.configure(fg=FG_COLOUR)

        clear_left_button_frame.configure(fg=FG_COLOUR)
        clear_right_button_frame.configure(fg=FG_COLOUR)
        clear_all_button_frame.configure(fg=FG_COLOUR)


    def colour_matte_black():
        
        change_bg_colour("#000000")
        change_fg_colour("#cccccc")
        
        change_bd_bg_colour("#000000")
        change_bd_fg_colour("#cccccc")


    def colour_coal_black():
        
        change_bg_colour("#111111")
        change_fg_colour("#cccccc")
        
        change_bd_bg_colour("#000000")
        change_bd_fg_colour("#cccccc")


    def colour_white():
        
        change_bg_colour("#ffffff")
        change_fg_colour("#000000")
        
        change_bd_bg_colour("#ffffff")
        change_bd_fg_colour("#000000")


    def colour_pearl_white():
        
        change_bg_colour("#eeeeee")
        change_fg_colour("#000000")
        
        change_bd_bg_colour("#ffffff")
        change_bd_fg_colour("#000000")


    def colour_evergreen_white():
        
        change_bg_colour("#ddeedd")
        change_fg_colour("#444444")
        
        change_bd_bg_colour("#eeffee")
        change_bd_fg_colour("#444444")


    def colour_red():
        
        change_bg_colour("#ee0000")
        change_fg_colour("#000000")
        
        change_bd_bg_colour("#ff0000")
        change_bd_fg_colour("#000000")


    def colour_deep_red():
        
        change_bg_colour("#110000")
        change_fg_colour("#ffeeee")
        
        change_bd_bg_colour("#110000")
        change_bd_fg_colour("#ffeeee")


    def colour_pink_rose():
        
        change_bg_colour("#ff2222")
        change_fg_colour("#eeffee")
        
        change_bd_bg_colour("#ff2222")
        change_bd_fg_colour("#eeffee")


    def colour_orange():
        
        change_bg_colour("#ee7700")
        change_fg_colour("#eeffee")
        
        change_bd_bg_colour("#ee7700")
        change_bd_fg_colour("#eeffee")


    def colour_yellow():
        
        change_bg_colour("#ffff00")
        change_fg_colour("#000000")
        
        change_bd_bg_colour("#ffff00")
        change_bd_fg_colour("#000000")


    def colour_pitch_green():
        
        change_bg_colour("#007711")
        change_fg_colour("#ffffee")
        
        change_bd_bg_colour("#007711")
        change_bd_fg_colour("#ffffee")


    def colour_casper_blue():
        
        change_bg_colour("#0000ff")
        change_fg_colour("#ddddff")
        
        change_bd_bg_colour("#0000ff")
        change_bd_fg_colour("#ddddff")


    def colour_deep_blue():
        
        change_bg_colour("#000011")
        change_fg_colour("#ddddff")
        
        change_bd_bg_colour("#000011")
        change_bd_fg_colour("#ddddff")


    def colour_aurora_violet():
        
        change_bg_colour("#ff00ff")
        change_fg_colour("#ffddff")

        change_bd_bg_colour("#ff00ff")
        change_bd_fg_colour("#ffddff")


    def colour_default():
        
        change_bg_colour("#eeeeff")
        change_fg_colour("#000011")
        
        change_bd_bg_colour("#eeeeff")
        change_bd_fg_colour("#000011")


    def colour_rainbow():
        
        change_bg_colour("#eeeeff")
        display_title.configure(fg="#ff0000")
        display_weight_lbs.configure(fg="#ee7700")
        display_weight_kg.configure(fg="#ffff00")

        get_weight_kg.configure(fg="#00ff00")
        weight_kg_input.configure(fg="#0000ff")

        get_weight_lbs.configure(fg="#ff00ff")
        weight_lbs_input.configure(fg="#ff0000")

        weight_lbs_button.configure(fg="#ee7700")
        weight_kg_button.configure(fg="#ffff00")

        clear_left_button.configure(fg="#00ff00")
        clear_right_button.configure(fg="#0000ff")
        clear_all_button.configure(fg="#ff00ff")
        

        change_bd_bg_colour("#eeeeff")
        display_title_frame.configure(fg="#ff0000")
        display_weight_lbs_frame.configure(fg="#ee7700")
        display_weight_kg_frame.configure(fg="#ffff00")

        get_weight_kg_frame.configure(fg="#00ff00")
        weight_kg_input_frame.configure(fg="#0000ff")

        get_weight_lbs_frame.configure(fg="#ff00ff")
        weight_lbs_input_frame.configure(fg="#ff0000")

        weight_lbs_button_frame.configure(fg="#ee7700")
        weight_kg_button_frame.configure(fg="#ffff00")

        clear_left_button_frame.configure(fg="#00ff00")
        clear_right_button_frame.configure(fg="#0000ff")
        clear_all_button_frame.configure(fg="#ff00ff")


    def colour_rainbow_dark():
        
        change_bg_colour("#000000")
        display_title.configure(fg="#ff0000")
        display_weight_lbs.configure(fg="#ee7700")
        display_weight_kg.configure(fg="#ffff00")

        get_weight_kg.configure(fg="#00ff00")
        weight_kg_input.configure(fg="#0000ff")

        get_weight_lbs.configure(fg="#ff00ff")
        weight_lbs_input.configure(fg="#ff0000")

        weight_lbs_button.configure(fg="#ee7700")
        weight_kg_button.configure(fg="#ffff00")

        clear_left_button.configure(fg="#00ff00")
        clear_right_button.configure(fg="#0000ff")
        clear_all_button.configure(fg="#ff00ff")
        
        
        change_bd_bg_colour("#000000")
        display_title_frame.configure(fg="#ff0000")
        display_weight_lbs_frame.configure(fg="#ee7700")
        display_weight_kg_frame.configure(fg="#ffff00")

        get_weight_kg_frame.configure(fg="#00ff00")
        weight_kg_input_frame.configure(fg="#0000ff")

        get_weight_lbs_frame.configure(fg="#ff00ff")
        weight_lbs_input_frame.configure(fg="#ff0000")

        weight_lbs_button_frame.configure(fg="#ee7700")
        weight_kg_button_frame.configure(fg="#ffff00")

        clear_left_button_frame.configure(fg="#00ff00")
        clear_right_button_frame.configure(fg="#0000ff")
        clear_all_button_frame.configure(fg="#ff00ff")


    # create widget frame
    display_title_frame = LabelFrame(main_window, text="weight converter", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)
    display_weight_lbs_frame = LabelFrame(main_window, text="display weight lbs", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)
    display_weight_kg_frame = LabelFrame(main_window, text="display weight kg", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)

    get_weight_kg_frame = LabelFrame(main_window, text="get weight kg", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)
    weight_kg_input_frame = LabelFrame(main_window, text="input weight kg", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)

    get_weight_lbs_frame = LabelFrame(main_window, text="get weight lbs", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)
    weight_lbs_input_frame = LabelFrame(main_window, text="input weight lbs", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)

    weight_lbs_button_frame = LabelFrame(main_window, text="convert weight to pounds", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)
    weight_kg_button_frame = LabelFrame(main_window, text="convert weight to kilograms", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE) 

    clear_left_button_frame = LabelFrame(main_window, text="clear", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)
    clear_right_button_frame = LabelFrame(main_window, text="clear", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)
    clear_all_button_frame = LabelFrame(main_window, text="clear all", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=4, relief=GROOVE)


    # create widgets
    display_title = Label(display_title_frame, text = "weight converter", font=("Verdana", 16, "bold"), fg=FG_COLOUR, bg=BG_COLOUR)
    display_title.pack(fill=BOTH, padx=30, pady=7)
    display_weight_lbs = Label(display_weight_lbs_frame, font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    display_weight_lbs.pack(fill=BOTH, padx=30, pady=7)
    display_weight_kg = Label(display_weight_kg_frame, font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    display_weight_kg.pack(fill=BOTH, padx=30, pady=7)

    get_weight_kg = Label(get_weight_kg_frame, text = "weight in kilograms(kg): ", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    get_weight_kg.pack(fill=BOTH, padx=30, pady=7)
    weight_kg_input = Entry(weight_kg_input_frame, font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    weight_kg_input.pack(fill=BOTH, padx=30, pady=7)
    get_weight_lbs = Label(get_weight_lbs_frame, text = "weight in pounds(lbs): ", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    get_weight_lbs.pack(fill=BOTH, padx=30, pady=7)
    weight_lbs_input = Entry(weight_lbs_input_frame, font=FONT, fg=FG_COLOUR, bg=BG_COLOUR)
    weight_lbs_input.pack(fill=BOTH, padx=30, pady=7)

    weight_lbs_button = Button(weight_lbs_button_frame, text = "[ convert weight to pounds ]", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=5, relief=RAISED,
            command=convert_to_pounds)
    weight_lbs_button.pack(fill=BOTH, padx=30, pady=7)
    weight_kg_button = Button(weight_kg_button_frame, text = "[ convert weight to kilograms ]", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=5, relief=RAISED,
            command=convert_to_kilograms)
    weight_kg_button.pack(fill=BOTH, padx=30, pady=7)

    clear_left_button = Button(clear_left_button_frame, text = "[ clear ]", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=5, relief=RAISED,
            command=clear_left_cmd)
    clear_left_button.pack(fill=BOTH, padx=30, pady=7)
    clear_right_button = Button(clear_right_button_frame, text = "[ clear ]", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=5, relief=RAISED,
            command=clear_right_cmd)
    clear_right_button.pack(fill=BOTH, padx=30, pady=7)
    clear_all_button = Button(clear_all_button_frame, text = "[ clear all ]", font=FONT, fg=FG_COLOUR, bg=BG_COLOUR, bd=5, relief=RAISED,
            command=clear_all_cmd)
    clear_all_button.pack(fill=BOTH, padx=30, pady=7)

    # place widgets
    y_pos = 100
    display_title_frame.place(x=0, y=0, width=WIDTH, height=y_pos)

    get_weight_kg_frame.place(x=0, y=y_pos, width=(WIDTH / 2), height=y_pos)
    weight_kg_input_frame.place(x=0, y=y_pos * 2, width=(WIDTH / 2), height=y_pos)
    weight_lbs_button_frame.place(x=0, y=y_pos * 3, width=(WIDTH / 2), height=y_pos)
    display_weight_lbs_frame.place(x=0, y=y_pos * 4, width=(WIDTH / 2), height=y_pos)
    clear_left_button_frame.place(x=0, y=y_pos * 5, width=(WIDTH / 2), height=y_pos)

    get_weight_lbs_frame.place(x=430, y=y_pos, width=(WIDTH / 2), height=y_pos)
    weight_lbs_input_frame.place(x=430, y=y_pos * 2, width=(WIDTH / 2), height=y_pos)
    weight_kg_button_frame.place(x=430, y=y_pos * 3, width=(WIDTH / 2), height=y_pos)
    display_weight_kg_frame.place(x=430, y=y_pos * 4, width=(WIDTH / 2), height=y_pos)
    clear_right_button_frame.place(x=430, y=y_pos * 5, width=(WIDTH / 2), height=y_pos)

    clear_all_button_frame.place(x=0, y=y_pos * 6, width=WIDTH, height=y_pos)
    
    # set menu
    top = Menu(main_window)
    file_menu = Menu(top)
    toggle_title = Menu(file_menu)
    toggle_title.add_command(label="Title Show", command=title_show)
    toggle_title.add_command(label="Title Hide", command=title_hide)
    file_menu.add_cascade(label="Toggle Title", menu=toggle_title)
    file_menu.add_separator()
    file_menu.add_command(label="Close", command=close_cmd)
    top.add_cascade(label="File", menu=file_menu)
    main_window.configure(menu=top)
    
    colourscheme = Menu(top)

    colours = [
            "Matte Black", "Coal Black", "White", "Pearl White", "Evergreen White", 
            "Red", "Deep Red", "Pink Rose", 
            "Orange", "Yellow", "Pitch Green", 
            "Casper Blue", "Deep Blue", "Aurora Violet", 
            "Default", "Rainbow", "Rainbow Dark"
            ]

    colours_cmd = [
            colour_matte_black, colour_coal_black, colour_white, colour_pearl_white, colour_evergreen_white, 
            colour_red, colour_deep_red, colour_pink_rose, 
            colour_orange, colour_yellow, colour_pitch_green, 
            colour_casper_blue, colour_deep_blue, colour_aurora_violet, 
            colour_default, colour_rainbow, colour_rainbow_dark
            ]

    count = 0
    for colour in colours:
        current_colour_cmd = colours_cmd[count]
        colourscheme.add_command(label=colour, command=current_colour_cmd)
        count += 1

    top.add_cascade(label="Colorscheme", menu=colourscheme)
    main_window.configure(menu=top)
    
    # bind hkey
    #main_window.bind('q', colour_matte_black)
    #main_window.update()

    main_window.mainloop()


if __name__ == '__main__':
    main()
