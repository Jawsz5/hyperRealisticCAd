import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt

class Rocket:
    def __init__(self, name, thrust, mass, nozzle, frame_material, fuel, fins):
        # Constants
        self.G = 6.6742e-11  # Gravitational constant in m^3/kg/s^2
        self.rPlanet = 6357000  # Radius of the planet in meters
        self.mPlanet = 5.972e24  # Mass of the planet in kg
    

        # Rocket parameters
        self.name = name
        self.thrust = thrust  # Newtons of thrust
        self.Isp1 = nozzle[0]  # Specific impulse of first stage in seconds
        self.Isp2 = nozzle[1]  # Specific impulse of second stage in seconds
        self.tMECO = 20.0  # Main Engine Cut Off time in seconds
        self.tSep1 = 2.0  # Time to remove first stage in seconds
        self.mass1 = mass[0]  # Mass of first stage in kg
        self.mass0 = mass[1]  # Mass of rocket without fuel in kg
        self.frame_material = frame_material
        self.fuel = fuel
        self.fins = fins

    def Cd(self, velocity):
        # Placeholder for drag coefficient calculation
        # Example: quadratic drag coefficient model
        return 0.1 + 0.01 * velocity  # Example linear relationship

    def heat_generation(self, state):
        x, z, veloX, veloZ, mass = state
        velocity = np.sqrt(veloX**2 + veloZ**2)
        return 0.5 * mass * velocity**2  # Simplified approximation of mechanical energy

    def temperature_change(self, heat_generated, frame_material):
        # Placeholder for temperature change calculation based on frame material
        if frame_material == "Aluminum":
            heat_capacity = 900  # J/(kg*K)
            temperature_change_per_joule = 0.0001  # Example value
            return heat_generated * temperature_change_per_joule / heat_capacity
        elif frame_material == "Steel":
            heat_capacity = 450  # J/(kg*K)
            temperature_change_per_joule = 0.0002  # Example value
            return heat_generated * temperature_change_per_joule / heat_capacity
        elif frame_material == "Titanium":
            heat_capacity = 520  # J/(kg*K)
            temperature_change_per_joule = 0.00015  # Example value
            return heat_generated * temperature_change_per_joule / heat_capacity
        elif frame_material == "Carbon Fiber":
            heat_capacity = 600  # J/(kg*K)
            temperature_change_per_joule = 0.00012  # Example value
            return heat_generated * temperature_change_per_joule / heat_capacity
        else:
            # Default calculation for other materials
            return 0.0

    def gravity(self, x, z):
        r = np.sqrt(x**2 + z**2)
        accelX = -self.G * self.mPlanet / (r**3) * x
        accelZ = -self.G * self.mPlanet / (r**3) * z
        return np.array([accelX, accelZ])

    def propulsion(self, t):
        if t < self.tMECO:
            theta = 10 * np.pi / 180
            thrustF = self.thrust
            ve = self.Isp1 * 9.81  # Exit velocity in m/s
            mdot = -thrustF / ve
        elif t < (self.tMECO + self.tSep1):
            theta = 0.0
            thrustF = 0.0
            mdot = -self.mass1 / self.tSep1
        else:
            theta = 0.0
            thrustF = 0.0
            mdot = 0.0
        thrustX = thrustF * np.cos(theta)
        thrustZ = thrustF * np.sin(theta)
        return np.array([thrustX, thrustZ]), mdot

    def derivatives(self, state, t):
        x, z, veloX, veloZ, mass = state
        r = np.sqrt(x**2 + z**2)
        
        if r != 0:
            gravityF = self.gravity(x, z) * mass
        else:
            gravityF = np.array([0, 0])
        
        thrustF, mdot = self.propulsion(t)
        velocity = np.sqrt(veloX ** 2 + veloZ ** 2)
        if velocity > 0.0:
            aeroF = -0.5 * self.Cd(velocity) * velocity**2
            aeroF_x = aeroF * veloX / velocity
            aeroF_z = aeroF * veloZ / velocity
        else:
            aeroF_x = 0.0
            aeroF_z = 0.0
        
        # Accounting for fins
        if self.fins > 0:
            # Assuming fins generate lift normal to the rocket's longitudinal axis
            # Fins create a lift force perpendicular to the rocket's longitudinal axis
            lift_perpendicular = 0.5 * self.fins * self.Cd(velocity) * velocity**2
            # Calculate angle of attack assuming fins are perpendicular to rocket's axis
            angle_of_attack = np.arctan2(veloZ, veloX)
            # Calculate lift forces
            lift_x = lift_perpendicular * np.cos(angle_of_attack)
            lift_z = lift_perpendicular * np.sin(angle_of_attack)
        else:
            lift_x = 0.0
            lift_z = 0.0
            
        forces = gravityF + thrustF + np.array([aeroF_x + lift_x, aeroF_z + lift_z])
        zdot = veloZ
        xdot = veloX
        
        if mass > 0:
            accelX = forces[0] / mass
            accelZ = forces[1] / mass
            ddot = np.array([accelX, accelZ])
        else:
            ddot = np.array([0, 0])
            mdot = 0
        
        # Heat generation and temperature change
        heat_generated = self.heat_generation(state)
        temperature_change = self.temperature_change(heat_generated, self.frame_material)
        
        # Update mass and temperature
        mass -= mdot * (t - self.tMECO)
        mass = max(mass, 0)  # Ensure mass is non-negative
        mass += temperature_change  # Adjust mass based on temperature change
        
        state_dot = np.array([xdot, zdot, ddot[0], ddot[1], mdot])
        return state_dot

    
    def simulate_flight(self):
        x0 = self.rPlanet
        z0 = 0.0
        veloX0 = 0.0
        veloZ0 = 0.0
        mass0 = self.mass0
        initial_state = np.array([x0, z0, veloX0, veloZ0, mass0])
        period = 2 * np.pi / np.sqrt(self.G * self.mPlanet) * (self.rPlanet + 200000) ** (3.0 / 2.0) * 1.5
        time = np.linspace(0, period, 1000)
        state_output = sci.odeint(self.derivatives, initial_state, time)
        x = state_output[:, 0]
        z = state_output[:, 1]
        altitude = np.sqrt(x ** 2 + z ** 2) - self.rPlanet
        veloX = state_output[:, 2]
        veloZ = state_output[:, 3]
        velocity = np.sqrt(veloX ** 2 + veloZ ** 2)
        mass = state_output[:, 4]

        # Plotting
        plt.figure()
        plt.plot(time, altitude)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Altitude (meters)")
        plt.title("Altitude vs Time")
        plt.grid()

        plt.figure()
        plt.plot(time, velocity)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Velocity (m/s)")
        plt.title("Velocity vs Time")
        plt.grid()

        plt.figure()
        plt.plot(time, mass)
        plt.xlabel("Time (seconds)")
        plt.ylabel("Mass (kg)")
        plt.title("Mass vs Time")
        plt.grid()

        plt.figure()
        plt.plot(x, z, 'r-', label='Orbit')
        plt.plot(x[0], z[0], 'g*')
        theta = np.linspace(0, 2 * np.pi, 1000)
        xPlanet = self.rPlanet * np.sin(theta)
        yPlanet = self.rPlanet * np.cos(theta)
        plt.plot(xPlanet, yPlanet, 'b-', label='Planet')
        plt.xlabel("x (meters)")
        plt.ylabel("z (meters)")
        plt.title("2D Orbit")
        plt.grid()
        plt.legend()

        plt.show()
    
    def calculate_delta_v(self):
        # Integrate the rocket's motion equations to calculate delta-v
        timesteps = 1000
        t = np.linspace(0, self.tMECO, timesteps)
        initial_state = np.array([self.rPlanet, 0.0, 0.0, 0.0, self.mass0])
        state_output = sci.odeint(self.derivatives, initial_state, t)
        
        # Calculate the initial and final velocity
        initial_velocity = np.sqrt(initial_state[2]**2 + initial_state[3]**2)
        final_velocity = np.sqrt(state_output[-1, 2]**2 + state_output[-1, 3]**2)
        
        # Calculate delta-v
        delta_v = final_velocity - initial_velocity
        
        # Add gravitational effects
        r_orbit = self.rPlanet + 290000  # Assuming altitude of 200 km
        v_orbit = np.sqrt(self.G * self.mPlanet / r_orbit)
        delta_v += v_orbit
        
        return delta_v

    def can_achieve_orbit(self):
        # Calculate required velocity to achieve orbit
        r_orbit = self.rPlanet + 200000  # Assuming altitude of 200 km
        v_orbit = np.sqrt(self.G * self.mPlanet / r_orbit)

        # Calculate delta-v capability of the rocket
        delta_v_capability = self.calculate_delta_v()

        # Check if rocket's delta-v capability exceeds required delta-v
        return delta_v_capability >= v_orbit


