print('Введите первое число')
a = int(input())
print('Введите операцию')
c = str(input())
print('Введите второе число')
b = int(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b != 0:
        print(a / b)
    else:
        print('Ошибка! На 0 делить нельзя!')
else:
    print('Ошибка! Нет такой операции!')