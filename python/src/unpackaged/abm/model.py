import random
import operator
import matplotlib
import tkinter
matplotlib.use('TkAgg')
matplotlib.use('macosx')
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import requests
import bs4

r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)

def run():
    animation = (matplotlib.animation.FuncAnimation(fig, update,
                frames=gen_function, repeat=False))
    canvas.draw()

# create main window
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)

# create layout
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# create menu bar
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run Model", command=run)

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

environment = []

# read in csv 'in.txt'
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

# create agents
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

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

    for i in range(num_of_agents):
        matplotlib.pyplot.xlim(0, 99)
        matplotlib.pyplot.ylim(0, 99)
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.scatter(agents[i].y,agents[i].x)
        #print(agents[i].y,agents[i].x)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

# wait for interactions
tkinter.mainloop()