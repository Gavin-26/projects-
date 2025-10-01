import turtle
import random
import time


screen = turtle.Screen()
screen.bgcolor("midnight blue")
screen.setup(width=800, height=600)


def draw_star(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()


def draw_snowflake(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    for _ in range(6):  
        turtle.forward(size)
        turtle.backward(size)
        turtle.right(60)


def draw_tree():
    tree_width = 200
    tree_height = 75
    start_y = -150

   
    for i in range(3):
        turtle.penup()
        turtle.goto(-tree_width // 2 + i * 25, start_y + i * tree_height)
        turtle.pendown()
        turtle.color("forest green")
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(tree_width - i * 50)
            turtle.left(120)
        turtle.end_fill()

   
    turtle.penup()
    turtle.goto(-25, -250)  
    turtle.pendown()
    turtle.color("brown")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)  
        turtle.left(90)
    turtle.end_fill()


def add_lights(light_positions):
    
    colors = ["red", "blue", "yellow", "orange"]
    
   
    for x, y in light_positions:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
       
        turtle.dot(10, random.choice(colors))


def change_lights(light_positions):
    colors = ["red", "blue", "yellow", "orange","purple","cyan","light blue","white"]
    
    while True:  
        for x, y in light_positions:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
           
            turtle.dot(10, random.choice(colors))
        time.sleep(0.5)


def draw_snowman(x, y):
    turtle.penup()
    turtle.goto(x+20, y - 180)  
    turtle.pendown()
    turtle.color("white")
   
    turtle.begin_fill()
    turtle.circle(60)  
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x+20, y - 110)  
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)  
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x+20, y - 20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(40)  
    turtle.end_fill()

  
    turtle.penup()
    turtle.goto(x , y + 30)
    turtle.dot(8, "black")
    turtle.goto(x + 40, y + 30)
    turtle.dot(8, "black")
    turtle.goto(x + 20, y - 30)
    turtle.dot(8, "black")

    
    turtle.goto(x +20, y )
    turtle.color("orange")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(6, steps=3)
    turtle.end_fill()

   
    turtle.penup()
    turtle.goto(x -10 , y + 50)  
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(60) 
        turtle.left(90)
        turtle.forward(20)  
        turtle.left(90)
    turtle.end_fill()

   
    turtle.penup()
    turtle.goto(x - 15, y - 30)
    turtle.pendown()
    turtle.setheading(150)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(x + 50, y - 30)
    turtle.pendown()
    turtle.setheading(30)
    turtle.forward(50)

   
    turtle.penup()
    turtle.goto(x - 20, y - 30)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(80) 
    turtle.left(90)
    turtle.forward(20) 
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()

  
    turtle.penup()
    turtle.goto(x + 20, y - 20) 
    turtle.color("white")
    turtle.write("And a", align="center", font=("Sans Serif", 8, "bold"))
    
    turtle.penup()
    turtle.goto(x + 20, y - 30)
    turtle.color("gold")
    turtle.write("Happy New Year", align="center", font=("Sans Serif", 7, "bold"))


def draw_gift_box(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    turtle.color("gold")
    turtle.penup()
    turtle.goto(x + 20, y)
    turtle.pendown()
    turtle.goto(x + 20, y + 50)
    turtle.goto(x + 30, y + 50)
    turtle.goto(x + 30, y)
    turtle.goto(x + 20, y)
    turtle.penup()
    turtle.goto(x, y + 20)
    turtle.pendown()
    turtle.goto(x + 50, y + 20)


def draw_gifts():
    positions = [(-260, -250), (-180, -250), (-100, -250), (50, -250), (150, -250), (230, -250)]
    for x, y in positions:
        draw_gift_box(x, y)


def draw_background():
  
    snowflake_positions = [
        (-300, 250), (250, 200), (200, 100), (-150, 150), (100, 50),
        (-50, -150), (-250, -200), (300, -100), (-200, -50), (150, 0),
        (50, 150), (-100, 50), (-100, -200), (200, -100), (0, -50),
        (-300, 100), (50, -200), (-200, -150), (100, 200), (-50, -250),
        (250, -200), (150, 250), (100, 150), (-250, -100), (300, 250),
        (0, -100), (150, 100), (-200, 250), (250, 50), (200, -150)
    ]
    for x, y in snowflake_positions:
        draw_snowflake(x, y, random.randint(5, 15))

   
    star_positions = [
        (-300, 300), (250, 250), (200, 300), (-100, 300), (50, 250),
        (150, 280), (-200, 150), (-50, 180), (100, 100), (150, 150),
        (0, 100), (200, 50), (-250, 50), (300, 100), (-150, 100),
        (50, 0), (150, -50), (-200, -100), (250, -150), (100, -100),
        (0, 0), (50, 50), (-150, -50), (-200, 200), (100, 150),
        (0, 200), (-50, 100), (150, 200), (-50, -100), (200, -200)
    ]
    for x, y in star_positions:
        draw_star(x, y, 15, "yellow")


def draw_crescent_moon():
    turtle.penup()
    turtle.goto(250, 200) 
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(40) 
    turtle.end_fill()
    
    
    turtle.penup()
    turtle.goto(230, 200)  
    turtle.pendown()
    turtle.color("midnight blue") 
    turtle.begin_fill()
    turtle.circle(40)  
    turtle.end_fill()


def write_christmas_message():
   
    turtle.penup()
    turtle.goto(0, 250)
    turtle.color("red")
    turtle.write("Merry Christmas", align="center", font=("Arial", 36, "bold"))
    
    
    turtle.penup()
    turtle.goto(0, 200)
    turtle.color("gold")
    turtle.write("to everyone", align="center", font=("Brush Script MT", 24, "normal"))


def main():
    
    light_positions = [
        (0, 10), (-35, 10), (-20, 35), (0, 55), (35, 10),(20,35),  
        (-60, -68), (-50, -50), (-40, -30), (-30, -10), (0, -10), (30, -10), (40,-30),
        (50,-50), (60,-68),(-40,-68),(-20,-68), (0,-68),(20,-68),(40,-68),
        (-80, -140), (-70, -120), (-60, -100), (-50, -84), (-20, -84), (10, -84), (30, -84), (50, -84),
        (80, -140),(70, -120), (60, -100),(-60, -140),(-40, -140),(-20, -140),(0, -140),(20, -140),
        (40, -140),(60, -140), 
    ]
    
    turtle.speed(0)
    turtle.hideturtle()
    draw_background()
    draw_tree()
    draw_gifts()
    draw_snowman(150, 0)  
    draw_crescent_moon() 
    write_christmas_message()  
    add_lights(light_positions)  
    change_lights(light_positions)  
    turtle.done()

if __name__ == "__main__":
    main()
