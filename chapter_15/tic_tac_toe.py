from tkinter import *

main_window = Tk()


# functions
def callback(r, c):
    """place player"""
    
    global player
    if player == "X" and grid_state[r][c] == 0 and stop_game == False:
        grid[r][c].configure(text="X")
        grid_state[r][c] = "X"
        player = "O"
    elif player == "O" and grid_state[r][c] == 0 and stop_game == False:
        grid[r][c].configure(text="O")
        grid_state[r][c] = "O"
        player = "X"

    check_for_winner()

def reset_cmd():
    """reset grid"""
    #mod lam

    for x in range(3):
        for y in range(3):
            print(grid[x][y])
            grid[x][y] = grid[x][y].configure(text="", bg="yellow")
            grid_state[x][y] = 0

def check_for_winner():
    """checks for winner"""

    for i in range(3):
        if grid_state[i][0] == grid_state[i][1] == grid_state[i][2] != 0:
            grid[i][0].configure(bg="grey")
            grid[i][1].configure(bg="grey")
            grid[i][2].configure(bg="grey")
            stop_game = True

    for i in range(3):
        if grid_state[0][i] == grid_state[1][i] == grid_state[2][i] != 0:
            grid[0][i].configure(bg="grey")
            grid[1][i].configure(bg="grey")
            grid[2][i].configure(bg="grey")
            stop_game = True
    
    if grid_state[0][0] == grid_state[1][1] == grid_state[2][2] != 0:
        grid[0][0].configure(bg="grey")
        grid[1][1].configure(bg="grey")
        grid[2][2].configure(bg="grey")
        stop_game = True

    if grid_state[2][0] == grid_state[1][1] == grid_state[0][2] != 0:
        grid[2][0].configure(bg="grey")
        grid[1][1].configure(bg="grey")
        grid[0][2].configure(bg="grey")
        stop_game = True

# set grid
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

#set grid state
grid_state = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

# init player
player = "X"
stop_game = False

# create and place items
for i in range(3):
    for j in range(3):
        grid[i][j] = Button(font=("Verdana", 56), width=3, bg="yellow",
                command=lambda r=i, c=j: callback(r, c))
        grid[i][j].grid(row=i, column=j)

reset_button = Button(text="reset", font=("Verdana", 56), bg="yellow",
        command=reset_cmd)
reset_button.grid(row=3, column=0, columnspan=2)

main_window.mainloop()
