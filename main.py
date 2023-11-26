from random import randint


while True:
    print('Изучение степеней')
    a = int(input('От какого числа: '))
    b = int(input('До какого числа: '))
    c = int(input('Какая степень: '))
    stp = int(input("До какого счёта: "))
    plus = int(input("Сколько прибавлять за правильный ответ: "))
    minus = int(input("Сколько вычетать за неправильный ответ: "))
    print('Вводи только ответы (числа)')
    s = 0
    while s < stp:
        d = randint(a, b)
        print('Сколько будет', d, '^', c, ': ')
        e = int(input())
        if e == d ** c:
            s += plus
            print('Правильно!', end='\n\n\n')
        else:
            print('Кажется неправильно :(')
            print('Правильный ответ: ', d ** c)
            s -= minus
        print("Счёт:", s, end='\n\n\n')
    print("Поздравляю!!!")
    print("Вы достигли счета", s)
    print("--- Игра окончена ---")
    n = int(input("Введите 1, чтобы продолжить"))
    if n == 1:
        continue
    else:
        exit()
        
