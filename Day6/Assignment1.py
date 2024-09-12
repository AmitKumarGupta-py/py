import logging
import time
from functools import wraps


logging.basicConfig(filename='decoratorExampleLog.log', level=logging.INFO)

def log_function_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Function {func.__name__} was called")
        return func(*args, **kwargs)
    return wrapper

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Function {func.__name__} took {execution_time} seconds to execute")
        return result
    return wrapper


@log_function_name
@log_execution_time
def example_function():
    time.sleep(1)  

example_function()
