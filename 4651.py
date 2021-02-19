# 배 = 0
# 등 = 1
# 배 1, 등 3 = 도 | A
# 배 2, 등 2 = 개 | B
# 배 3, 등 1 = 걸 | C 
# 배 4, 등 0 = 윷 | D
# 배 0, 등 4 = 모 | E

l = ['E', 'A', 'B', 'C', 'D']
for i in range(0, 3) :
    a = list(map(int, input().split()))
    zero_count = 0
    for r in a :
        if r == 0 :
            zero_count += 1

    print(l[zero_count])

