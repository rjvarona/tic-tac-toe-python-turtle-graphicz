from turtle import *
from tttlogic import *
import tkinter.messagebox

width(5)
hideturtle()

speed(0)
title('RJ Tic Tac Toe: Player X')

def getPos(x,y):
    print("(", x, "," ,y, ")")
    return 

def point_to_square (x, y):
    if -50 < x < 50 and 0 < y < 100:
        position = "Center"
    elif -150 < x < -50 and 0 < y < 100:
        position = "West"
    elif 50 < x < 150 and 0 < y < 100:
        position = "East"
    elif 50 < x < 150 and 100 < y < 200:
        position = "NorthEast"
    elif -50 < x < 50  and 100 < y < 200:
        position = "North"
    elif -150 < x < -50 and 100 < y < 200:
        position = "NorthWest"
    elif -150 < x < -50 and -100 < y < 0:
        position = "SouthWest"
    elif -50 < x < 50 and -100 < y < 0:
        position = "South"
    elif 50 < x < 150 and -100 < y < 0:
        position = "SouthEast"
    elif x < -150 or x > 150 or y > 200 or y < -100:
        position = " "
    print(position)
    return position


def square_to_point(x, y):
    position = point_to_square(x, y)
    #print("calling sqare_to_point")
    if position == "Center":
        x = 50
        y = 50
        print("(", x, "," ,y, ")")
    elif position == "West":
        x = -50
        y = 50
        print("(", x, "," ,y, ")")
    elif position == "East":
        x = 150
        y = 50
        print("(", x, "," ,y, ")")
    elif position == "NorthEast":
        x = 150
        y = 150
        print("(", x, "," ,y, ")")
    elif position == "North":
        x = 50 
        y = 150
        print("(", x, "," ,y, ")")
    elif position == "NorthWest":
        x = -50
        y = 150
        print("(", x, "," ,y, ")")
    elif position == "SouthWest":
        x = -50
        y = -50
        print("(", x, "," ,y, ")")
    elif position == "South":
        x = 50
        y = -50
        print("(", x, "," ,y, ")")
    elif position == "SouthEast":
        x = 150
        y = -50
        print("(", x, "," ,y, ")")
    elif position == " ":
        x = -1000
        y = -1000
    
    return (x, y)

def hit():
    onscreenclick(square_to_point) 

hit()  


    


def board():
    setposition(-150,0)
    forward(300)
    penup()
    left(90)
    forward(100)
    pendown()
    left(90)
    forward(300)
    backward(100)
    right(90)
    forward(100)
    backward(300)
    right(90)
    penup()
    forward(100)
    pendown()
    left(90)
    forward(300)
#board()



def drawO(x,y):
    tracer(0)
    x,y = square_to_point(x, y)
    if (x,y) == (-1000,-1000):
        pass
    else:
        penup()
        setposition(x, y)
        pendown()
        color('red')
        circle(50)
        update()
        #changeplayer()
        
    


    
def drawX (x,y):
    tracer(0)
    x,y = square_to_point(x, y)
    if (x,y) == (-1000,-1000):
            pass
    else:
        penup()
        setposition(x - 85,y - 35)
        pendown()
        color('blue')
        right(45)
        forward(100)
        penup()
        left(135)
        forward(70)
        pendown()
        left(135)
        forward(100)
        right (135)
        penup()
        forward(70)
        pendown
        right(90)
        update()
        #changeplayer()
        


canvas = getcanvas()    
canvas.config(cursor="X_Cursor")

def askagain():
    if current_player() == 'X':
        answer = tkinter.messagebox.askquestion ("Tic Tac Toe O wins", "Do you want to play again?")
    elif current_player() == 'O':
        answer =  tkinter.messagebox.askquestion ("Tic Tac Toe X wins", "Do you want to play again?")
    if answer == 'yes':
        main()
    elif answer =='no':
        bye()       
    

def mouseclick(x, y): 
    square = point_to_square(x, y)
    if current_player() == 'X' and move(square) == True:
        canvas.config(cursor="Circle")
        title("Tic Tac Toe: turn O")        
        #x,y = drawX(x,y)  
        drawX(x,y)
        
    
    elif current_player() == "O" and move(square) == True:
        canvas.config(cursor="X_Cursor")
        title("Tic Tac Toe: turn X")        
        #x,y = drawO(x,y)
        drawO(x,y)
    player,status = check_status()
    if status == "Win_NW_NE":
        pencolor("black")
        width(10)        
        penup()
        right(90)
        setposition (-150, 150)
        pendown()
        forward (300)
        update()
        askagain()
        
    elif status == "Win_W_E":
        pencolor("black")
        width(10)        
        penup()
        setposition(-150, 50)
        pendown()
        right(90)
        forward (300)
        update()
        askagain()        
    elif status == "Win_SW_SE":
        pencolor("black")
        width(10)        
        penup()
        setposition(-150, -50)
        pendown()
        right(90)
        forward (300)
        update()
        askagain()        
    elif status == "Win_NW_SW":
        pencolor("black")
        width(10)        
        penup()
        setposition(-100, -100)
        pendown()
        forward (300)
        update()
        askagain()
    elif status == "Win_N_S":
        pencolor("black")
        width(10)        
        penup()
        setposition(0, -100)
        pendown()
        forward (300)
        update()
        askagain()
    elif status == "Win_NE_SE":
        pencolor("black")
        width(10)        
        penup()
        setposition(100, -100)
        pendown()
        forward (300) 
        update()
        askagain()
    elif status == "Win_NW_SE":
        pencolor("black")
        width(10)        
        penup()
        setposition(-150, 200)
        right(135)
        pendown()
        forward (400)
        update()
        askagain()
    elif status == "Win_NE_SW":
        pencolor("black")
        width(10)        
        penup()
        setposition(150, 200)
        left(135)
        pendown()
        forward (400)
        update()
        askagain()

    
def main():
    reset()
    canvas.config(cursor="X_Cursor")
    speed(0)
    width(5)
    hideturtle()
    tracer(0)
    initialize_board()
    set_player('X')
    board()
    onscreenclick(mouseclick)
    update()
    listen()           
    mainloop()    
    
    
if __name__ == '__main__': 
    reset()
    canvas.config(cursor="X_Cursor")
    speed(0)
    width(5)
    hideturtle()
    tracer(0)
    initialize_board()
    set_player('X')
    board()
    onscreenclick(mouseclick)
    update()
    listen()           
    mainloop()