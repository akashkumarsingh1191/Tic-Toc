from Board import print_Board
Board=  {
            '7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' '
        }
board_key=[]
for key in Board:
    board_key.append(key)

def game():
    turn='X'
    count=0
    for i in range(10):
        print_Board(Board)
        print(f'It\'s your turn {count} .Move to which place.' )
        move = input('Enter your move (1-9): ')
        try:
            if Board[move]==" ":
                Board[move]=turn
                count+=1
            else:
                print(f'That place is already filled.\nMove to which place.')
                continue
        except:
            print('Invalid move. Please try again.')
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



            
# main()