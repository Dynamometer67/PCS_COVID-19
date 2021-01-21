import numpy as np
from matplotlib import pyplot as plt


def visualize(S, I, R, t_max):
    for i in range(t_max):
        t = np.linspace(0, i, num=i)
        y_s = S[:i]
        y_i = I[:i]
        y_r = R[:i]

        plt.plot(t, y_s, 'r-', label="Susceptible")
        plt.plot(t, y_i, 'b-', label="Infected")
        plt.plot(t, y_r, 'g-', label="Recovered")

        plt.xlabel('Time (days)')
        plt.ylabel('Cases')
        plt.title('SIR simulation of COVID-19 spread')
        plt.xlim(0, t_max)
        plt.ylim(0, 1000)
        # plt.text(0.5, max(numbers) + 0.0016 * max(numbers), 'Cases: ' + str(int(y[i])))
        plt.legend()
        plt.draw()
        plt.pause(0.00001)
        if i is not (t_max - 1):
            plt.clf()
        else:
            plt.show()


    # x_numbers = np.linspace(1, np.size(numbers), num=np.size(numbers))
    # plt.plot(x_numbers, numbers
