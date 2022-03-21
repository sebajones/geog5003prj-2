import random
import operator
import matplotlib.pyplot as plt
import agentframework
import csv

f = open("in.txt")

environment = []

for row in f:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
f.close()

plt.imshow(environment)
plt.show()

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()


plt.xlim(0, 99)
plt.ylim(0, 99)
for i in range(num_of_agents):
    plt.scatter(agents[i].x, agents[i].y)
plt.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)