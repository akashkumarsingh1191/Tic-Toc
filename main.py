Board=  {
            '7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '
        }
board_key=[]

for key in Board:
    board_key.append(key)

# print(Board)
def print_Board(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['1'] + ' | ' + board['2'] + ' | ' +board['3'])
# print_Board(Board)


def game():
    turn='X'
    count=0
    for i in range(10):
        print_Board(Board)
        print(f'It\'s your turn {count} .Move to which place.' )
        move=input()

        if Board[move]==" ":
            Board[move]=turn
            count+=1
        else:
            print(f'That place is already filled.\nMove to which place.')
            continue
        if(count>=5):
            if(Board['7'] == Board['8'] == Board['9']!=" "):
                print_Board(Board)
                print(f'\nGame over.\n')
                print(f'*** {turn} won ***')
                break
            elif(Board['4'] == Board['5'] == Board['6']!=" "):
                print_Board(Board)
                print(f'\nGame over.\n')
                print(f'*** {turn} won ***')
                break
            elif(Board['1'] == Board['2'] == Board['3'] != " "):
                print_Board(Board)
                print(f'\nGame over.\n')
                print(f'*** {turn} won ***')
                break
            elif(Board['1'] == Board['5'] == Board['9'] !=  " "):
                print_Board(Board)
                print(f'\nGame over.\n')
                print(f'*** {turn} won ***')
                break
            elif(Board['3'] == Board['5'] == Board['7'] !=  " "):
                print_Board(Board)
                print(f'\nGame over.\n')
                print(f'*** {turn} won ***')
                break
            elif(Board['1'] == Board['4'] == Board['7'] !=  " "):
                print_Board(Board)
                print(f'\nGame over.\n')
                print(f'*** {turn} won ***')
                break
            elif(Board['2'] == Board['5'] == Board['8'] !=  " "):
                print_Board(Board)
                print(f'\nGame over.\n')
                print(f'*** {turn} won ***')
                break
            elif(Board['3'] == Board['6'] == Board['9'] != " "):
                print_Board(Board)
                print(f'\nGame over.\n')
                print(f'*** {turn} won ***')
                break
        if(count == 9):
            print_Board(Board)
            print(f'\nGame over.\n')
            print(f'*** It\'s a tie! ***')

        # We have to change the turn after every move.
        if(turn == 'X'):
            turn='O'
        else:
            turn='X'
    
        restart=input(f'Do you want to play Again.(Y/N)').upper()
        if restart == 'Y':
            for key in Board:
                Board[key] = " "
            
            game()
if  __name__ == "__main__":
    game()



            
main()