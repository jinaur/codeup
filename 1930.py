import sys

def supersum(k,n):
    if k == 0:
        return n
    sum = 0
    for i in range(1, n+1):
        sum += supersum(k-1,i)
    return sum
 
while True :
    try :
        k , n = map(int, sys.stdin.readline().split())
        print(supersum(k, n))
    except EOFError :
        break