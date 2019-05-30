import sys

from bcsa_dcd import bcsa_dcd
import read_configuration
import read_network
import analysis as anal

def main(argv):

    params = read_configuration.read(argv[1])

    if argv[2] == 'static':
        snapshots = read_network.read_static_network(argv[3])
    elif argv[2] == 'dynamic':
        snapshots = read_network.read_dynamic_network(argv[3])

    mobcsa_dcd_ = bcsa_dcd(params, snapshots)
    partitions, analysis_data = mobcsa_dcd_.execute()

    anal.draw(snapshots, partitions, analysis_data)

if __name__ == '__main__':
    sys.exit(main(sys.argv))