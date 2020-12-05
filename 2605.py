lines = []
visits = []
for i in range(0, 7) :
    Aline = list(map(int, input().split()))
    lines.append(Aline)
    visits.append([0] * len(Aline))
    
def my_func(x, y) :
    if visits[y][x] == 1 :
        return 0

    visits[y][x] = 1
    count = 1
    color = lines[y][x]

    if y < 6 and lines[y+1][x] == color :
        count += my_func(x, y+1)
    if y > 0 and lines[y-1][x] == color :
        count += my_func(x, y-1)
    if x < 6 and lines[y][x+1] == color :
        count += my_func(x+1, y)
    if x > 0 and lines[y][x-1] == color :
        count += my_func(x-1, y)

    return count
    
a = 0
for y in range(0, 7) :
    for x in range(0, 7) :
        r = my_func(x, y)
        if r >= 3 :
            a += 1

print(a)