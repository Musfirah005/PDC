import multiprocessing
import time
import Tribonacci
import random

# ---------- Producer Process ----------
class Producer(multiprocessing.Process):
    def __init__(self, queue, n):
        super().__init__()
        self.queue = queue
        self.n = n

    def run(self):
        series = Tribonacci.get_series(self.n)
        for num in series:
            self.queue.put(num)
            print(f"Process Producer : item {num} appended to queue {self.name}")
            time.sleep(random.uniform(0.5, 1.2))
            print(f"The size of queue is {self.queue.qsize()}")
        print(f"{self.name} finished producing.\n")


# ---------- Consumer Process ----------
class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print("the queue is empty")
                break
            else:
                time.sleep(random.uniform(1.0, 1.5))
                item = self.queue.get()
                print(f"Process Consumer : item {item} popped from by {self.name}\n")
                time.sleep(random.uniform(0.3, 0.6))


# ---------- Main Program ----------
if __name__ == "__main__":
    n = 10  # number of Tribonacci numbers
    queue = multiprocessing.Queue()

    producer = Producer(queue, n)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
