t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    left, right, staticmethodck = 0, len(arr)-1, None
    if arr[left] >= arr[right]:
        stack = [arr[left]]
        left += 1
    else:
        stack = [arr[right]]
        right -= 1
    if len(arr) <= 2:
        print ('Yes')
    else:
         
        while left <= right:
            if arr[left] > stack[-1] or arr[right] > stack[-1]:
                print ('No')
                break
            if arr[left] >= arr[right]:
                stack.append(arr[left])
                left += 1
            else:
                stack.append(arr[right])
                right -= 1
        else:
            print ('Yes')
