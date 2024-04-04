
## modules needed
import numpy as np #numeric python
import matplotlib.pyplot as plt #graphing things with matlab
import scipy.integrate as sci #integrating things


##Constant parameters
mass = 640.0/100 ##Kg


#motion equations: F=ma = m*2nd derivative of altitude
#z is the altitude above the surface
# meters
#zdot is the velcoity
#z double dot is the acceleration
#second order differential equation
def Derivatives(state, t):
    global mass
    #state vector
    z = state[0]
    veloZ = state[1]

    #total forces: gravity, aerodynamics, thrust
    gravity = -9.807 * mass
    aero = 0.0 #for now
    thrust = 0.0 #for now
    forces = gravity + aero + thrust

    #zdot - kinematic relationship
    zdot = veloZ

    #compute acceleration
    zddot = forces/mass

    #compute the state dot vector
    stateDot = np.asarray([zdot,zddot])



    return stateDot

#### MAIN SCRIPT

###initial conditions
tZ0 = 0.0
veloZ0 = 164.0 #m/s
initialState = np.array([tZ0, veloZ0])

#Time window
tup = np.linspace(0,35,1000)

#numerical integration call
stateup = sci.odeint(Derivatives, initialState, tup)

zup = stateup[:, 0]
veloZup = stateup[:, 1]

##plot this thing


##altitude
plt.plot(tup, zup)
plt.xlabel("Time (seconds)")
plt.ylabel("Altitude (meters)")
plt.grid();

##velo
plt.figure(); ##new graph
plt.plot(tup, veloZup)
plt.xlabel("Time (seconds)")
plt.ylabel("Normal Speed (meters/Second)")
plt.grid();