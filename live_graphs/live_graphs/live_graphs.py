
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('fivethirtyeight')

fig = plt.figure()
#plot 1x1 subplot 1
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('graph_data.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs, ys)

# anamate fig using funtion animate every 2 secunds
ani = animation.FuncAnimation(fig, animate, interval=2000)


plt.show()