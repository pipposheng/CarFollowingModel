# CarFollowingModel
Simulation of Car-Following Model using GM First Car-Following Model using Python!

This code simulates a car-following model with ten vehicles. The vehicles was traveling at 44 ft/sec.
The headway between each vehicle is 114 ft. 

At time 0, vehicle 1 decelerated with a deceleration rate of 4.6 ft/sec^2. Each following vehicle decelerated 2.2 seconds later
than the vehicle in front of it. The deceleration rates of the following vehicles follow the GM's First Car-Following Model,
while the stimulus coefficient was 0.74. The equation is a(t+t') = 0.74(v_n-1(t) - V_n(t)).

The vehicle movement until the stop of the last vehicle is then simulated. 

