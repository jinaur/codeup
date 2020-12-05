n = int(input())

def reverse(answer):
    if answer == 1:
        return print(answer)
    elif answer%2:
        reverse(3*answer+1)
    else: 
        reverse(answer//2)
    return print(answer)


answer = n
r = reverse(answer)
