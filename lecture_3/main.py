print ('Загадай диапазон и число')
min = -10000
max = -9000
while True:
    mid = (min + max) // 2
    answer = input(f"ur numer </>/= {mid}")
    if answer == '=':
        print (f"ur number {mid}")
        break
    elif answer == '<':
        max = mid - 1
    elif answer == '>':
        min = mid + 1
    elif answer == 'exit':
        break
    else:
        print ('mimo')
    
    