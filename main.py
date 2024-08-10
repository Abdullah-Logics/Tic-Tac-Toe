import random

def sum(a,b,c):
    return a + b +c

def show_board(x_state,o_state):
    print()
    num = 0
    while num < 9:
        print(f" {"X" if x_state[num] else ("O" if o_state[num] else " ") } |",end="")
        if num == 2 or num == 5 or num == 8:
            print("\n------------")
        num = num + 1    
    print()    

def check_win(x_state,o_state):
    win_possibiliites = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] 
    for state in win_possibiliites:      
        if sum(x_state[state[0]],x_state[state[1]],x_state[state[2]]) == 3:
            print("X Wins.....")
            return 1
        elif sum(o_state[state[0]], o_state[state[1]],o_state[state[2]]) == 3:
            print("\nO Wins.....")    
            return 1
        
        
if __name__ == "__main__":

    x_state = [0,0,0,0,0,0,0,0,0]
    o_state = [0,0,0,0,0,0,0,0,0]
    turn = random.randint(0,100000000) % 2 # 1 -->X   0-->O

    print("Welcome to Tic Tac Toe")
    show_board(x_state,o_state)
    max = 0
    while True:
        try:
            if turn == 1:
                print("X's Turn")
                value = int(input("Enter a value:- "))
                value = value - 1
                if x_state[value] == 1 or o_state[value] == 1 or value > 9:
                    print("Invalid Selection....\n")
                    continue
                x_state[value] = 1 
            elif turn == 0:
                print("O's Turn")
                value = int(input("Enter a value:- "))
                value = value - 1
                if x_state[value] == 1 or o_state[value] == 1:
                    continue
                o_state[value] = 1 
            show_board(x_state, o_state)
            r = check_win(x_state, o_state)
            if r == 1:
                print("Congratulations...")
                break
            turn = 1 - turn          
            max += 1
            if max == 9:
                print("Tie!....")
                break
        except:
            print("Invalid Selection...\n")
            continue

