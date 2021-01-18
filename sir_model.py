# This file defines a class for an SIR model
import numpy as np
from scipy.integrate import odeint

class SIR_model:
    def __init__(self, S0=999, I0=10, R0=0, t0=0, t_max=160, vaccinated=0.0,
            vaccine_effect=0.95, mask_coverage=0.8, mask_efficacy=0.2):
        """This method initiates the SIR model. In this model, S is the amount
        of people susceptible to the virus, I the amount of infected and R the
        amount of recovered or dead people."""
        # Adjustable by the user
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.t = np.linspace(t0, t_max, t_max - t0 + 1)
        self.C_mask = mask_efficacy * mask_coverage
        self.vacc = vaccinated
        self.vacc_eff = vacc_effect
        print(self.mask())
        self.growth_rate = 0.2 * self.mask()
        self.recovery_rate = 0.1
        # self.death_rate = 0.015

        # Not adjustable by the user
        self.N = S0 + I0 + R0

    def mask(self):
        return 1 - 1.75 * self.C_mask + 0.75 * self.C_mask**2

    def run(self):
        """This method runs the simulation of the model."""
        S, I, R = odeint(self.deriv, [self.S0, self.I0, self.R0], self.t).T
        return S, I, R

    def deriv(self, y, t):
        S, I, R = y
        return self.dS(S, I), self.dI(S, I), self.dR(I)

    def dS(self, S, I):
        """Calculates the difference in the amount of susceptible people for
        a single timestep."""
        # print(-self.growth_rate * self.mask_coefficient() * self.S * self.I)
        return -self.growth_rate * (S * I / self.N)

    def dI(self, S, I):
        """Calculates the difference in the amount of infected people for
        a single timestep."""
        return -self.dS(S, I) - self.dR(I)

    def dR(self, I):
        """Calculates the difference in the amount of recovered/dead people for
        a single timestep."""
        return self.recovery_rate * I

    def show_results(self):
        """When the simulation is over, this method can be used to visualize
        the results of the simulation."""
        pass

    def visualize(self):
        """This method can be used to visualize the simulation while it is
        running."""
        pass
