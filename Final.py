import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


## hyper resevoir design including potential futuristic computers

G = nx.heptagon_graph()
pos = nx.spectral_layout(G, dim=3)

#positions of different nodes on the network
nodes = ["Quantum", "Optical", "Bio", "ASIC 1", "GPU 1", "CPU 1", "ASIC 2"]
edges = [("Quantum", "Optical"), ("Quantum", "Bio"), ("ASIC 1", "Quantum"), ("ASIC 1", "Bio"),
         ("GPU 1, Quantum"), ("GPU 1, Bio"), ("CPU 1", "GPU 1"), ("GPU 1", "ASIC 1"), ("ASIC 2", "Bio"), ("ASIC 2", "Optical")]
#don't need method edges since those were specific to the rocekt class
pos = {"Quantum": (0,0,3), "Optical": (1,0,0), "Bio": (0,1,0), "ASIC 1": (1,1,0), "GPU 1": (1,1,1), "CPU 1": (2,1,0), "ASIC 1": (1,2,1)}

nodes = np.array([pos[v] for v in G])
edges = np.array([(pos[u], pos[v]) for u, v in G.edges()])
plt.show()


def init():
    ax.scatter(*nodes.T, alpha=0.2, s=100, color="blue")
    for vizedge in edges:
        ax.plot(*vizedge.T, color="gray")
    ax.grid(False)
    ax.set_axis_off()
    plt.tight_layout()
    return


def _frame_update(index):
    ax.view_init(index * 0.2, index * 0.5)
    return


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ani = animation.FuncAnimation(
    fig,
    _frame_update,
    init_func=init,
    interval=50,
    cache_frame_data=False,
    frames=100,
)



#hyper resevoir with just modern computers. Same structure


