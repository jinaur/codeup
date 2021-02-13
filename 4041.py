n = input()

nr = int(n[::-1])

r = 0
for i in range(0, len(n)) :   
    if n[i] != 0 :
        r += int(n[i])

print(nr)
print(r)

