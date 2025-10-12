1-lock.py

Multiple threads generate Tribonacci series.
threadLock.acquire() allows a thread to hold the lock for print and calculation.
The series is calculated and printed, then threadLock.release() gives the lock to the next thread. All threads join and total execution time is printed. Threads run sequentially for printing, but series calculation happens inside the lock.

2-lock2.py

Multiple threads generate Tribonacci series in parallel.
In this code, only printing is done inside the lock and calculation happens in parallel.
Each thread calculates get_series(n) outside the lock, then threadLock.acquire() ensures the print statement is thread-safe. Random sleep simulates task duration, and finish is printed. All threads join and total execution time is printed.
Faster than the first code because calculation is parallel and the lock is only for the critical section. Random duration simulates realistic threaded tasks.

3-semaphore.py

Demonstrates the Producer-Consumer problem using a semaphore, where the producer generates Tribonacci series and the consumer waits for it. The semaphore is initialized with 0, and the consumer waits until the producer releases. The producer calculates the series and uses sem.release(), then the consumer wakes up. The consumer prints the received series using sem.acquire(), ensuring proper synchronization. Multiple produce-consume cycles run with threads, and the semaphore coordinates execution order between producer and consumer.

Ensures the consumer never prints the series before it is generated.
