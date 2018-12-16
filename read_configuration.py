import csv

def read(file_, delimiter_):
    
    params = {}
    
    with open(file_) as file:
        reader = csv.reader(file, delimiter=delimiter_)

        for line in reader:
            params[line[0]]=float(line[1])
    
    return params