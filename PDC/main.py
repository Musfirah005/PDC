import time
import threading
import multiprocessing
import Tribonacci


# ---------- Helper Function for Process ----------
def run_process(results, idx, n):
    results[idx] = Tribonacci.get_series(n)


# ---------- Run Functions ----------
def normal_run(n):
    start = time.time()
    series = Tribonacci.get_series(n)
    end = time.time()
    exec_time_ns = (end - start) * 1_000_000_000
    print(f"Normal Run -> Numbers added in the list | Execution Time: {int(exec_time_ns)} ns")
    return series


def thread_run(n, num_threads):
    results = [None] * num_threads
    threads = []
    start = time.time()
    for i in range(num_threads):
        t = threading.Thread(target=lambda idx=i: results.__setitem__(idx, Tribonacci.get_series(n)))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    exec_time_ns = (end - start) * 1_000_000_000
    print(f"Threaded Run -> Numbers added in the list | Execution Time: {int(exec_time_ns)} ns")
    return results


def process_run(n, num_processes):
    manager = multiprocessing.Manager()
    results = manager.list([None] * num_processes)
    processes = []
    start = time.time()

    for i in range(num_processes):
        p = multiprocessing.Process(target=run_process, args=(results, i, n))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    exec_time_ns = (end - start) * 1_000_000_000
    print(f"Process Run -> Numbers added in the list | Execution Time: {int(exec_time_ns)} ns")
    return list(results)


# ---------- Main ----------
if __name__ == "__main__":
    n = 10
    num_threads = 5
    num_processes = 5

    normal_run(n)
    thread_run(n, num_threads)
    process_run(n, num_processes)
