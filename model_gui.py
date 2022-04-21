import random
import operator
import matplotlib
matplotlib.use('TkAgg')
matplotlib.use('macosx')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import tkinter
import csv

environment = []

# read in csv
with open("in.txt", newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# create agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

carry_on = True

def update(frame_number):
    fig.clear()
    global carry_on

    # move agents
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")

    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update,
    frames=gen_function, repeat=False)
    canvas.draw()

# main window
root = tkinter.Tk()

root.mainloop()