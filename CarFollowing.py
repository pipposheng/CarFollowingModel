""" This is a Python Module for the simulation of Car-Following Theory using
    GM First Car Following Model. The movements of ten vehicles are simulated.
    """
""" This Module can also be modified to Functions with parameters of Coefficient,
    Reaction Time, Initial Speed, Deceleration Rate, Headway, Total Time, and
    Number of Vehicles."""
    
coef = 0.74           # Stimulus Coefficient = 0.74
deltat = 2.2          # Reaction Time = 2.2 s, Time gap between the decelerations.
Vini = 44             # Initial Speed  = 44 ft/s
rate = -4.6           # Deceleration Rate of the First Vehicle (ft/s^2)
hini = -114           # Initial Headway between each Vehicle = 114 ft
N = 10                # Number of Vehicles
T = 30                # Total Simulation Time
Tstep = 0.1           # Time step for Simulation
Nstep = int(T/Tstep)  # Simulation Steps

t = []            # Time of Traveling
for i in range(0,Nstep):   
    t.append(i*0.1)

# Initialization of Deceleration Matrix, Speed Matrix, Movement Matrix
a = [[]]
v = [[]]
d = [[]]

for n in range(0,N):
    if n == 0:       # Speed and Deceleration Lists of the First Vehicle
        v[0] = [Vini]
        a[0] = [rate]
        for i in range(1,Nstep):
            if (v[0][i-1] + a[0][i-1]*0.1) > 0:
                v[0].append(v[0][i-1] + a[0][i-1]*0.1)
                a[0].append(rate)
            else:
                v[0].append(0)
                a[0].append(0)
    else:            # Speed and Deceleration Lists of the Following Vehicles
        v.append([])
        a.append([])
        v[n].append(Vini)
        a[n].append(0)
        for i in range(1,Nstep):
            if i < 22*n:
                v[n].append(Vini)
                a[n].append(0)
            elif (v[n][i-1] + a[n][i-1]*0.1) > 0:
                v[n].append(v[n][i-1] + a[n][i-1]*0.1)
                a[n].append(coef*(v[n-1][i-1] - v[n][i-1]))
            else:
                v[n].append(0)
                a[n].append(0)

for n in range(0,N):    # Movement Lists of the Vehicles
    d.append([])
    d[n].append(n*hini)
    for i in range(1,Nstep):
        d[n].append(d[n][i-1] + (v[n][i-1] + v[n][i]) / 2 * 0.1)
        
# Output to File for Plotting
f = open('CarFollowing.txt','w')
for i in range(0,Nstep):
    f.write('%.1f\t' %t[i])
    for n in range(0,N):
        f.write('%.2f\t' %d[n][i])
    f.write('\n')
f.close()
