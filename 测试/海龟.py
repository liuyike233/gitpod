import turtle
turtle.speed(10)

# 红色的旗面
def qimian(x, y, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(1, 5):
        if i % 2 == 0:
            turtle.forward(205)
        else:
            turtle.forward(285)
        turtle.left(90)
    turtle.end_fill()

# 黄色的五角星(大)
def wujiaoxing(x, y, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()

# 四个小五角星
def xiaowujiao(x, y, single):
    turtle.up()
    turtle.goto(x, y)
    turtle.left(single)
    turtle.down()
    turtle.color("yellow")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(12)
        turtle.right(144)
    turtle.end_fill()

qimian(-110, -90, "red")
wujiaoxing(-85, 55, "yellow")
xiaowujiao(-35, 80, 30)
xiaowujiao(-14, 55, 60)
xiaowujiao(-12, 28, 30)
xiaowujiao(-22, 10, 60)
turtle.up()
turtle.goto(-110,-90)
turtle.write("祖国爸爸70周年快乐", font=("Arial",18, "bold"))
turtle.hideturtle()
turtle.done()