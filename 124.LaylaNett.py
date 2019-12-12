import turtle as trtl
import random
# maze turtle set up
maze = trtl.Turtle()
maze.pensize(5)
maze.ht()
maze.speed(0)

#maze set up
amount = 20
maze_wall = 25
maze_door = 30
maze.color("green")
barrier= 20

#basic maze wall
for i in range(25):
    if i > 4 and i < 22:
        door = random.randint(2*maze_wall, amount - 2*maze_wall)
        barrier = random.randint(2*maze_wall, amount - 2*maze_wall)

        if door < barrier:
            maze.forward(door)

            #door thingy
            maze.penup()
            maze.forward(maze_door)
            maze.pendown()

            maze.forward(barrier - door - maze_door)

            #barrier thingy
            maze.left(90)
            maze.forward(maze_wall*2)
            maze.back(maze_wall*2)
            maze.right(90)

            maze.forward(amount - barrier)

        else:
            maze.forward(barrier)

            #barrier thingy part 2
            maze.left(90)
            maze.forward(maze_wall*2)
            maze.back(maze_wall*2)
            maze.right(90)

            maze.forward(door - barrier)

            #door thingy part 2
            maze.penup()
            maze.forward(maze_door)
            maze.pendown()

            maze.forward(amount - door - maze_door)

        
    maze.left(90)
    amount += maze_wall

#player turtle set up

player = trtl.Turtle()
player.pensize(5)
player.shape("turtle")
player.pencolor("blue")

#player movement

def up():
    player.setheading(90)
    player.forward(10)
  

def down():
    player.setheading(270)
    player.forward(10)
  

def right():
    player.setheading(0)
    player.forward(10)
  

def left():
    player.setheading(180)
    player.forward(10)
   

wn = trtl.Screen()
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")
wn.listen()
wn.mainloop()