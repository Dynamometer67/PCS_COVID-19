# This file defines a class for an SIR model

class SIR_model:
    def __init__(self, S=10**7, I=100, R=0, t=0,
            vaccinated=0.0, vaccine_effect=0.95, masks=0.0):
        """This method initiates the SIR model. In this model, S is the amount
        of people susceptible to the virus, I the amount of infected and R the
        amount of recovered or dead people."""
        # Adjustable by the user
        self.S = S
        self.I = I
        self.R = R
        self.t = t
        self.masks = masks
        self.vaccinated = vaccinated
        self.vaccine_effect = vaccine_effect
        self.growth_rate = 0.2

        # Not adjustable by the user
        self.recovery_rate = 0.1
        self.death_rate = 0.015
        self.N = S + I + R
        # 0.5 because most masks have an efficiency of 50%
        # self.mask_coefficient = self.masks * 0.5

    def mask_coefficient(self):
        return 0.8 - 0.0175 * self.masks + 0.0001 * self.masks**2

    def run(self):
        """This method runs the simulation of the model."""
        # This condition should be changed to a case when we would want to stop
        # the simulation.
        while self.t < 10:
            self.step()

    def step(self):
        """This method runs a single step in the simulation."""
        print(self.S, self.I, self.R)
        self.S += self.dS()
        self.I += self.dI()
        self.R += self.dR()
        self.t += 1
        # if self.t % 5 == 0:
        print("Susceptible: ", str(self.S))
        print("Infected: ", str(self.I))
        print("Recovered: ", str(self.R))
        print("Total: ", str((self.S + self.I + self.R)))

    def dS(self):
        """Calculates the difference in the amount of susceptible people for
        a single timestep."""
        # print(-self.growth_rate * self.mask_coefficient() * self.S * self.I)
        return -self.growth_rate * self.S * self.I / self.N

    def dI(self):
        """Calculates the difference in the amount of infected people for
        a single timestep."""
        return -self.dS() - self.dR()

    def dR(self):
        """Calculates the difference in the amount of recovered/dead people for
        a single timestep."""
        return self.recovery_rate * self.I

    def show_results(self):
        """When the simulation is over, this method can be used to visualize
        the results of the simulation."""
        pass

    def visualize(self):
        """This method can be used to visualize the simulation while it is
        running."""
        pass
