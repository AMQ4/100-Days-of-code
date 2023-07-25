import turtle
import pandas

screen = turtle.Screen()
screen.bgpic("./palestine map/v1.png")
drawer = turtle.Turtle()
drawer.penup()
drawer.speed(3)

data = pandas.read_csv("./palestine map/states.csv")
no_states = len(data)
states = data["المحافظة"].to_list()
answered = 0
listed = []
ans = screen.textinput(f"Score {answered}/{no_states}", "Enter a state")
while ans is not None and len(listed) <= no_states:
    if ans in states:
        state = data[data["المحافظة"] == ans]
        drawer.goto(state["س"].iloc[0], state["ص"].iloc[0])
        drawer.write(state["المحافظة"].item()) # the same as iloc
        answered += 1
        listed.append(state["المحافظة"].iloc[0])
        states.remove(listed[-1])
        ans = screen.textinput(f"Score {answered}/{no_states}", "Enter a state")
    elif ans in listed:
        ans = screen.textinput(f"Score {answered}/{no_states}", f"{ans} is already mentioned, try again")
    else:
        ans = screen.textinput(f"Score {answered}/{no_states}", f"{ans} is not a Palestine state")
not_listed = set(states) - set(listed)

for s in not_listed:
    state = data[data["المحافظة"] == s]
    drawer.goto(state["س"].iloc[0], state["ص"].iloc[0])
    drawer.write(state["المحافظة"].item())

turtle.mainloop()
