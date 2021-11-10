# XO game
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = ""
lsp = []
pl = 1
print("Enter the two player name")
# loop for getting player name
while pl <= 2:
    pl1 = input()
    lsp.append(pl1)
    pl = pl + 1
print(lsp[0], "your character is X")
print(lsp[1], "your character is O")
j = 0
c = ""
while True:
    # function for getting 1 to 9 3x3 matrix
    def pr():
        i = 0
        while i < len(ls):
            if (i % 3) == 0:
                print()
            print(ls[i], end=" ")
            i = i + 1


    round = 0
    while round < 2:
        pr()
        print()
        print(lsp[round], "your turn ")
        nm = int(input())
        a = ls.index(nm)
        if round == 0:
            ls.insert(a, "X")
            ls.remove(nm)
        elif round == 1:
            ls.insert(a, "O")
            ls.remove(nm)
        round = round + 1
        # conditions for X player winning
        if ls[0] == ls[1] == ls[2] == "X" or ls[3] == ls[4] == ls[5] == "X" or ls[6] == ls[7] == ls[8] == "X" or ls[
            0] == ls[4] == ls[8] == "X" or ls[2] == ls[4] == ls[6] == "X" or ls[1] == ls[4] == ls[7] == "X" or ls[2] == \
                ls[5] == ls[8] == "X" or ls[3] == ls[6] == ls[9] == "X":
            print()
            print(lsp[0], "Win the match")
            win = "win"
            break
        # conditions for O player winning
        elif ls[0] == ls[1] == ls[2] == "O" or ls[3] == ls[4] == ls[5] == "O" or ls[6] == ls[7] == ls[8] == "O" or ls[
            0] == ls[4] == ls[8] == "O" or ls[2] == ls[4] == ls[6] == "O" or ls[1] == ls[4] == ls[7] == "O" or ls[2] == \
                ls[5] == ls[8] == "O" or ls[3] == ls[6] == ls[9] == "O":
            print()
            print(lsp[1], "Win the match")
            win = "win"
            break
    if win == "win":
        break
    j = j + 1
