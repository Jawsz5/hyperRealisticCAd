import numpy as np
from Rocket import Rocket
import random


# Define the parameters for 15 real rockets
rockets_data = [
    {"name": "Falcon 9", "thrust": 7607e3, "mass": [549054, 549054 + 10188], "nozzle": [282, 348], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 4},
    {"name": "Saturn V", "thrust": 35080e3, "mass": [2970000, 2970000 + 127000], "nozzle": [265, 421], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 0},
    {"name": "Delta IV Heavy", "thrust": 9631e3, "mass": [733000, 733000 + 28550], "nozzle": [275, 370], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 0},
    {"name": "Atlas V 401", "thrust": 4152e3, "mass": [334000, 334000 + 10100], "nozzle": [311, 410], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 0},
    {"name": "H-IIA 202", "thrust": 1250e3, "mass": [285000, 285000 + 13400], "nozzle": [442, 460], "frame_material": "Aluminum", "fuel": "H2/LOX", "fins": 0},
    {"name": "Long March 2D", "thrust": 2960e3, "mass": [401000, 401000 + 14200], "nozzle": [270, 293], "frame_material": "Aluminum", "fuel": "N2O4/UDMH", "fins": 0},
    {"name": "Vega", "thrust": 2200e3, "mass": [137000, 137000 + 7350], "nozzle": [295, 318], "frame_material": "Aluminum", "fuel": "Solid", "fins": 0},
    {"name": "Soyuz-2.1b", "thrust": 4220e3, "mass": [308000, 308000 + 7150], "nozzle": [311, 330], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 0},
    {"name": "Falcon Heavy", "thrust": 22e6, "mass": [1420788, 1420788 + 55698], "nozzle": [282, 348], "frame_material": "Carbon Fiber", "fuel": "RP-1/LOX", "fins": 4},
    {"name": "Electron", "thrust": 0.0285e6, "mass": [12500, 12500 + 1800], "nozzle": [303, 311], "frame_material": "Composite", "fuel": "RP-1/LOX", "fins": 0},
    {"name": "Starship", "thrust": 71e6, "mass": [1200000, 1200000 + 120000], "nozzle": [380, 380], "frame_material": "Stainless Steel", "fuel": "Liquid Methane/LOX", "fins": 0},
    {"name": "New Glenn", "thrust": 3.85e6, "mass": [3000000, 3000000 + 125000], "nozzle": [421, 462], "frame_material": "Composite", "fuel": "Liquid Hydrogen/LOX", "fins": 0},
    {"name": "Delta II", "thrust": 890e3, "mass": [23000, 23000 + 2040], "nozzle": [275, 340], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 3},
    {"name": "Falcon 1", "thrust": 420e3, "mass": [30600, 30600 + 470], "nozzle": [282, 348], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 4},
    {"name": "Ariane 6", "thrust": 1900e3, "mass": [530000, 530000 + 17000], "nozzle": [457, 460], "frame_material": "Aluminum", "fuel": "H2/LOX", "fins": 0},


]


# Simulate flights for each rocket
for rocket_data in rockets_data:
    rocket = Rocket(rocket_data["name"], rocket_data["thrust"], rocket_data["mass"], rocket_data["nozzle"],
                    rocket_data["frame_material"], rocket_data["fuel"], rocket_data["fins"])
    print(f"Rocket: {rocket.name}")
    print(rocket.can_achieve_orbit())
    print("=" * 50)

# List to store instances of rockets
rockets = []

# Define ranges for randomized parameters
thrust_range = (1e6, 2e6)  # Thrust in Newtons
mass_range = (1e5, 2e5)  # Mass in kg
isp_range = (200, 400)  # Specific impulse in seconds
material_options = ["Aluminum", "Steel", "Titanium", "Carbon Fiber"]
fuel_range = (1e4, 2e4)  # Fuel mass in kg
fin_options = ["Small", "Medium", "Large"]

# Create 20 instances of rockets with randomized parameters
rockets = []
for i in range(20):
    name = f"Rocket {i+1}"
    thrust = np.random.uniform(*thrust_range)
    mass1 = np.random.uniform(*mass_range)
    mass0 = mass1 + np.random.uniform(*fuel_range)  # Total mass including fuel
    nozzle = (np.random.uniform(*isp_range), np.random.uniform(*isp_range))
    frame_material = np.random.choice(material_options)
    fuel = np.random.uniform(*fuel_range)
    fins = np.random.choice(fin_options)
    rockets.append(Rocket(name, thrust, (mass1, mass0), nozzle, frame_material, fuel, fins))

# Simulating flight for each rocket
#about 30-50% of these rockets with randomized parameters fail which is ideal
for rocket in rockets:
    print(f"Rocket: {rocket.name}")
    print("\n")
    print(rocket.can_achieve_orbit())





# Test the Rocket class with example rockets
'''
rocket1_thrust = 9000000  # Newtons of thrust
rocket1_mass = (500000, 200000)  # Mass of first stage and rocket without fuel in kg
rocket1 = Rocket("Rocket 1", rocket1_thrust, rocket1_mass, nozzle=(300, 320), frame_material="Aluminum", fuel=300000, fins=3)

rocket2_thrust = 8000000  # Newtons of thrust
rocket2_mass = (550000, 210000)  # Mass of first stage and rocket without fuel in kg
rocket2 = Rocket("Rocket 2", rocket2_thrust, rocket2_mass, nozzle=(310, 330), frame_material="Steel", fuel=280000, fins=4)

rocket3_thrust = 6000000  # Newtons of thrust
rocket3_mass = (450000, 190000)  # Mass of first stage and rocket without fuel in kg
rocket3 = Rocket("Rocket 3", rocket3_thrust, rocket3_mass, nozzle=(340, 360), frame_material="Titanium", fuel=250000, fins=4)

rocket4_thrust = 750000  # Newtons of thrust
rocket4_mass = (480000, 220000)  # Mass of first stage and rocket without fuel in kg
rocket4 = Rocket("Rocket 4", rocket4_thrust, rocket4_mass, nozzle=(320, 350), frame_material="Carbon Fiber", fuel=27, fins=3)

# Test if rockets can achieve orbit
print("Rocket 1 can achieve orbit:", rocket1.can_achieve_orbit())
print("Rocket 2 can achieve orbit:", rocket2.can_achieve_orbit())
print("Rocket 3 can achieve orbit:", rocket3.can_achieve_orbit())
print("Rocket 4 can achieve orbit:", rocket4.can_achieve_orbit())
'''