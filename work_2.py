ishod = input('Зашифрованное сообщение:')

ishod = ishod.upper()

symb = list(ishod)

a = int(input('Введите количество строк:'))

b = len(symb) // a

word = ''

for i in range(0,b):
    for y in range(0,len(symb),b):
        word += symb[i+y]   

print('Исходное сообщение:'+ ishod)
print('Расшифрованное сообщение:' + word)