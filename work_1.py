import random

def f(n):
    lst = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    if len(lst) != 0:
        return (sorted(set(lst)))
        
    if len(lst) == 0:
        symb.append(' ')
        return(f(n+1))     
    
print('Введите сообщение:')
ishod = str(input())
ishod = ishod.replace(" ","")
ishod = ishod.upper()
symb = list(ishod)
mn = f(len(symb))

a = random.choice(mn)

word = ''
for i in range(0,a):
    for y in range(0,len(symb),a):
        word += symb[i+y]   

print('Исходное сообщение:' + ishod )
print('Зашифрованное сообщение:' + word)
print('Количество строк равно:' + str(a))
print('Количество пробелов:' + str(len(symb)-len(ishod)))