import sys

from mobcsa_dcd import mobcsa_dcd
import read_configuration
import read_network
import analysis as anal

def main(argv):

    params = read_configuration.read(argv[1])

    if argv[2] == 'static':
        snapshots = read_network.read_static_network(argv[3])
    elif argv[2] == 'dynamic':
        snapshots = read_network.read_dynamic_network(argv[3])

    mobcsa_dcd_ = mobcsa_dcd(params, snapshots)
    partitions, analysis_data = mobcsa_dcd_.execute()

    anal.draw(snapshots, partitions, analysis_data)

if __name__ == '__main__':
    sys.exit(main(sys.argv))

'''
def groundTruth(dataset):
    labels=[]
    if(dataset=="karate"):
        labels=[0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1]
    if(dataset=="dolphins"):
        labels=[0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0]
    if(dataset=="football"):
        labels=[7,0,2,3,7,3,2,8,8,7,3,10,6,2,6,2,7,9,6,1,9,8,8,7,10,0,6,9,11,1,1,6,2,0,6,1,5,0,6,2,3,7,5,6,4,0,11,2,4,11,10,8,3,11,6,1,9,4,11,10,2,6,9,10,2,9,4,11,8,10,9,6,3,11,3,4,9,8,8,1,5,3,5,11,3,6,4,9,11,0,5,4,4,7,1,9,9,10,3,6,2,1,3,0,7,0,2,3,8,0,4,8,4,9,11]
    if(dataset=="polbooks"):
        labels=[0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,2,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0]
    return labels
'''