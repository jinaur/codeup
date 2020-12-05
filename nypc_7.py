n = int(input())
s, k = map(int, input().split())
a = list(map(int, input().split()))

arr = []

for i in range(0, n) :
    arr.append({
    'no': i+1,
    'v': a[i],
    'd': abs(a[i] - s)
})

arr = sorted(arr, key=lambda x: (x['d'], x['v']))

for i in range(0, k) :
    r = arr[i]
    print(r['no'], end=' ')

print()