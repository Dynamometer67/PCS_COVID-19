# This file defines a class for an SIR model
import numpy as np
from scipy.integrate import odeint

class SIR_model:
    def __init__(self, S0=999, I0=10, R0=0, t_max=100, growth_rate=0.2,
                 recovery_rate=0.1, mask_coverage=0.0, mask_efficacy=0.0):
        """This method initiates the SIR model. In this model, S is the amount
        of people susceptible to the virus, I the amount of infected and R the
        amount of recovered or dead people."""
        # Adjustable by the user
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.t_max = t_max
        self.growth_rate = growth_rate
        self.rec_rate = recovery_rate
        self.mask_cov = mask_coverage
        self.mask_eff = mask_efficacy
        # self.stochastic = stochastic

    def mask_factor(self):
        C_mask = self.mask_eff * self.mask_cov
        return 1 - 1.75 * C_mask + 0.75 * C_mask**2

    def run(self):
        """This method runs the simulation of the model."""
        self.t = np.linspace(0, self.t_max, self.t_max + 1)
        self.N = self.S0 + self.I0 + self.R0
        self.beta = self.growth_rate * self.mask_factor()

        self.S, self.I, self.R = \
                odeint(self.step, [self.S0, self.I0, self.R0], self.t, mxstep=100000).T

    def step(self, y, t):
        S, I, R = y
        dS = self.dS(S, I)
        dI = self.dI(S, I)
        dR = self.dR(I)

        # print(dS)

        # if self.stochastic:
        # S_noise = self.step_noise(dS)
        # R_noise = self.step_noise(dR)
        # dS += S_noise
        # dI -= S_noise + R_noise
        # dR += R_noise

        # print(dS)
        # print(y)

        # if t < 3:
        #     print("a")
            # print("dS = " + str(dS) + " and S = " + str(S))
            # print("dI = " + str(dI) + " and I = " + str(I))
            # print("dR = " + str(dR) + " and R = " + str(R))

        return dS, dI, dR

    def step_noise(self, dX):
        var = abs(dX / 2)
        noise = np.random.normal(0.0, var)

        if (noise > dX and dX >= 0) or (noise < dX and dX <= 0):
            return dX
        return noise

    def noise(self, X_diff, mean=0, var_factor=0.5):
        # Create an array containing noise values with the specified mean and
        # variance.
        X_noise = np.random.normal(mean, np.abs(X_diff * var_factor))
        # Check if X_noise is smaller than X_diff and X_diff is bigger than 0
        # for each element. This is needed to change all noise values that are
        # too large with the np.where function. The opposite is also done to
        # change values that are too small.
        pos_condition = np.all([X_noise <= X_diff, X_diff >= 0], axis=0)
        neg_condition = np.all([X_noise >= X_diff, X_diff <= 0], axis=0)
        # Now check whether either one of the conditions is true for all
        # elements so that we can use it for np.where. It is used to change all
        # X_noise values that are bigger than their corresponding value in
        # X_diff if X_diff is positive and all X_noise values that are smaller
        # than their corresponding value in X_diff if X_diff is negative to the
        # values in X_diff. It basically sets boundaries for the values of
        # X_noise so that the absolute values of X_noise are always smaller
        # than or equal to the absolute values of X_diff. The reason why it is
        # complicated is that these statements also make it so that values that
        # are negative stay negative and values that are positive stay positive.
        condition = np.any([pos_condition, neg_condition], axis=0)
        # Set all noise values to be within the boundaries.
        X_bounded_noise = np.where(condition, X_noise, X_diff)

        # Now make it so that the previous noise values are added to the
        # current noise value for each noise value.
        return np.cumsum(X_bounded_noise)

    def dS(self, S, I):
        """Calculates the difference in the amount of susceptible people for
        a single timestep."""
        return -self.beta * (S * I / self.N)

    def dI(self, S, I):
        """Calculates the difference in the amount of infected people for
        a single timestep."""
        return -self.dS(S, I) - self.dR(I)

    def dR(self, I):
        """Calculates the difference in the amount of recovered/dead people for
        a single timestep."""
        return self.rec_rate * I

    def add_stochasticity(self):
        S_diff = np.diff(self.S)
        R_diff = np.diff(self.R)

        S_noise = self.noise(S_diff)
        R_noise = self.noise(R_diff)

        self.S[1:] += S_noise
        self.I[1:] -= S_noise + R_noise
        self.R[1:] += R_noise

        print(self.S + self.I + self.R)

    def euler_maruyama(self):
        """
        https://www.math.kit.edu/ianm3/lehre/nummathfin2012w/media/euler_maruyama.pdf
        https://en.wikipedia.org/wiki/Euler%E2%80%93Maruyama_method
        """
        pass

    def show_results(self):
        """When the simulation is over, this method can be used to visualize
        the results of the simulation."""
        pass

    def visualize(self):
        """This method can be used to visualize the simulation while it is
        running."""
        pass
