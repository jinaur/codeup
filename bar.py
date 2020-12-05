n = int(input())

Max = 0
count = 0
l = []

for i in range(0, n) :
	a = int(input())
	l.append(a)
	
l.reverse()
	
for i in range(0, n) :
	if l[i] > Max :
		count += 1
		Max = l[i]
		

print(count)