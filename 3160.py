n = int(input())
     
inventory = 0
sell = 0
lastTurn = 0

for i in range(0, n) :
    t, order = list(map(int, input().split()))
    turn = t//10
    if turn > lastTurn :
        inventory += 5
        lastTurn = turn
    
    if inventory >= order :
        inventory -= order
        sell += order

print(sell)

