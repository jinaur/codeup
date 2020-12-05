n = int(input())

while True :
    if n <= 60 :
        break
    n -= 60

a = 0
b = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
b_count = 0
r = ""

for i in range(0, n) :
    if a >= 10 :
        a = -1
    if b[i-b_count] == "L" :
        b_count += 11   
    a += 1
    r = b[i-b_count]

print(str(r) + str(a))