n = int(input())

Minc = 100000 # 번호
Mins = 100000 # 거리
Minp = 100000 # 가격
for i in range(0, n) :
    a, b, c = list(map(int, input().split()))
    if b < Mins :
        Minc = a
        Mins = b
        Minp = c
    
    