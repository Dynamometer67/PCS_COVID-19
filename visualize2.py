import numpy as np
from matplotlib import pyplot as plt

counter = 2
numbers = np.array([1,3,2,5,5,21,4,2,4,5,6,3,2])


for _ in range(np.size(numbers)):
    y = numbers[:counter]
    x = np.linspace(1, np.size(y), num=np.size(y))
    counter += 1
    plt.plot(x,y)
    plt.draw()
    plt.pause(0.5)
    plt.clf()

x_numbers = np.linspace(1, np.size(numbers), num=np.size(numbers))
plt.plot(x_numbers, numbers)
plt.show()
