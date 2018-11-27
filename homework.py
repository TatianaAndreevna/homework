operation = str(input('Введите значение: ((-, +, *, /) число_1 число_2):'))
result = operation.split()


def polish_notation(operation):
    try:
        assert float(result[1]) >= 0 and float(result[2]) >= 0, 'Введено отрицательное число!'
        if result[0] == '+':
            print(float(result[1]) + float(result[2]))
        elif result[0] == '-':
            print(float(result[1]) - float(result[2]))
        elif result[0] == '*':
            print(float(result[1]) * float(result[2]))
        elif result[0] == '/':
            try:
                print(float(result[1]) / float(result[2]))
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
        else:
            print('Ошибка')
    except AssertionError:
            print('Введено отрицательное число!')


polish_notation(operation)

