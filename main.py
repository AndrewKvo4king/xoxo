def greet():
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

field=[['-']*3 for _ in range (3)]

def show ():
    print('  | 0 | 1 | 2 |')
    for i in range (len(field)):
        print (str(i)+ '   ' + '   '.join(field[i]))

def ask ():
    while True:
        cords = input ('Введите две координаты через пробел:').split()
        if len(cords)!=2:
            print('Введите только две координаты!')
            continue
        if not (cords[0].isdigit() and cords[1].isdigit()):
            print('Введите числа!')
            continue
        x, y = map(int, cords)
        if not (0 <= x < 3 and 0 <= y < 3):
            print('Координаты вне диапазона!')
            continue
        if field [x] [y]!= ' ':
            print('Поле занято!')
            continue
        break
    return x, y
def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False

greet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик")
    else:
        print(" Ходит нолик")
    x, y = ask()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if win():
        break
    if count == 9:
        print(" Ничья!")
        break