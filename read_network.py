import csv
import networkx as nx

def read(file_, delimiter_, snapshot_step):
    
    snapshots = []

    with open(file_) as file:

        reader = csv.reader(file, delimiter=delimiter_)

        if(snapshot_step == -1):    #static network file
            
            g = nx.Graph()

            for line in reader:
                g.add_edge(line[0], line[1])
            
            g = nx.convert_node_labels_to_integers(g)
            snapshots.append(g)
        
        else:   #dynamic network file
            return snapshots
    
    return snapshots