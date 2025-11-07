4-pipe.py 

this program shows inter-process communication (IPC) using multiprocessing.Pipe.
One process (generate_series) generates the Tribonacci series and sends each number through the pipe, while the second process (receive_series) receives and prints the numbers.

A duplex pipe connects the two processes: the first sends data, and the second continuously reads it until the pipe is closed, raising an EOFError.
The main process creates both child processes, closes its own pipe ends, and waits for them to finish using join().

This example shows process-based parallelism, where data is passed between processes without shared memory. It highlights how Pipe enables direct, synchronized communication between independent processes.


5- queue.py

This program shows inter-process communication using the multiprocessing.Queue through a Producer–Consumer model.
The producer process generates a specified number of Tribonacci numbers using the Tribonacci.get_series() function and places each number into the shared queue,
displaying messages about the produced items and current queue size.
The consumer process simultaneously retrieves and removes items from the queue, printing the consumed values until the queue becomes empty. 
Random sleep intervals are used in both processes to simulate asynchronous execution. 
The main program initializes the shared queue, creates one producer and one consumer process, starts them, and waits for their completion.
 This implementation effectively illustrates how processes can communicate and synchronize safely using queues in Python’s multiprocessing environment.

6- processlifecycle.py

This program shows process creation, execution, and termination using the multiprocessing module. 
It defines a worker function, tribonacci_worker(), which generates and prints the Tribonacci series for a given number of terms using the Tribonacci.get_series() 
function, pausing briefly between outputs to simulate time-consuming computation. In the main program, a separate process is created to run this worker function, 
and its state is displayed before, during, and after execution using is_alive(). The program allows the process to run for a few seconds before explicitly terminating 
it with terminate(), then ensures cleanup with join(). Finally, it prints the process’s exit status, effectively illustrating how to start, monitor, stop, and manage
independent processes in Python’s multiprocessing environment.

7- barrier.py

This program shows the process synchronization using multiprocessing.Barrier and Lock.
Two processes use a barrier to start together, ensuring they print the Tribonacci series at the same time, while two others run independently without synchronization. 
The Lock ensures that output from different processes doesn’t overlap, keeping the printed results clear.
By comparing synchronized and unsynchronized processes, the program shows how barriers coordinate process execution and locks manage shared output safely.


