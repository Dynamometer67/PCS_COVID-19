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
        plt.ylim(min(numbers), max(numbers) + max(numbers))
        plt.text(0.5, max(numbers) + 0.0016 * max(numbers), 'Cases: ' + str(int(y[i])))
        plt.legend()
        plt.draw()
        plt.pause(0.00001)
        if i is not (np.size(numbers) - 1):
            plt.clf()
        else:
            plt.show()


    # x_numbers = np.linspace(1, np.size(numbers), num=np.size(numbers))
    # plt.plot(x_numbers, numbers
