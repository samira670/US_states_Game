import turtle
import pandas


screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("US_STATE_GAME")
turtle.shape(image)


game_is_on = True
score = 0

while game_is_on == True:

    input= screen.textinput(title=f"your score= {score}", prompt="What's the state name?")
    #The first letter of input is bacome upper case like our data in 50_states.csv
    input_u = input.title()

    # Reading CSV
    data = pandas.read_csv("50_states.csv")

    #Get the coloumn of state from data
    states = data.state

    #Converting our serieto a list
    list = states.to_list()


    #Loop through our list to check whether our answer is correct or not & and remove the answers that are correct from our list to prevent repetition
    for stat in list:

        if  stat == input_u:
            # if our answer is correct we add our score
            score+=1

            #using tutle to write our state in the image(map)
            timmy = turtle.Turtle()
            timmy.penup()
            timmy.hideturtle()

            #Finding the x and y position
            row = data[data.state == stat]
            x_position = row.x
            y_position = row.y
            timmy.goto(int(x_position), int(y_position))
            timmy.write(stat)
            list.remove(stat)
        else:
            pass
        if list == []:

                game_is_on == False
                print("you finish the game")




screen.exitonclick()