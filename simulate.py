# This file defines a function which can be used to create and simulate an SIR
# model

from sir_model import SIR_model

def create_and_run():
    model = SIR_model()
    model.run()

if __name__ == "__main__":
    create_and_run()
