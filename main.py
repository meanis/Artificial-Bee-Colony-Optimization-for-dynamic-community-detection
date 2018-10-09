import sys

from mobcsa_dcd import mobcsa_dcd
import read_configuration
import read_network
import analysis as anal

def main(argv):
    
    if len(argv) < 4:
        sys.stderr.write("Usage: python main.py params_file_path params_file_delimiter network_file_path network_file_delimiter")
        return 1
    
    params = read_configuration.read(argv[1], argv[2])
    snapshots = read_network.read(argv[3], argv[4], params['snapshot_step'])
    
    mobcsa_dcd_ = mobcsa_dcd(params, snapshots)
    partitions, analysis_data = mobcsa_dcd_.execute()

    anal.draw(snapshots, partitions, analysis_data)

if __name__ == '__main__':
    sys.exit(main(sys.argv))