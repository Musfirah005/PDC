import multiprocessing
import time
import Tribonacci  

def tribonacci_worker(n):
    print("Starting Tribonacci process...")
    series = Tribonacci.get_series(n)
    for i, num in enumerate(series):
        print(f"Tribonacci[{i}] = {num}")
        time.sleep(1)  
    print("Finished generating Tribonacci series.")

if __name__ == "__main__":
    n = 10  # number of terms in the Tribonacci series

    p = multiprocessing.Process(target=tribonacci_worker, args=(n,))

    print("Process before execution:", p, p.is_alive())

    p.start()
    print("Process running:", p, p.is_alive())

    time.sleep(3)
    p.terminate()
    print("Process terminated:", p, p.is_alive())

    p.join()
    print("Process joined:", p, p.is_alive())

    print("Process exit code:", p.exitcode)
