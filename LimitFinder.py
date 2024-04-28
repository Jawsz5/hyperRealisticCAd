import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes for rocket components
components = [
    "Rocket", "Thrust", "Mass", "Nozzle", "Fuel Mass", 
    "Frame Material", "Fins", "Orbit"
]
G.add_nodes_from(components)

# Add edges representing influences and dependencies
edges = [
    ("Thrust", "Orbit"),
    ("Mass", "Orbit"),
    ("Nozzle", "Orbit"),
    ("Fuel Mass", "Orbit"),
    ("Frame Material", "Orbit"),
    ("Fins", "Orbit"),
    ("Fuel Mass", "Mass")
]
G.add_edges_from(edges)

# Add edges representing how components affect rocket methods
method_edges = [
    ("Thrust", "propulsion"),
    ("Mass", "propulsion"),
    ("Nozzle", "propulsion"),
    ("Fuel Mass", "propulsion"),
    ("Frame Material", "heat_change"),
    ("Frame Material", "temperature_change"),
    ("Fins", "heat_change"),
    ("Fins", "temperature_change"),
    ("Thrust", "delta_V"),
    ("Nozzle", "delta_V"),
    ("Mass", "delta_V"),
    ("Fuel Mass", "delta_V"),
    ("Frame Material", "can_achieve_orbit"),
    ("Fins", "can_achieve_orbit")
]
G.add_edges_from(method_edges)

# Specify positions for better visualization
pos = {
    "Rocket": (0, 0),
    "Thrust": (1, 1),
    "Mass": (1, 0),
    "Nozzle": (1, -1),
    "Fuel Mass": (2, 1),
    "Frame Material": (2, 0),
    "Fins": (2, -1),
    "Orbit": (3, 0)
}

# Draw the graph
plt.figure(figsize=(12, 8))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="skyblue")

# Draw edges
nx.draw_networkx_edges(G, pos, arrows=True, width=1.5, alpha=0.5, edge_color="gray")

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

plt.title("Rocket Components Network")
plt.axis("off")
plt.show()