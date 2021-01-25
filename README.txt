-------------------------------------------------------------------------------
Jesse van den Berge - 12410241
Mark van Hofwegen   - 12378348

This file explains how the figures and simulations can be reproduced and how
the program works.
-------------------------------------------------------------------------------

Files and description:
    This project consists of gui.py, sir_model.py and simulate.py.
    In order to work with these files, you have to install python3 and the
    following libraries:
        - matplotlib
        - tkinter
        - numpy
        - scipy

    sir_model.py:
        This file defines a class for the SIR model, which contains the
        ODEs, visualization and methods to run the model.

    gui.py:
        This file defines a class for the GUI, which is used to set the
        parameters for the model.

    simulate.py:
        This file is used to create and simulate the model. In this file,
        functions are defined for testing and creating figures.


Model parameters:
    - S0: The starting value for the amount of susceptible people. Can be any
      positive real number.
    - I0: The starting value for the amount of infected people. Can be any
      positive real number.
    - R0: The starting value for the amount of recovered people. Can be any
      positive real number.
    - t_max: The amount of timesteps the simulation will take. Can be any
      positive integer
    - growth_rate: The rate at which the infected people infect the susceptible
      people. Can be any positive real number.
    - rec_rate: The rate at which infected people move to recovered. Can be any
      positive real number.
    - mask_cov: The ratio of people that wear mouth masks. Can be any real
      number between 0 and 1.
    - mask_eff: The effectiveness of the mouth masks. Can be any real number
      between 0 and 1.
    - stochastic: Indicates whether the model is stochastic or not. Must be 0
      if the model should not be stochastic. Can be any other real number to
      indicate that the model is stochastic.


Reproducing the figures:
    Step 1: Start up the GUI with the following - "python3 ./simulate.py"
        Make sure the original code in the main function of this file is
        uncommented.
    Step 2: Fill in the specified parameters to reproduce the graphs.
    step 3: Click on OK when you are done filling in the parameters.

    The figures can also be recreated without using the GUI. If this is what
    you want, then you can do the following in the main function of
    simulate.py:
        1. Comment or remove the code in the main function of simulate.py
        2. Create the model using "model = SIR_model()" and put in the brackets
           the desired values for the parameters.
        3. Run the model using "model.run()".
        4. Plot the graph using
           "model.show_results("SIR simulation of COVID-19 spread")".

    Here are the parameters used for every figure or instructions for
    recreating them when they require a different method to recreate them:

        - Figure 1: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4,
          rec_rate=0.1, mask_cov = 0.0,  mask_eff = 0.0,  stochastic=1.0.

        - Figure 2: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4,
          rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.2,  stochastic=1.0.

        - Figure 3: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4,
          rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.4,  stochastic=1.0.

        - Figure 4: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4,
          rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.5,  stochastic=1.0.

        - Figure 5: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4,
          rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.55, stochastic=1.0.

        - Figure 6: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4,
          rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.6,  stochastic=1.0.

        - Figure 7: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4,
          rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.65, stochastic=1.0.

        - Figure 8: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4,
          rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.7,  stochastic=1.0.

        - Figure 9: To reproduce this figure, use the function
          "visualize_mask_eff()" in the main function and comment all the other
          code in the main function in simulate.py.

        - Table 1: The data for this table can be obtained by using the
          function "get_infl_points()" in the main function of simulate.py
          and commenting all the other code in the main function.
