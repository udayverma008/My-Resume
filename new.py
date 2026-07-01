arr = [10, 20, 30, 40, 50]
arr[4] = 100
print(arr)
arr.append(50)
print(arr)
arr.pop(5)
print(arr)

    
    
def largest(arr):
    max = arr[0]

    for num in arr:
        if num > max:
            max = num

    return max

print(largest(arr))

name ="uday"
print(name)
for ch in name:
    print(ch)

print(name[::-1])