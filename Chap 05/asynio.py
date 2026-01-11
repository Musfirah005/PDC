import asyncio

async def tribonacci_coroutine(future, n):
    """Coroutine to generate first n Tribonacci numbers."""
    if n <= 0:
        series = []
    else:
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
    # Simulate async work
    await asyncio.sleep(2)
    future.set_result(f'Tribonacci series for n={n}: {series}')


def got_result(future):
    print(future.result())


if __name__ == '__main__':
    # Ask user for input to avoid sys.argv errors
    n = int(input("Enter n for Tribonacci series: "))

    loop = asyncio.get_event_loop()
    future = asyncio.Future()

    task = tribonacci_coroutine(future, n)

    future.add_done_callback(got_result)

    loop.run_until_complete(asyncio.wait([task]))
    loop.close()
6