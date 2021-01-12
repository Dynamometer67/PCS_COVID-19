
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x = []
y1 = []
y2 = []
index = count()


def animate(i):
    x.append(next(index))
    y1.append(random.randint(1,5))
    y2.append(random.randint(1,5))

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')
    plt.xlim(0, 50)
    plt.ylim(0, 50)

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=100)

plt.tight_layout()
plt.show()
