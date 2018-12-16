import sys

from mobcsa_dcd import mobcsa_dcd
import read_configuration
import read_network
import analysis as anal

def main(argv):
    
    params = read_configuration.read(argv[1], argv[2])

    if argv[3] == 'static':
        snapshots, groundtruth_communities = read_network.read_static_network(argv[4], argv[5])
    elif argv[3] == 'lfr':
        snapshots, groundtruth_communities = read_network.read_lfr_benchmark_network()
    elif argv[3] == 'dynamic':
        snapshots, groundtruth_communities = read_network.read_dynamic_network(argv[4], argv[5])
    elif argv[3] == 'temporal':
        snapshots, groundtruth_communities = read_network.read_temporal_network(argv[4], argv[5], params['snapshot_step'], params['snapshot_overlap'])

    mobcsa_dcd_ = mobcsa_dcd(params, snapshots)
    partitions, analysis_data = mobcsa_dcd_.execute()

    anal.draw(snapshots, partitions, analysis_data)

if __name__ == '__main__':
    sys.exit(main(sys.argv))