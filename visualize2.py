import numpy as np
from matplotlib import pyplot as plt


def visualize(numbers, title):
    for i in range(np.size(numbers)):
        y = numbers[:(i + 2)]
        x = np.linspace(0, np.size(y), num=np.size(y))
        plt.plot(x, y, 'r-', label=title)
        plt.xlabel('Time (days)')
        plt.ylabel('Cases')
        plt.title('Graph of ' + title)
        plt.xlim(0, np.size(numbers))
        plt.ylim(min(numbers), max(numbers) + 1)
        plt.text(0.5, max(y) + 0.0016 * max(y), 'Cases: ' + str(int(y[i])))
        plt.legend()
        plt.draw()
        plt.pause(0.00001)
        plt.clf()

    # x_numbers = np.linspace(1, np.size(numbers), num=np.size(numbers))
    # plt.plot(x_numbers, numbers
    plt.show()
