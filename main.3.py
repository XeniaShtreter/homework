a = int(input('Введите продолжительность в секундах '))
if a < 60:
    print(str(a) + 'c')
elif 60 <= a < 3600:
    m = a // 60
    c = a % 60
    print(str(m) + 'm ' + str (c) + 'c')
elif 3600 <= a < 86400:
    h = (a // 60) // 24
    m = (a // 60) % 60
    c = a % 60
    print(str(h) + 'h ' + str(m) + 'm ' + str(c) + 'c')
elif a >= 86400:
    d = (a // 3600) // 24
    h = (a // 60) % 24
    m = (a // 60) % 60
    c = a % 60
    print(str(d) + 'd ' + str(h) + 'h ' + str(m) + 'm ' + str(c) + 'c')