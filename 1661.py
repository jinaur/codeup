a = input()

for i in range(0, len(a)) :
    if a[i] == "," :
        print(" ", end="")
    elif a[i] == " " :
        continue
    elif a[i] == ";" :
        print()
    else :
        print(a[i], end="")

print(" ")

