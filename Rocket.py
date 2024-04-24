import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

class Rocket:
    def __init__(self, name, thrust, mass, nozzle, frame_material, fuel, fins):
        # Constants
        self.G = 6.6742e-11  # Gravitational constant in m^3/kg/s^2
        self.rPlanet = 6357000  # Radius of the planet in meters
        self.mPlanet = 5.972e24  # Mass of the planet in kg

        # Rocket parameters
        self.name = name
        self.max_thrust = thrust  # Newtons of thrust
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
            thrustF = self.max_thrust
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
        gravityF = self.gravity(x, z) * mass
        velocity = np.sqrt(veloX**2 + veloZ**2)
        heat_generated = self.heat_generation(state)
        temperature_change = self.temperature_change(heat_generated, self.frame_material)
        mass -= temperature_change
        if velocity > 0.0:  # Check if velocity is greater than zero
            aeroF = -0.5 * self.Cd(velocity) * velocity**2  # Drag force
            aeroF_x = aeroF * veloX / velocity
            aeroF_z = aeroF * veloZ / velocity
        else:
            aeroF_x = 0.0
            aeroF_z = 0.0
        thrustF, mdot = self.propulsion(t)
        forces = gravityF + np.array([aeroF_x, aeroF_z]) + thrustF
        zdot = veloZ
        xdot = veloX
        if mass > 0:
            ddot = forces / mass
        else:
            ddot = 0
            mdot = 0
        state_dot = np.array([xdot, zdot, ddot[0], ddot[1], mdot])
        return state_dot
    
    def overheating(self, state):
        heat_generated = self.heat_generation(state)
        temperature_change = self.temperature_change(heat_generated, self.frame_material)
        return heat_generated <= temperature_change

    def aerodynamic_failure(self, velocity):
        max_velocity_for_stability = 500  # Define a maximum stable velocity
        return velocity <= max_velocity_for_stability

    def enough_thrust_mass_constraint(self):
        # Check if there is enough thrust to lift the rocket of given mass
        return self.max_thrust >= self.mass0 * 9.81

    def can_reach_orbit(self, x0=0.0, z0=0.0, veloX0=0.0, veloZ0=0.0):
        initial_state = [x0, z0, veloX0, veloZ0, self.mass0]
        period = 2 * np.pi / np.sqrt(self.G * self.mPlanet) * (self.rPlanet + 200000) ** (3.0 / 2.0) * 1.5
        time = np.linspace(0, period, 1000)

        state_output = sci.odeint(self.derivatives, initial_state, time)
        altitude = np.sqrt(state_output[:, 0] ** 2 + state_output[:, 1] ** 2) - self.rPlanet
        velocity = np.sqrt(state_output[:, 2] ** 2 + state_output[:, 3] ** 2)
        max_altitude = max(altitude)

        overheating_check = all(self.overheating(state) for state in state_output)
        aerodynamic_failure_check = all(self.Cd(v) < 0.3 for v in velocity)  # Example Cd threshold
        enough_thrust_mass_constraint_check = self.enough_thrust_mass_constraint()

        if max_altitude > 0 and overheating_check and aerodynamic_failure_check and enough_thrust_mass_constraint_check:
            return True
        else:
            return False

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