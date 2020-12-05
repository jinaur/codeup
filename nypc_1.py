n = int(input())
l = list(map(int, input().split()))

myLastMax = myMax = l[0]

for a in l[1:] :
    myLastMax = max(a, myLastMax+a)
    myMax = max(myLastMax, myMax)
    
print(myMax)