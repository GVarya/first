order = [1, 2, 3, 2, 4]


def reader():
    a = int(input())
    return(a)



def reader_and_cheker(order):
    """
    получает на вход order(порядок загаданный компьютером)
    поочерёдно считывает ходы пользователя и сравнивает с order
    как только пользователь нажимает на неправильную кнопку, функция
    возвращает False и программа начинает игру с начала.
    """
    for i in order:
        hod = reader()
        if hod != i:
            return(False)
    return(True)



print(reader_and_cheker(order))