arr = list(map(int, input("Enter numbers separated by space: ").split()))
mini = arr[0]

for num in arr:
    if num < mini:
        mini = num


numbers = [4, 7, 2, 9, 1]
print("Smallest number:", mini)