def fibonacci(value:int):
    if value <= 1:
        return value
    result = fibonacci(value - 1) +fibonacci(value - 2)
    return result
   
print(fibonacci())