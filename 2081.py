Max = 0
Max_i = 0

for i in range(0, 9) :
    n = int(input())
    if n > Max :
        Max = n
        Max_i = i+1

print(Max)
print(Max_i)


