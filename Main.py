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
thrust_range = (0.8e6, 2.4e6)  # Thrust in Newtons
mass_range = (1e5, 2.5e5)  # Mass in kg
isp_range = (160, 420)  # Specific impulse in seconds
material_options = ["Aluminum", "Steel", "Titanium", "Carbon Fiber"]
fuel_range = (0.8e4, 2.5e4)  # Fuel mass in kg
fin_options = (0,10)

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
#about 50% of these rockets with randomized parameters fail which is ideal
for rocket in rockets:
    print(f"Rocket: {rocket.name}")
    print("\n")
    print(rocket.can_achieve_orbit())
