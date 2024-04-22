import numpy as np
from Rocket import Rocket

# Define the parameters for 10 real rockets
rockets_data = [
    {"name": "Falcon 9", "thrust": 7607e3, "mass": [549054, 549054 + 10188], "nozzle": [282, 348], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 4},
    {"name": "Saturn V", "thrust": 35080e3, "mass": [2970000, 2970000 + 127000], "nozzle": [265, 421], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 0},
    {"name": "Space Shuttle", "thrust": 30e6, "mass": [2040000, 2040000 + 86000], "nozzle": [450, 450], "frame_material": "Aluminum", "fuel": "SRBs/LOX/LH2", "fins": 0},
    {"name": "Delta IV Heavy", "thrust": 9631e3, "mass": [733000, 733000 + 28550], "nozzle": [275, 370], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 0},
    {"name": "Atlas V 401", "thrust": 4152e3, "mass": [334000, 334000 + 10100], "nozzle": [311, 410], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 0},
    {"name": "Ariane 5", "thrust": 13720e3, "mass": [777000, 777000 + 20380], "nozzle": [434, 431], "frame_material": "Aluminum", "fuel": "H2/LOX", "fins": 0},
    {"name": "H-IIA 202", "thrust": 1250e3, "mass": [285000, 285000 + 13400], "nozzle": [442, 460], "frame_material": "Aluminum", "fuel": "H2/LOX", "fins": 0},
    {"name": "Long March 2D", "thrust": 2960e3, "mass": [401000, 401000 + 14200], "nozzle": [270, 293], "frame_material": "Aluminum", "fuel": "N2O4/UDMH", "fins": 0},
    {"name": "Vega", "thrust": 2200e3, "mass": [137000, 137000 + 7350], "nozzle": [295, 318], "frame_material": "Aluminum", "fuel": "Solid", "fins": 0},
    {"name": "Soyuz-2.1b", "thrust": 4220e3, "mass": [308000, 308000 + 7150], "nozzle": [311, 330], "frame_material": "Aluminum", "fuel": "RP-1/LOX", "fins": 0},
]

# Simulate flights for each rocket
for rocket_data in rockets_data:
    rocket = Rocket(rocket_data["name"], rocket_data["thrust"], rocket_data["mass"], rocket_data["nozzle"],
                    rocket_data["frame_material"], rocket_data["fuel"], rocket_data["fins"])
    print(f"Simulating flight of {rocket_data['name']}...")
    rocket.simulate_flight()
    print("=" * 50)