# This file defines a class for an SIR model

class SIR_model:
    def __init__(self, S=10**7, I=100, R=0, t=0, growth_rate=0.25,
            recovery_rate=0.1, vaccinated=0.0, avg_age=40, std_age=20):
        """This method initiates the SIR model. In this model, S is the amount
        of people susceptible to the virus, I the amount of infected and R the
        amount of recovered or dead people."""
        self.S = S
        self.I = I
        self.R = R
        self.t = t
        self.growth_rate=growth_rate
        self.recovery_rate = recovery_rate
        self.avg_age = avg_age
        self.std_age = std_age

    def run(self):
        """This method runs the simulation of the model."""
        # This condition should be changed to a case when we would want to stop
        # the simulation.
        while self.t < 100:
            self.step()

    def step(self):
        """This method runs a single step in the simulation."""
        self.S += self.dS()
        self.I += self.dI()
        self.R += self.dR()
        self.t += 1

    def dS(self):
        """Calculates the difference in the amount of susceptible people for
        a single timestep."""
        return -self.growth_rate * self.S * self.I

    def dI(self):
        """Calculates the difference in the amount of infected people for
        a single timestep."""
        return self.dS() - self.dR()

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