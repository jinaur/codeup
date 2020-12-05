a = input()

r = 0
for i in range(0, len(a)) :
    r += int(a[i])

if r % 7 == 4 :
    print("Bad")
else :
    print("Good")

    