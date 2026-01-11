from mpi4py import MPI

def get_series(n):
    """Return first n Tribonacci numbers as a list"""
    if n <= 0:
        return []
    a, b, c = 0, 1, 1
    series = [a]
    if n > 1:
        series.append(b)
    if n > 2:
        series.append(c)
    for _ in range(3, n):
        next_num = a + b + c
        series.append(next_num)
        a, b, c = b, c, next_num
    return series

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.rank

# Each process sends/receives Tribonacci data
if rank == 0:
    # Process 0 computes first 10 Tribonacci numbers
    data = get_series(10)
    destination_process = 4
    comm.send(data, dest=destination_process)
    print(f"Process {rank} sending data {data} to process {destination_process}")

if rank == 1:
    # Process 1 computes first 15 Tribonacci numbers
    data = get_series(15)
    destination_process = 8
    comm.send(data, dest=destination_process)
    print(f"Process {rank} sending data {data} to process {destination_process}")

if rank == 4:
    # Process 4 receives data from process 0
    data = comm.recv(source=0)
    print(f"Process {rank} received data: {data}")

if rank == 8:
    # Process 8 receives data from process 1
    data = comm.recv(source=1)
    print(f"Process {rank} received data: {data}")
