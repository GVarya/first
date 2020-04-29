

def main():
    level = 1
    r = 3
    while True:
        polerisovalka(level)  #рисует поле с уровнем который передаётся в качестве i
        movecreator(r)  #  генерирует последовательность нажатия из r количества кнопок и возвращает последовательность order
        shower(order)   # выводит последовательность order на экран
        readerandcheker(order) # читает ответ пользователя и возвращает True если ответ правельный и False  если нет
        level += 1
        r += 1
        if readerandcheker:
            printresultT() # выводит на экран чт человек прав
        else:
            prinresultF() # выводит на экран Гейм Овер и возвращает игрока на 1 уровень
            main()


