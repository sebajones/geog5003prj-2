import random
import operator
import matplotlib.pyplot
import agentframework
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

# define measure distance method
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# create agents
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

# move agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        agents[i].move()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

#call measure distance method
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)



#a = agentframework.Agent()

#print(a.y, a.x)
#a.move()
#print(a.y, a.x)

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()