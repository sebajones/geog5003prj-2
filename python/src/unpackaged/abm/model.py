# import packages

import random
import operator
import matplotlib
import matplotlib.pyplot

# control number of agents
num_of_agents = 10
num_of_iterations = 100

# make agent list

agents = []

# make random integers and append to agents list

for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

for i in range(num_of_agents):

    #move agents randomly

    for j in range(num_of_iterations):

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

# print agents]

print(agents)

# calculate distance between points

# y_diff = (agents[0][0] - agents[1][0])
# y_diffsq = y_diff * y_diff

# x_diff = (agents[0][1] - agents[1][1])
# x_diffsq = x_diff * x_diff

# sum = y_diffsq + x_diffsq

# answer = sum**0.5

# print(answer)

# print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()