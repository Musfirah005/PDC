import threading
import time
from threading import Thread
from Tribonacci1 import get_series  

# Global Lock
threadLock = threading.Lock()

class Tribonacci1Thread(Thread):
    def __init__(self, name, n):
        Thread.__init__(self)
        self.name = name
        self.n = n

    def run(self):
        start = time.time()
        print(f"{self.name} started at {start:.2f} seconds")

        # Acquire the lock
        threadLock.acquire()
        try:
            series = get_series(self.n)
            print(f"{self.name} output: {series}")
        finally:
            # Release the lock
            threadLock.release()

        end = time.time()
        print(f"{self.name} finished at {end:.2f} seconds")

def main():
    start_time = time.time()  # Start time for total execution

    threads = []
    num_threads = 5  # Total threads
    n = 10           # Number of Tribonacci numbers

    # Thread creation
    for i in range(num_threads):
        t = Tribonacci1Thread(f"Thread#{i+1}", n)
        threads.append(t)
        t.start()

    # Thread joining
    for t in threads:
        t.join()

    print("All threads completed.")

    # Total execution time
    total_time = time.time() - start_time
    print(f"Total execution time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()
