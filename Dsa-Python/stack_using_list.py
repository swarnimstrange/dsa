stack = []

def add():
    print("Element to add:")
    element= int(input())
    if len(stack) == n:
        print("List is full!")
    else:
        stack.insert(0,element)
        print(stack)

def pop():
    if stack == []:
        print("stack is empty")
    else:
        stack.pop()
        print(stack)

print("Limit of Stack")
n = int(input())
while True:
    print("1.add element in stack\n2.pop element from stack\n3.quit")
    choice = int(input())
    if choice == 1:
        add()
    elif choice == 2:
        pop()
    elif choice == 3:
        break


