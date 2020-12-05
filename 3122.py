n = int(input())

for i in range(1, n//2+3) :
    print((n-i)*" "+((i+(i-1)*2)-1)*"*"+(n-i)*" ")

for i in range(n//2+3, 1, -1) :
    print((n-i)*" "+((i+(i-1)*2)-1)*"*"+(n-i)*" ")
