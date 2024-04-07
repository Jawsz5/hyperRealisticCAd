
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
#z is the altitude from the center of the planet along the north pole
#x is the altitude from the center along the equator
# meters
#zdot is the velcoity along z
#z double dot is the acceleration along z
#second order differential equation

##Gravitaitonal acceleration model
def gravity(x, z):
    global rPlanet,mPlanet

    r = np.sqrt(x**2 + z**2)

    if r < rPlanet:
        accelX = 0.0
        accelZ = 0.0
    else:
        accelX = G*mPlanet/(r**3)*x
        accelZ = G*mPlanet/(r**3)*z
    return np.asarray([accelX, accelZ])



##After implementing thrust, create soemthing for size (mass) of the rocket, and for heat possibly

class Rockets:
    global mass,rPlanet,mPlanet,G

    def Derivatives(state, t):
        global mass
        #state vector
        x = state[0]
        z = state[1]
        veloX = state[2]
        veloZ = state[3]

        #total forces: gravity, aerodynamics, thrust
        gravityF = -gravity(x,z) * mass
        aeroF = np.asarray([0.0, 0.0]) #for now
        thrustF = np.asarray([0.0, 0.0]) #for now
        forces = gravityF + aeroF + thrustF

        #zdot - kinematic relationship
        zdot = veloZ
        xdot = veloX

        #compute acceleration
        ddot = forces/mass

        #compute the state dot vector
        stateDot = np.asarray([xdot, zdot,ddot[0], ddot[1]])



        return stateDot

    #### MAIN SCRIPT

    print('Surface Gravity (m/s^2) = ',gravity(0, rPlanet))

    ###initial conditions
    x0 = rPlanet + 600000
    z0 = 00.0
    r0 = np.sqrt(x0**2+z0**2)
    veloZ0 = np.sqrt(G*mPlanet/r0)*1.1 #m/s
    veloX0 = 100.0
    initialState = np.array([x0, z0, veloX0, veloZ0])

    #Time window
    period = 2*np.pi/np.sqrt(G*mPlanet)*r0**(3.0/2.0)*1.5
    tup = np.linspace(0,period,1000)

    #numerical integration call
    stateup = sci.odeint(Derivatives, initialState, tup)

    xup = stateup[:,0]
    zup = stateup[:, 1]
    altitude = np.sqrt(xup**2 + zup**2) - rPlanet
    veloXup = stateup[:, 2]
    veloZup = stateup[:, 3]
    veloup = np.sqrt(veloXup**2 + veloZup**2)

    ##plot this thing


    ##altitude
    plt.plot(tup, altitude)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Altitude (meters)")
    plt.grid();

    ##velo
    plt.figure(); ##new graph
    plt.plot(tup, veloup)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Total speed (meters/Second)")
    plt.grid();

    ##2d orbit
    plt.figure()
    plt.plot(xup, zup, 'r-', label='Orbit')
    plt.plot(xup[0], zup[0], 'g*')
    theta = np.linspace(0,2*np.pi,100)
    xPlanet = rPlanet*np.sin(theta)
    yPlanet = rPlanet*np.cos(theta)
    plt.plot(xPlanet,yPlanet, 'b-', label = 'Planet')
    plt.grid()
    plt.legend()