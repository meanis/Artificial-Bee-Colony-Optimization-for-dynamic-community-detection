import networkx as nx
import matplotlib.pyplot as plt

from functions import locus_decode

def node_labeling(solution):
    
    labels = [0 for _ in range(len(solution))]
    partition = locus_decode(solution)

    label = 0
    for community in partition:
        for member in community:
            labels[member] = label
        label += 1

    return labels

def draw(snapshots, partitions, analysis_data):
    
    for moment in range(len(snapshots)):
        
        g = snapshots[moment]
        fs = partitions[moment]
        data = analysis_data[moment]

        pos = nx.spring_layout(g)
        labels = node_labeling(fs.solution)

        plt.title("network communities")

        nx.draw(g, pos=pos, with_labels=True, node_color=labels, node_size=80)
        
        plt.show()

        plt.plot(data['global optimal'])

        plt.show()