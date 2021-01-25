-------------------------------------------------------------------------------
Jesse van den Berge - 12410241
Mark van Hofwegen   - 12378348

This file explains how the figures and simulations can be reproduced.
-------------------------------------------------------------------------------
Step 1: Start up the GUI with the following - "python3 ./simulate.py"
Step 2: Fill in the specified parameters to reproduce the graphs.
step 3: Click on OK when you are done filling in the parameters.

Here are the parameters used for every graph:
- Figure 1: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4, rec_rate=0.1, mask_cov = 0.0,  mask_eff = 0.0,  stochastic=1.0.
- Figure 2: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4, rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.2,  stochastic=1.0.
- Figure 3: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4, rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.4,  stochastic=1.0.
- Figure 4: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4, rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.5,  stochastic=1.0.
- Figure 5: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4, rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.55, stochastic=1.0.
- Figure 6: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4, rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.6,  stochastic=1.0.
- Figure 7: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4, rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.65, stochastic=1.0.
- Figure 8: S0=10^6, I0=10^5, R0=0, t_max=150, growth_rate=0.4, rec_rate=0.1, mask_cov = 0.95, mask_eff = 0.7,  stochastic=1.0.
- Figure 9: To reproduce this figure, use the function "visualize_mask_eff()" in the main function and comment all the other code
            in the main function in simulate.py.

- Table 1: The data for this table can be obtained by using the function "get_infl_points()" in the main function of simulate.py
           and commenting all the other code in the main function.
