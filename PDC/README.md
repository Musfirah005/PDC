# PDC
Chapter 01 code

First, we created a file named Tribonacci.py that calculates the Tribonacci series and stores the generated numbers in a list.This file is then imported into the Main.py file, where the Tribonacci series is executed in three different ways:
Normal Run: calculated normally without using threading or multiprocessing.
Threaded Run: calculated using multiple threads.
Process Run: calculated using multiple processes.
The program measures the execution time for each method and displays the time taken for all three approaches in the output.

The results show that the normal and threaded runs executed almost instantly because the task size was small, while the process run took longer due to the overhead of creating separate processes. This indicates that multiprocessing is beneficial only for larger or more complex computations, whereas for smaller tasks, normal or threaded execution is faster and more efficient.