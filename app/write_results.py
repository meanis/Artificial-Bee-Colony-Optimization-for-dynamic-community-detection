import csv

def write_results(writer, params, analysis_data):
        writer.writerow([
            params['nb_s'],
            params['nb_cycles'],
            params['limit_cycles'],
            params['employed_bees_percentage'],
            params['T0'],
            params['Tmin'],
            params['alpha'],
            params['cycles_per_t'],
            params['gamma'],
            params['sigma'],
            params['delta'],
            ] + [
                snapshot_analysis_data['global_optimal'][-1] for snapshot_analysis_data in analysis_data
            ])