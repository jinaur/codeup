a = input()

for i in range(0, len(a)) :
    if a[i] == "," :
        print("", end=" ")
    else :
        print(a[i], end="")

print(" ")

