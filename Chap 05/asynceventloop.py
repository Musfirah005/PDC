import asyncio

async def task_A(n, series):
    """Generate Tribonacci numbers asynchronously in a round-robin style"""
    print("task_A called")
    await asyncio.sleep(0.1)  # non-blocking sleep
    if len(series) < n:
        next_num = sum(series[-3:]) if len(series) >= 3 else sum(series)
        series.append(next_num)
        await task_B(n, series)

async def task_B(n, series):
    print("task_B called")
    await asyncio.sleep(0.1)
    if len(series) < n:
        next_num = sum(series[-3:]) if len(series) >= 3 else sum(series)
        series.append(next_num)
        await task_C(n, series)

async def task_C(n, series):
    print("task_C called")
    await asyncio.sleep(0.1)
    if len(series) < n:
        next_num = sum(series[-3:]) if len(series) >= 3 else sum(series)
        series.append(next_num)
        await task_A(n, series)

async def main(n):
    # start the series with the initial three Tribonacci numbers
    series = [0, 1, 1][:n]
    await task_A(n, series)
    print("Final Tribonacci series:", series)

# Run the async loop
n = 10  # generate first 10 numbers
asyncio.run(main(n))

