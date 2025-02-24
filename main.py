import time
from bubble_sort_algorithm import bubble_sort
from binary_tree import Binary_Tree
import helpers
import sys 

sys.setrecursionlimit(3000000)

# Use this code as guidance to conduct your experiment.
# Design and write your experiment program in methods and call them to run the experiment.

def experiment():
    print("running experiment", end="")
    for i in range(6):
        dataset = helpers.generate_dataset(10)
        bubble_sort(dataset)
    print()

def run_experiment():
    dataset = helpers.generate_dataset(1000)
    print("Performing bubble sort")
    start = time.thread_time_ns()
    #bubble_sort(dataset)
    end = time.thread_time_ns()
    duration_nano = (end - start)/100000
    print("Bubble Sort Duration: ",duration_nano)

    print("Performing BST sort")
    start = time.thread_time_ns()
    bst = Binary_Tree()
    bst.create_tree(dataset)
    bst.in_order()  
    end = time.thread_time_ns()
    duration_nano = (end - start)/100000
    print("BST Sort Duration: ",duration_nano)    


def run_sample_experiment(no_experiments):
    for i in range(no_experiments):
        print("Experiment #", i+1)
        run_experiment()
        #bst_experiment()

def bst_experiment():
    dataset = helpers.generate_dataset(5000000)
    print("Performing BST sort")
    start = time.thread_time_ns()
    bst = Binary_Tree()
    bst.create_tree(dataset)
    bst.in_order()  
    end = time.thread_time_ns()
    duration_nano = (end - start)/100000
    print("BST Sort Duration: ",duration_nano)     


def main():
    run_sample_experiment(1)
    

if __name__ == "__main__":
    main()
