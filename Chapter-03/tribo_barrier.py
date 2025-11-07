import multiprocessing
from multiprocessing import Barrier, Lock, Process
from datetime import datetime
from time import time, sleep
import Tribonacci  


# with barrier 
def tribonacci_with_barrier(synchronizer, serializer, n):
    """Each process waits for others, then prints the Tribonacci series."""
    name = multiprocessing.current_process().name

    synchronizer.wait()

    now = datetime.fromtimestamp(time())

    series = Tribonacci.get_series(n)

    # Use lock to prevent mixed output
    with serializer:
        print(f"\n{name} ----> Started at {now}")
        print(f"{name} Tribonacci({n}) series: {series}")
        print(f"{name} ----> Finished printing\n")
        sleep(0.5)


# without barrier 
def tribonacci_without_barrier(n):
    """Each process runs independently (no synchronization)."""
    name = multiprocessing.current_process().name
    now = datetime.fromtimestamp(time())
    series = Tribonacci.get_series(n)
    print(f"\n{name} ----> Started at {now}")
    print(f"{name} Tribonacci({n}) series: {series}")
    print(f"{name} ----> Finished printing\n")
    sleep(0.5)


if __name__ == "__main__":
    n = 10  # number of Tribonacci terms

    synchronizer = Barrier(2)  
    serializer = Lock()        

    # Two processes that synchronize with barrier
    Process(name='p1 - tribonacci_with_barrier',
            target=tribonacci_with_barrier,
            args=(synchronizer, serializer, n)).start()

    Process(name='p2 - tribonacci_with_barrier',
            target=tribonacci_with_barrier,
            args=(synchronizer, serializer, n)).start()

    # Two processes without synchronization
    Process(name='p3 - tribonacci_without_barrier',
            target=tribonacci_without_barrier,
            args=(n,)).start()

    Process(name='p4 - tribonacci_without_barrier',
            target=tribonacci_without_barrier,
            args=(n,)).start()
