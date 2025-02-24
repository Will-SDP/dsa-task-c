# These are examples of auxiliary methods for your guidance
from random import randint
import csv 
import datetime
import json 

def generate_dataset(n, max=1000000):
    dataset = []
    for i in range(0, n):
        random_number = randint(0, max)
        dataset.append(random_number)

    return dataset    

def write_result(result):
    '''
    Writes results to a csv file. Example input dataa 

    data = [
        {'Execution time': 2, 'function': 'bubble_sort()', 'dataset': ' '.join([str(s) for s in [1,2,3]])}
    ]

    '''
    d = datetime.datetime.today()
    file_name = f"Expermiments-{d.strftime("%H")}-{d.strftime("%M")}_{d.strftime("%d")}-{d.strftime("%m")}-{d.strftime("%Y")}.csv"
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['Execution time', 'function', 'dataset']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def write_dataset(data, file_name):
    '''
    Takes a dictionary containing a data set and writes it to a json file. 
    Example dictionary 

    my_dict = {
        "name": "My dataset", 
        "data": [1,2,3,4,5]
    }

    '''
    content = json.dumps(data, indent=2)
    with open(file_name, "w") as out_file:
        out_file.write(content)

def read_dataset(file_name):
    with open(file_name, 'r') as open_file:
        obj = json.load(open_file)
    return obj 








