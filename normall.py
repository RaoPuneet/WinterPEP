n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

last = 1000000
possible = True

while left <= right:
    
    if arr[left] >= arr[right]:
        pick = arr[left]
        left += 1
        right -= 1
    else:
        pick = arr[right]
        left += 1
        right -= 1

    if pick <= last:
        last = pick
    else:
        possible = False
        break

if possible:
    print("Yes")
else:
    print("No")
