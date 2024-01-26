from turtle import Turtle, Screen
import time
import random
screen = Screen()


#promenne
score = 0
highest_score = 0

screen.bgcolor("light green")
screen.title("Vitejte ve Snake game")
screen.setup(width= 600, height= 600)
screen.tracer(0)

#hadi hlava, jablko a skore
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 265)
score_sign.write("Skore: 0 Nejvyssi skore: 0 ",align= "center", font=("Arial", 18))


body_parts = []



# funkce
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    
        

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"  

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"



#kliknuti na klavesy
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")


# hlavni cyklus
while True:
    screen.update()

    #kontrola kolize s hranou obrazovky
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < - 290:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        #skryti casti tela
        for one_body_part in body_parts:
            one_body_part.goto(800, 800)

        #vyprazdnime list s castmi tela(sede ctverecky)
        body_parts.clear()

        #resetovani score
        score = 0
        score_sign.clear()
        score_sign.write(f"Skore: {score} Nejvyssi skore: {highest_score} ",align= "center", font=("Arial", 18))

    # kolize hlavy s jablkem - had sni jablko
    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)

        #pridani casti tela
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)



        # zvyseni skore
        score += 10
        if score > highest_score:
            highest_score = score

        score_sign.clear()
        score_sign.write(f"Skore: {score} Nejvyssi skore: {highest_score} ",align= "center", font=("Arial", 18))

    # presun tela hada
    for index in range(len(body_parts)-1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)



    # Nastavi smer prvni casti tela na smer hlavy
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)

    move()


    #hlava narazila do tela
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            #skryti casti tela
            for one_body_part in body_parts:
                one_body_part.goto(800, 800)

            #vyprazdneni listu s castmi tela(sede ctverecky)
            body_parts.clear()
            
            #resetovani score
            score = 0
            score_sign.clear()
            score_sign.write(f"Skore: {score} Nejvyssi skore: {highest_score} ",align= "center", font=("Arial", 18))

    time.sleep(0.1)





screen.exitonclick()