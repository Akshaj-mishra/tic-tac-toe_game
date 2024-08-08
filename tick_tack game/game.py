import tkinter 

def set_title(row, coloumn):
    global current_playe,turn
    if turn == 9:
        return
    if (game_over):
        return
    if board[row][coloumn]["text"] != "":
        return
    board[row][coloumn]["text"] = current_playe
    
    if current_playe == playero:
        current_playe = playerx
    else:
        current_playe = playero
    lable["text"] = current_playe +"'s Turn"
    check_winner()

def check_winner():
    global turn, game_over
    turn += 1
    # check horizontal
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"]==board[row][2]["text"] and board[row][0]["text"] != ""):
            lable.config(text=board[row][0]["text"] + " is the winner", foreground= color_yellow)
            for i in range(3):
                board[row][i].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    # check vertical 
    for col in range(3):
        if (board[0][col]["text"] == board[1][col]["text"]==board[2][col]["text"] and board[0][col]["text"] != ""):
            lable.config(text=board[0][col]["text"] + " is the winner", foreground= color_yellow)
            for i in range(3):
                board[i][col].config(foreground=color_yellow, background=color_light_gray)
            game_over = True
            return
    # digonal check 
    if (board[0][0]["text"] == board[1][1]["text"]==board[2][2]["text"] and board[0][0]["text"] != ""):
        lable.config(text=board[0][1]["text"] + " is the winner", foreground= color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    if (board[0][2]["text"] == board[1][1]["text"]==board[2][0]["text"] and board[0][2]["text"] != ""):
        lable.config(text=board[0][2]["text"] + " is the winner", foreground= color_yellow)
        for i in range(3):
            board[i][2-i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    #if it is draw 
    if turn == 9 and not game_over:
        lable.config(text="It's a draw!", foreground= color_yellow)
        game_over = True
        return


def new_game():
    global game_over, turn, current_player
    for i in range(3):
        for j in range(3):
            board[i][j].config(text="", state=tkinter.NORMAL, foreground= color_blue, background = color_gray)
    current_player = playerx
    lable.config(text= current_playe + "'s turn ", foreground= "white")
    turn = 0
    game_over = False
        

#game setup
playerx = "X"
playero =  "O"
current_playe = playerx 
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turn = 0
game_over = False


#creating window
window = tkinter.Tk()
window.title("TICK TAC TOE")
window.resizable(False,False)

frame = tkinter.Frame(window)
lable = tkinter.Label(frame, text = current_playe +"'s Turn",font= ("Consolas",20), background= color_gray , foreground= "white")

lable.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range (3):
    for coloumn in range (3):
        board[row][coloumn] = tkinter.Button(frame, text="",font=("consolas",50,"bold"), background=color_gray,foreground=color_blue,width=4,height=1,
                                            command= lambda row= row, coloumn = coloumn : set_title(row,coloumn))
        board[row][coloumn].grid(row = row+1, column= coloumn)
Button = tkinter.Button(frame,text="Restart",font=("Consolas",20),background=color_gray,foreground="white", command= new_game)
Button.grid(row = 4,column=0,columnspan=3,sticky="we")

frame.pack()


window.mainloop()