n = input()

r = int(n[::-1])
r = r * 2
r = r % 100
print(r)
if r > 50 :
    print("OH MY GOD")
else :
    print("GOOD")

    