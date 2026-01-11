import asyncio
import sys

# Modern async function
async def tribonacci_coroutine(n):
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
    await asyncio.sleep(2)  # simulate async delay
    return series

async def main(n1, n2):
    # Run both coroutines concurrently
    results = await asyncio.gather(
        tribonacci_coroutine(n1),
        tribonacci_coroutine(n2)
    )
    for series in results:
        print(f"Tribonacci series: {series}")

if __name__ == '__main__':
    n1 = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    n2 = int(sys.argv[2]) if len(sys.argv) > 2 else 7

    # Modern way to run asyncio code
    asyncio.run(main(n1, n2))
