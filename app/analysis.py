import networkx as nx
import matplotlib.pyplot as plt

from functions import locus_decode
from functions import node_labeling

def draw(snapshots, partitions, analysis_data):

    for moment in range(len(snapshots)):

        g = snapshots[moment]
        fs = partitions[moment]
        snapshot_analysis_data = analysis_data[moment]

        pos = nx.spring_layout(g)
        labels = node_labeling(fs.solution)

        plt.figure('Résultat de la détection de communautés')
        plt.title('Les communautés du réseau social')

        nx.draw(g, pos=pos, with_labels=True, node_color=labels, node_size=80)
        plt.show()

        global_optimals = snapshot_analysis_data['global_optimal']
        plt.figure('Résultat de la détection de communautés')
        plt.title("Evolution de la qualité de la solution à travers les cycles de recherche")
        plt.bar(range(len(global_optimals)), global_optimals, width=0.1, color='green')
        plt.xlabel('cycle de recherche')
        plt.ylabel('coût de la meilleure solution trouvée')

        xMax = len(global_optimals)
        yMin = global_optimals[0]
        yMax = global_optimals[-1]

        plt.text(5, yMax, 'f: ' + str(yMax), style='oblique', bbox={'facecolor':'orange', 'alpha':0.5, 'pad':10})
        plt.axis([0, xMax + 1, yMin - 0.01, yMax + 0.01])
        plt.grid(True, which='both', axis='y')
        plt.show()