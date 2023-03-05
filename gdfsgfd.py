import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time   {func.__name__}: {end_time - start_time} second")
        return result
    return wrapper

@calculate_time
def my_function():
    time.sleep(1)
    print("function my_function yes")

def test_calculate_time():
    start_time = time.time()
    my_function()
    end_time = time.time()
    assert end_time - start_time > 1.0
    print("Ok")

test_calculate_time()
