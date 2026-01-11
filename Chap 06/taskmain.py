import celery_add_task  # Your Celery task module

def get_series_task(n):
    """
    Use Celery task to compute the first n Tribonacci numbers asynchronously.
    Returns an AsyncResult object.
    """
    return celery_add_task.get_tribonacci_series.delay(n)

if __name__ == '__main__':
    n = 10
    result = get_series_task(n)  # Returns AsyncResult
    print("Task submitted. Use result.get() to fetch the series when ready.")
    
    # Fetch the result (this will block until the task completes)
    series = result.get(timeout=10)  # Optional timeout to avoid indefinite waiting
    print("Tribonacci series:", series)
