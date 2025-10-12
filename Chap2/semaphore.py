import logging
import threading
import time
from Tribonacci1 import get_series
from random import randint

# Logging format
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared resource
series = []
n = 10

# Semaphore
sem = threading.Semaphore(0)

def consumer():
    logging.info("Consumer is waiting for series")
    sem.acquire()  # Wait for producer
    logging.info(f"Consumer received series: {series}")

def producer():
    global series
    time.sleep(randint(1, 3))  # Simulate work
    series = get_series(n)
    logging.info(f"Producer generated series: {series}")
    sem.release()  # Notify consumer

def main():
    threads = []
    num_iterations = 5  # Number of produce-consume cycles

    for i in range(num_iterations):
        t_cons = threading.Thread(target=consumer, name=f"ConsumerThread#{i+1}")
        t_prod = threading.Thread(target=producer, name=f"ProducerThread#{i+1}")

        threads.append(t_cons)
        threads.append(t_prod)

        t_cons.start()
        t_prod.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    logging.info("All threads completed.")

if __name__ == "__main__":
    main()
