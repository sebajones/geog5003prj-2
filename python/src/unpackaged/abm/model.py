# import random

import random

# make y0 and x0 random integer between 0 and 100

y0 = random.randint(0,99)
x0 = random.randint(0,99)

# move y0 randomly

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

# move x0 randomly

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

# move y0 randomly again

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

# move x0 randomly again

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

# make y1 and x1 random integer between 0 and 100

y1 = random.randint(0,99)
x1 = random.randint(0,99)

# move y1 randomly

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

# move x1 randomly

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

# move y1 randomly again

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

# move x1 randomly again

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

# calculate distance between points

y_diff = (y0 - y1)
y_diffsq = y_diff * y_diff

x_diff = (x0 - x1)
x_diffsq = x_diff * x_diff

sum = y_diffsq + x_diffsq

answer = sum**0.5
print(answer)