grid = {
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9"
}

def print_grid(grid):

    print (f"\n{grid[1]}|{grid[2]}|{grid[3]}")
    print ("-+-+-")
    print (f"{grid[4]}|{grid[5]}|{grid[6]}")
    print ("-+-+-")
    print (f"{grid[7]}|{grid[8]}|{grid[9]}\n")

def verification(sign):
    
    win_combinations = [
        [1,2,3],
        [3,6,9],
        [9,8,7],
        [7,4,1],
        [2,5,8],
        [4,5,6],
        [1,5,9],
        [7,5,3]
    ]
    
    for comb in win_combinations:

        if(grid[comb[0]] == sign and grid[comb[1]] == sign and grid[comb[2]] == sign):
            return "win"

    squares = 0
    for key, value in grid.items():
        if value not in ["X","O"]:
            squares +=1
    if squares == 0:
        return "draw"

def game_round(grid):

    players = ["X","O"]
    for player in players:

        while True:
            try:
                option = int(input(f"{player}'s turn to choose a square (1-9):"))
            except ValueError:
                print("\nInvalid input\n")
                continue
            
            if option < 1 or option > 9:
                print("\nInvalid input\n") 
                continue
            elif grid[option] in players:
                print("\nThat square is already taken, try another one\n")
            else: break        
        
        grid[option] = player
        print_grid(grid)
        state = verification(player)
        if(state == "win"):
            print(f"\n{player} wins!\n")
            return False  
        elif(state == "draw"):
            print(f"\nIt's a draw!\n")
            return False     

def main():  

    game = True

    print_grid(grid)
    while (game != False):            
        game = game_round(grid)

if __name__ == "__main__":
    main()








