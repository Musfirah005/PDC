# main_pipe.py
import multiprocessing
import Tribonacci


def generate_series(pipe_conn, n):
    """Generate Tribonacci series and send each number via pipe"""
    output_conn, _ = pipe_conn
    series = Tribonacci.get_series(n)
    for num in series:
        output_conn.send(num)
    output_conn.close()


def receive_series(pipe_conn):
    """Receive and display numbers from the pipe"""
    _, input_conn = pipe_conn
    try:
        while True:
            num = input_conn.recv()
            print("Received:", num)
    except EOFError:
        print("End of series")


if __name__ == "__main__":
    n = 10  # number of terms

    # Create a duplex pipe
    pipe_conn = multiprocessing.Pipe(True)

    # Create two processes: one for generating, one for receiving
    p1 = multiprocessing.Process(target=generate_series, args=(pipe_conn, n))
    p2 = multiprocessing.Process(target=receive_series, args=(pipe_conn,))

    # Start both
    p1.start()
    p2.start()

    # Close parent references
    pipe_conn[0].close()
    pipe_conn[1].close()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("Tribonacci Pipe Communication Complete")
