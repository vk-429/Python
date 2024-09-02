import logging

logging.basicConfig(level=logging.INFO)

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b, c=0):  # Adding a keyword argument `c`
    return a + b + c  # Now the result includes `c`

# Passing `a`, `b`, and `c` (a keyword argument)
my_function(2, 3, c=4)
