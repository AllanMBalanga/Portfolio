import turtle
import pandas

screen = turtle.Screen()
screen.title("PH Map")
image = "Ph_administrative_map_blank.gif"
screen.addshape(image)
turtle.shape(image)

guessed_region = []

data = pandas.read_csv("regions.csv")
data_list = data.regions.to_list()

while len(guessed_region) < 16:
    user_region = screen.textinput(title=f"{len(guessed_region)}/16 Correct Regions", prompt="Guess the region: ").upper()

    if user_region == "EXIT":
        missing_region = [region for region in data_list if region not in guessed_region]
        new_data = pandas.DataFrame(missing_region)
        new_data.to_csv("new_data.csv")
        break

    if user_region in data_list:
        guessed_region.append(user_region)
        region = turtle.Turtle()
        region.hideturtle()
        region.penup()
        region_row = data[data.regions == user_region]
        region.goto(region_row.x.item(),region_row.y.item())
        region.write(user_region)


