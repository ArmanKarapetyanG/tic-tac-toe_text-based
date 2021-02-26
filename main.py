def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

print('\nIII-----------------------WELCOME TO TIC TAC TOE-----------------------III')
emp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
poses = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print_tic_tac_toe(emp)

class Player:
    def __init__(self, brush, name):
        self.name = name
        self.brush = brush

if input('Type 1 for "X" or 2 for "O" ') == "1":
    name = str(input('Your name is? '))
    brush = "X"
    mainplayer = Player(brush, name)
    name = str(input('and second players name is? '))
    brush = "O"
    secondaryplayer = Player(brush, name)
else:
    name = str(input('Your name is? '))
    brush = "O"
    mainplayer = Player(brush, name)
    name = str(input('and second players name is? '))
    brush = "X"
    secondaryplayer = Player(brush, name)
players = [mainplayer, secondaryplayer]
def winner(emp):
    if emp[0] == emp[1] == emp[2] and emp[0] != ' ':
        for i in players:
            if i.brush == emp[0]:
                return (f'{i.name} WINs!')
    elif emp[3] == emp[4] == emp[5] and emp[3] != ' ':
        for i in players:
            if i.brush == emp[0]:
                return (f'{i.name} WINs!')
    elif emp[6] == emp[7] == emp[8] and emp[6] != ' ':
        for i in players:
            if i.brush == emp[0]:
                return (f'{i.name} WINs!')
    elif emp[0] == emp[4] == emp[8] and emp[0] != ' ':
        for i in players:
            if i.brush == emp[0]:
                return (f'{i.name} WINs!')
    elif emp[2] == emp[4] == emp[6] and emp[2] != ' ':
        for i in players:
            if i.brush == emp[0]:
                return (f'{i.name} WINs!')
    elif emp[0] == emp[3] == emp[6] and emp[0] != ' ':
        for i in players:
            if i.brush == emp[0]:
                return (f'{i.name} WINs!')
    elif emp[1] == emp[4] == emp[7] and emp[1] != ' ':
        for i in players:
            if i.brush == emp[1]:
                return (f'{i.name} WINs!')
    elif emp[2] == emp[5] == emp[8] and emp[2] != ' ':
        for i in players:
            if i.brush == emp[0]:
                return (f'{i.name} WINs!')
    else:
        return ' '
while len(poses) != 0:
    if brush == "X":
        print(f'move is up to {secondaryplayer.name}')
        print_tic_tac_toe(emp)
        move = int(input(f'Choose available position {poses} '))
        emp[move] = secondaryplayer.brush
        poses.remove(move)
        print(f'your turn {mainplayer.name}')
        print_tic_tac_toe(emp)
        if winner(emp) != ' ':
            print(winner(emp))
            break

        move = int(input(f'Choose available position {poses} '))
        emp[move] = mainplayer.brush
        poses.remove(move)
        print_tic_tac_toe(emp)
        if winner(emp) != ' ':
            print(winner(emp))
            break
    else:
        print(f'move is up to {mainplayer.name}')
        print_tic_tac_toe(emp)
        move = int(input(f'Choose available position {poses} '))
        while move not in poses:
            print('please choose right pos')
            move = int(input(f'Choose available position {poses} '))
        emp[move] = mainplayer.brush
        poses.remove(move)
        print(f'your turn {secondaryplayer.name}')
        print_tic_tac_toe(emp)
        if winner(emp) != ' ':
            print(winner(emp))
            break

        move = int(input(f'Choose available position {poses} '))
        while move not in poses:
            print('please choose right pos')
            move = int(input(f'Choose available position {poses} '))
        emp[move] = secondaryplayer.brush
        poses.remove(move)
        print_tic_tac_toe(emp)
        if winner(emp) != ' ':
            print(winner(emp))
            break