import time

from functools import lru_cache
# @lru_cache()
# def calculate_surname1(age:int, name: str = 'Vova') -> str:
#     print('Wait 5 seconds')
#     time.sleep(5)
#     return f'Hello {name} ({age} y.o.)'


# if __name__ == '__main__':
#     print(calculate_surname1(18, 'Andrey'))




MY_CACHE:dict[str,str] = {}    
def my_calculate_surname(name:str = "ZoVa"):
    if name in MY_CACHE:
        return MY_CACHE[name]
    time.sleep(5)
    surname = "ZoVa" + "4kin"
    MY_CACHE[name] = surname
    return surname

print(my_calculate_surname())
print(my_calculate_surname())
print(my_calculate_surname())
print(my_calculate_surname())
print(my_calculate_surname())
