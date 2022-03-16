# import packages

import random
import operator
import matplotlib
import matplotlib.pyplot

# make agent list

agents = []

# make random integers and append to agents list

agents.append([random.randint(0,99),random.randint(0,99)])

# move y0 randomly

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

# move x0 randomly

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# move y0 randomly again

if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1

# move x0 randomly again

if random.random() < 0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1

# make random integers and append to agents list

agents.append([random.randint(0,99),random.randint(0,99)])

# move y1 randomly

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

# move x1 randomly

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

# move y1 randomly again

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1

# move x1 randomly again

if random.random() < 0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1

# print agents]

print(agents)

# calculate distance between points

y_diff = (agents[0][0] - agents[1][0])
y_diffsq = y_diff * y_diff

x_diff = (agents[0][1] - agents[1][1])
x_diffsq = x_diff * x_diff

sum = y_diffsq + x_diffsq

answer = sum**0.5

print(answer)

print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0], color='red')
matplotlib.pyplot.scatter(agents[1][1],agents[1][0], color='red')
matplotlib.pyplot.show()