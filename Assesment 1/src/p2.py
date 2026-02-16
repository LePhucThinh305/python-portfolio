# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021A
# Assignment: 1
# Author: Le Phuc Thinh (s3893964)
# Created date: 12/4/2021
# Last modified date: 18/4/2021

def draw_bar_chart(house_id, food_qty, milk_qty, almond_milk_qty, tm_milk_qty, toilet_paper_qty):
    import turtle  # importing turle

    # Creating turtle tom and moving it to the top middle of the turtle window to write the house id
    win = turtle.Screen()
    win.bgcolor('white')
    tom = turtle.Turtle()
    tom.up()
    tom.goto(0.0, 370.0)
    tom.down()
    tom.write('house id:' + str(house_id), False, align='center', font=("Arial", 13, "normal"))
    # Telling tom to go to the bottom left of the turtle window and drawing the x axis
    # The x-axis is 550 pixel long and each bar is 100 pixel wide
    tom.up()
    tom.goto(-750, -370)
    tom.down()
    tom.forward(550)
    tom.goto(-750, -370)
    tom.left(90)
    # Finding the maximum y value out of the 5 bar and making the why axis 10 pixel longer than the max_y value
    max_y = 0
    if food_qty > max_y:
        max_y = food_qty
    if milk_qty > max_y:
        max_y = milk_qty
    if almond_milk_qty > max_y:
        max_y = almond_milk_qty
    if tm_milk_qty > max_y:
        max_y = tm_milk_qty
    if toilet_paper_qty > max_y:
        max_y = toilet_paper_qty
    tom.forward(max_y + 10)
    tom.goto(-750, -370)
    # Drawing the bars
    for qty in [food_qty, milk_qty, almond_milk_qty, tm_milk_qty, toilet_paper_qty]:
        tom.forward(qty)
        tom.right(90)
        tom.forward(100)
        tom.right(90)
        tom.forward(qty)
        tom.left(180)
    # Labeling at the bottom of each bar
    tom.up()
    tom.goto(-750, -390)
    tom.down()
    tom.write('food quantity:' + str(food_qty))

    tom.up()
    tom.goto(-650, -390)
    tom.down()
    tom.write('milk_qty:' + str(milk_qty))

    tom.up()
    tom.goto(-550, -390)
    tom.down()
    tom.write('almond_milk_qty:' + str(almond_milk_qty))

    tom.up()
    tom.goto(-450, -390)
    tom.down()
    tom.write('tm_milk_qty:' + str(tm_milk_qty))

    tom.up()
    tom.goto(-350, -390)
    tom.down()
    tom.write('toilet_paper_qty:' + str(toilet_paper_qty))

    win.exitonclick()
