
## modules needed
import numpy as np #numeric python
import matplotlib.pyplot as plt #graphing things with matlab
import scipy.integrate as sci #integrating things

##Constant parameters
G = 6.6742*10**-11 #gravitational constant in SI units
###Planet
rPlanet = 6357000 #kilometers
mPlanet = 5.972e24

#Rocket parameters
mass = 640.0/100 ##Kg

#motion equations: F=ma = m*2nd derivative of altitude
#z is the altitude above the surface
# meters
#zdot is the velcoity
#z double dot is the acceleration
#second order differential equation

##Gravitaitonal acceleration model
def gravity(z):
    global rPlanet,mPlanet

    r = np.sqrt(z**2)

    if r < rPlanet:
        accel = 0.0
    else:
        accel = G*mPlanet/(r**3)*r
    return accel



class Rockets:
    global mass,rPlanet,mPlanet,G

    def Derivatives(state, t):
        global mass
        #state vector
        z = state[0]
        veloZ = state[1]

        #total forces: gravity, aerodynamics, thrust
        gravityF = -gravity(z) * mass
        aeroF = 0.0 #for now
        thrustF = 0.0 #for now
        forces = gravityF + aeroF + thrustF

        #zdot - kinematic relationship
        zdot = veloZ

        #compute acceleration
        zddot = forces/mass

        #compute the state dot vector
        stateDot = np.asarray([zdot,zddot])



        return stateDot

    #### MAIN SCRIPT

    print('Surface Gravity (m/s^2) = ',gravity(rPlanet))

    ###initial conditions
    z0 = rPlanet
    veloZ0 = 25*331.0 #m/s
    initialState = np.array([z0, veloZ0])

    #Time window
    tup = np.linspace(0,35,1000)

    #numerical integration call
    stateup = sci.odeint(Derivatives, initialState, tup)

    zup = stateup[:, 0]
    altitude = zup - rPlanet
    veloZup = stateup[:, 1]

    ##plot this thing


    ##altitude
    plt.plot(tup, altitude)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Altitude (meters)")
    plt.grid();

    ##velo
    plt.figure(); ##new graph
    plt.plot(tup, veloZup)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Normal Speed (meters/Second)")
    plt.grid();