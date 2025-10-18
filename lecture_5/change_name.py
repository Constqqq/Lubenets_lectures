def change_name(name:str, registr) -> str:
    symbols: list[str] = []
    for symbol in name:
        symbols += symbol.lower()
    for i in range(len(symbols)):
        if registr == 'нечёт':
            if  (i+2)%2 == 0:
                symbols[i] = symbols[i].upper()
        elif registr == 'чёт':
            if  not i%2 == 0:
                symbols[i] = symbols[i].upper()   
        else:
            print('Error')
    name = ''.join(symbols)
    return name
    

name = input('Введите имя')
registr = input('Чёт/Нечёт').lower()
print(change_name(name,registr))