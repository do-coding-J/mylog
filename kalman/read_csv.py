import csv

def read_csv(file_name):
    data = []
    with open(file_name, newline='\n') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            tmp = []
            for col in range(0, len(row)):
                if type(row[col]) != float:
                    tmp.append(row[col])
                else:    
                    tmp.append(float(row[col]))
            data.append(tmp)
            
    return data