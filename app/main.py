import sys
import csv

from bcsa_dcd import bcsa_dcd
import read_configuration
import read_network
from write_results import write_results
import analysis as anal

def main(argv):

    params = read_configuration.read(argv[1])

    if argv[2] == 'static':
        snapshots = read_network.read_static_network(argv[3])
    elif argv[2] == 'dynamic':
        snapshots = read_network.read_dynamic_network(argv[3])

    with open('results.csv', 'w') as _file:
        writer = csv.writer(_file, lineterminator = '\n')
        writer.writerow([
            'nb_s',
            'nb_cycles',
            'limit_cycles',
            'employed_bees_percentage',
            'T0',
            'Tmin',
            'alpha',
            'cycles_per_t',
            'gamma',
            'sigma',
            'delta',
            ] + [
                f"Modularité of snapshot {i+1}" for i,v in enumerate(snapshots)
            ])

        for _ in range(int(params['nb_exec'])):
            print('execution number: ', (_ + 1))
            mobcsa_dcd_ = bcsa_dcd(params, snapshots)
            partitions, analysis_data = mobcsa_dcd_.execute()
            write_results(writer, params, analysis_data)

    anal.draw(snapshots, partitions, analysis_data)

if __name__ == '__main__':
    sys.exit(main(sys.argv))