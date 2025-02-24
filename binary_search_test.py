import time
import helpers
from binary_search import binary_search
from random import randint


def run_experiment():
    # Define a large dataset 
    dataset = helpers.generate_dataset(10000000)
    index = randint(0, 999999)   
    target = dataset[index]
    print("Binary Search")
    start = time.thread_time_ns()
    binary_search(target, dataset)
    end = time.thread_time_ns()
    duration_nano = (end - start)/100000
    print("Binary Search: ",duration_nano)     

run_experiment()    