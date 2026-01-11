from celery import Celery

# Your broker URL is fine if RabbitMQ is running locally
app = Celery('tribonacciTask', broker='amqp://guest@localhost//')

@app.task
def get_tribonacci_series(n):
    """
    Return first n Tribonacci numbers as a list
    """
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
