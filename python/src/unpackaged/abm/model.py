# import packages

import random
import operator
import matplotlib.pyplot
import time

start = time.process_time()

def distance_between(agents_row_a, agents_row_b):
    return ((((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] -
    agents_row_b[1])**2))**0.5)

# control number of agents
num_of_agents = 10
num_of_iterations = 100

# make agent list

agents = []

# make random integers and append to agents list
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# move agents
for j in range(num_of_iterations):
    for i in range(num_of_agents):

        # move y0 randomly
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        # move x0 randomly
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100

# print agents

# print(answer)
# answer = ((((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] -
#   agents_row_b[1])**2))**0.5)

# print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

end = time.process_time()

print("time = " + str(end - start))