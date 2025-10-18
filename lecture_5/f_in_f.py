def print_to_console(init_value: int):
    print(init_value)
    print('Hello')


def inc_by_10(value:10) -> int:
    value +=10
    return value   


def no_return(value:int) -> int | None:
    if value % 2 ==0:
        value *=10
        if value == 20:
            return
        else:
            return value
    

def rec(x:int) -> int:
    print(x)
    x+= 1
    if x <100:
        rec(x)
    return x









