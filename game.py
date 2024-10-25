import turtle
import winsound 



game=turtle.Screen()
game.setup(1000,600)
game.bgcolor("green")
game.title("Pong Game")
game.tracer(0)
score_a=0
score_b=0


#left pad
left=turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("yellow")
left.shapesize(stretch_wid=5,stretch_len=1)
left.penup()
left.goto(-490,0)

#right pad
right=turtle.Turtle()
right.speed(0)
right.shape("square")
right.color("yellow")
right.shapesize(stretch_wid=5,stretch_len=1)
right.penup()
right.goto(480,0)

#ball
ball=turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.dx=0.5
ball.dy=0.5

#score
pen=turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("red")
pen.goto(0,260)
pen.hideturtle()
pen.write("Player A: 0   ,  Player B: 0" , align="center",font=("Ariella",24,"normal"))

#instruction
user_left=turtle.Turtle()
user_left.penup()
user_left.speed(0)
user_left.color("yellow")
user_left.goto(-450,180)
user_left.hideturtle()
user_left.write("Key : w(for up)\n       z(for down) ", font=("Ariella",13,"normal"))


#insruction
user_right=turtle.Turtle()
user_right.penup()
user_right.speed(0)
user_right.color("yellow")
user_right.hideturtle()
user_right.goto(270,180)
user_right.write("Key : Up arrow(for up)\n        Down arrow(for down) " , font=("Ariella",13,"normal"))


#moving left and right pad
def left_up():
    left.sety(left.ycor()+20)
def left_down():
    left.sety(left.ycor()-20)
def right_up():
    right.sety(right.ycor()+20)
def right_down():
    right.sety(right.ycor()-20)


game.listen()
game.onkeypress(left_up,"w")
game.onkeypress(left_down,"z")
game.onkeypress(right_up,"Up")
game.onkeypress(right_down,"Down")

while True:
    game.update()
    
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    
    #ball collision condition
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    
    if ball.ycor()<-285:
        ball.sety(-285)
        ball.dy*=-1

    if ball.xcor()>480:
        ball.setx(480)
        ball.dx*=-1
        pen.clear()
        score_a+=1
        pen.write("Player A: {}   ,  Player B: {}".format(score_a,score_b), align="center",font=("Ariella",24,"normal"))


    if ball.xcor()<-475:
        ball.setx(-475)
        ball.dx*=-1
        pen.clear()
        score_b+=1
        pen.write("Player A: {}   ,  Player B: {}".format(score_a,score_b) ,align="center",font=("Ariella",24,"normal"))

    #pad collision condition
    if ball.xcor()>470 and ball.ycor()<right.ycor()+50 and ball.ycor()>right.ycor()-50:
        ball.setx(470)
        ball.dx*=-1
        freq = 500		 
        dur = 100			
        winsound.Beep(freq, dur)

    if ball.xcor()<-470 and ball.ycor()<left.ycor()+50 and ball.ycor()>left.ycor()-50:
        ball.setx(-470)
        ball.dx*=-1
        freq = 500		 
        dur = 100			
        winsound.Beep(freq, dur)




    
    
    

