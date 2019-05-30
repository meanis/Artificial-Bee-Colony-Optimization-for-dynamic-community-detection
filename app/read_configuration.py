import csv

def read(file_):
    
    params = {}
    
    with open(file_) as file:
        reader = csv.reader(file, delimiter=':')

        for line in reader:
            params[line[0]]=float(line[1])
    
    return params