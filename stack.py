stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

print("Removed:", stack.pop())

print("Stack after pop:", stack)

s = "uday"
stack = []
for ch in s:
    stack.append(ch)
reversed=""    
while stack:
    reversed += stack.pop()
    print(reversed)
stack = []
stack.append(5)
stack.append(10)
stack.append(15)
reverse_stack = []
while stack:
    reverse_stack.append(stack.pop())
    print(reverse_stack)