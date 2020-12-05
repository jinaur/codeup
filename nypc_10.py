n = int(input())

def my_func(arr) :
    l = ['+', '-', '*', '/', '.']
    for i in l :
        for j in l :
            if i == '.' and j == '.' :
                continue
            if i == '/' and arr[1] == 0 :
                continue
            if j == '/' and arr[2] == 0 :
                continue

            s = str(arr[0]) + i + str(arr[1]) + j + str(arr[2])
            
            e = eval(s)
            if e == arr[3] and :
                print(s + '=' + str(arr[3]))
                return

for i in range(0, n) :
    arr = list(map(int, input().split()))
    r = my_func(arr)
