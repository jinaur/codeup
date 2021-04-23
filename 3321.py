# n : 토핑 종류의 수
# a : 도우의 가격
# b : 토핑의 가격
# c : 도우의 칼로리수
# r : 토핑의 칼로리수
# (572 + 2530 + 1861 + 1649) / 41 
# r : 달러
# count : 열량

n = int(input())
a, b = list(map(int, input().split()))
c = int(input())
l = []
lr = []
Max = 0
for i in range(0, n) :
    t = int(input())
    l.append(t)
    lr.append(t)

lr.sort()
l.sort()

for i in range(0, n-1) :
    Min = 100000 
    count = c
    r = a
    count += sum(l)
    r += b * (len(l))
    count = int(count / r)
    if count > Max :
        Max = count

    if lr[i] < Min :
        Min = lr[i]
        l.remove(Min)

print(Max)

