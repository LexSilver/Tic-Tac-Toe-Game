Playing_field =  [["-", "-", "-"],
                  ["-", "-", "-"],
                  ["-", "-", "-"]]

def draw_field():
    for x in Playing_field:
        print(x[0], x[1], x[2])


def cross():
    print("First player's turn ")
    string = int(input("Enter line number: "))
    column = int(input("Enter column number: "))

    while string < 1 or string > 3  or column < 1  or column > 3  or Playing_field[string - 1][column - 1] == 'x' or Playing_field[string - 1][column - 1] == 'o':
        string = int(input("Enter line number again: "))
        column = int(input("Enter column number again: "))

    Playing_field[string - 1][column - 1] = "x"

def circle():
    print("Second player's turn")
    string = int(input("Enter line number: "))
    column = int(input("Enter column number: "))

    while string < 1 or string > 3  or column < 1  or column > 3  or Playing_field[string - 1][column - 1] == 'x' or Playing_field[string - 1][column - 1] == 'o':
        string = int(input("Enter line number again: "))
        column = int(input("Enter column number again: "))

    Playing_field[string - 1][column - 1] = "o"

def chec():
    for x in Playing_field:
        if x[0] == x[1] == x[2] != "-":
            print("The winner is - ", x[0])
            victory[0] = 1
            break
    for i in range(0, 2):
        if Playing_field[0][i] == Playing_field[1][i] == Playing_field[2][i] != "-":
            print("The winner is - ", Playing_field[0][i])
            victory[0] = 1
            break
    if Playing_field[0][0] == Playing_field[1][1] == Playing_field[2][2] != "-":
        print("The winner is - ", Playing_field[0][0])
        victory[0] = 1

    elif Playing_field[0][2] == Playing_field[1][1] == Playing_field[0][2] != "-":
        print("The winner is - ", Playing_field[0][2])
        victory[0] = 1

print("Tic tac toe 3 х 3.")

print("The playing field")
draw_field()
while True:
    k = 0
    victory = [0]

    while k < 9:
        cross()
        k += 1
        draw_field()
        chec()
        if victory[0] == 1:
            break
        elif k == 9:
            print("Standoff")
            break
        circle()
        chec()
        if victory[0] == 1:
            break
        k += 1
        draw_field()
        break