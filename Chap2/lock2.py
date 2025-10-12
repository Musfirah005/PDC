import threading
import time
from threading import Thread
from random import randint
from Tribonacci1 import get_series  

# Global Lock
threadLock = threading.Lock()

class TribonacciThread(Thread):
    def __init__(self, name, n):
        Thread.__init__(self)
        self.name = name
        self.n = n

    def run(self):
        # Series calculation (lock ke bahar, parallel)
        series = get_series(self.n)
        
        # Print (critical section)
        threadLock.acquire()
        try:
            print(f"{self.name} output: {series}")
        finally:
            threadLock.release()
        
        # Simulate random duration task
        duration = randint(1, 5)
        time.sleep(duration)
        print(f"{self.name} finished after {duration} seconds")

def main():
    start_time = time.time()  # Start time

    threads = []
    num_threads = 5
    n = 10

    for i in range(num_threads):
        t = TribonacciThread(f"Thread#{i+1}", n)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads completed.")
    
    # Total execution time
    total_time = time.time() - start_time
    print(f"Total execution time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
