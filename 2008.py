n = int(input())
a = list(map(int, input().split()))

Ascending = a
Descending = a
Ascending = sorted(a)
Descending = sorted(a, reverse=True)

for i in range(0, n) :
    if a == Ascending and a == Descending :
        print("섞임")
        break

    if a == Ascending :
        print("오름차순")
        break
    elif a == Descending :
        print("내림차순")
        break
    else :
        print("섞임")
        break

