import numpy as np
from matplotlib import pyplot as plt


def find_max(S, I, R):
    max = np.array([S, I, R])
    return np.max(max)


def visualize(S, I, R, t_max):
    max_number = find_max(S, I, R)

    for i in range(1, t_max + 1):
        t = np.linspace(0, i, num=i)
        y_s = S[:i]
        y_i = I[:i]
        y_r = R[:i]

        plt.plot(t, y_s, 'r-', label="Susceptible: " + str(int(y_s[-1])))
        plt.plot(t, y_i, 'b-', label="Infected: " + str(int(y_i[-1])))
        plt.plot(t, y_r, 'g-', label="Recovered: " + str(int(y_r[-1])))

        plt.xlabel('Time (days)')
        plt.ylabel('Cases')
        plt.title('SIR simulation of COVID-19 spread')
        plt.xlim(0, t_max)
        plt.ylim(0, max_number + 0.05 * max_number)

        # plt.text(0.5, max_number + 0.5, 'Cases: ' + str((y_s[-1])))
        plt.legend()
        plt.draw()
        plt.pause(0.00001)
        if i is not t_max:
            plt.clf()
        else:
            plt.show()


    # x_numbers = np.linspace(1, np.size(numbers), num=np.size(numbers))
    # plt.plot(x_numbers, numbers
