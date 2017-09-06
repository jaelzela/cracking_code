import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
        self.intermediate.setdefault(key, [])       
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print item

mapReducer = MapReduce()

def mapper(record):
    row = record.strip().split(',')
    if row[0] == 'Department':
        key = row[1].strip()
        value = row[2]
        label = 'd'
    else:
        key = row[2].strip()
        value = row[1]
        label = 'n'
    mapReducer.emitIntermediate(key, (label, value))
    

def reducer(key, list_of_values):
    depts = []
    names = []
    for label, element in list_of_values:
        if label == 'd':
            depts.append(element)
        else:
            names.append(element)
            
    for n in names:
        for d in depts:
            mapReducer.emit((key, n, d))
    
            
if __name__ == '__main__':
    inputData = []
    for line in sys.stdin:
        inputData.append(line)
    mapReducer.execute(inputData, mapper, reducer)

