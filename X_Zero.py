game_over = False
player1 = True
n = 0

# Создаем карту

maps = {'str1': ' ', '0': '0', '1': '1', '2': '2',
        'str2': '0', '00': '-', '01': '-', '02': '-',
        'str3': '1', '10': '-', '11': '-', '12': '-',
        'str4': '2', '20': '-', '21': '-', '22': '-'}

# Выигрышные линии
victories = [['00', '01', '02'],
             ['10', '11', '12'],
             ['20', '21', '22'],
             ['00', '10', '20'],
             ['01', '11', '21'],
             ['02', '12', '22'],
             ['00', '11', '22'],
             ['02', '11', '20']]

# Вывод на экран
def print_maps():
    print(maps.get('str1'), maps.get('0'), maps.get('1'), maps.get('2'))
    print(maps.get('str2'), maps.get('00'), maps.get('01'), maps.get('02'))
    print(maps.get('str3'), maps.get('10'), maps.get('11'), maps.get('12'))
    print(maps.get('str4'), maps.get('20'), maps.get('21'), maps.get('22'))

# Сделать ход в ячейку
def step_maps(step, symbol):
    global player1, n     # n нужна для подсчета ходов, чтобы определить ничью
    if step != "":
        if maps[step] == '-':
            maps[step] = symbol
            n = n + 1
            player1 = not player1
            print(player1)
        else:
            print('Ход в ячейку уже сделан! Сходите еще раз')

# Текущий результат игры
def get_result():
    win = ""
    if n < 9:
        for i in victories:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                win = "Победа X!"
            if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
                win = "Победа O!"
    else:
        win = "Ничья!"

    return win

# Основная программа

while game_over == False:
    symbol = ''
    step = ''

    #  Показываем карту
    print_maps()

    # Узнаем чей ход
    if player1 == True:
        symbol = "X"
    else:
        symbol = "O"

    # Узнаем строку/столбец
    step1 = input("введите номер строки: ")
    step2 = input("введите номер столбца: ")

    # Проверяем рамки игрового поля
    if 0 <= int(step1) <= 2:
        if 0 <= int(step2) <= 2:
            step = step1 + step2
        else:
            print('Такой ячейки на поле нет!')
    else:
        print('Такой ячейки на поле нет!')

    step_maps(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True

# Игра окончена. Объявим победителя.
print_maps()
print(win)