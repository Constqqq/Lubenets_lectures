

MY_CACHE:dict[int,int] = {0: 0, 1:1, 2:1}

def fibonacci(value:int) -> int :
    if value in MY_CACHE:
        return MY_CACHE[value]
    result = fibonacci(value - 1) +fibonacci(value - 2)
    MY_CACHE[value] = result
    return result
   
print(fibonacci(300))
