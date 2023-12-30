def create():
    print("Enter the names of eight tennis players: ")
    names=[]
    for i in range(8):
        name=input()
        names.append(name)
    return names

def competition(names):
    winner_oneround=[]
    winner_tworound=[]
    print("Round 1-----------------------") # first round, team the eight integrants 1vs1 four teams
    for i in range(0,len(names),2):
        
        winner=str(input(f"a.{names[i]} - b.{names[i+1]}: "))

        if winner=="a":
            winner_oneround.append(names[i])
        elif winner=="b":
            winner_oneround.append(names[i+1])
    
    print("Round 2-----------------------") # second round, team the four integrants - 1vs1 two teams
    for i in range(0,len(winner_oneround),2):
        winner02=str(input(f"a.{winner_oneround[i]} - b.{winner_oneround[i+1]}: "))

        if winner02=="a":
            winner_tworound.append(winner_oneround[i])
        elif winner02=="b":
            winner_tworound.append(winner_oneround[i+1])

    print("Round 2-----------------------") # final round, 1 vs 1 
    for i in range(0,len(winner_tworound),2):
        final_winner=str(input(f"a.{winner_tworound[i]} - b.{winner_tworound[i+1]}: "))

        if final_winner=="a":
            return winner_tworound[i]
        elif final_winner=="b":
            return winner_tworound[i+1]

list_names=create()       # call the function
champion=competition(list_names)    
print(f"Champion: {champion}")

















