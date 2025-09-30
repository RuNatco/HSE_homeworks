def validate_stack_sequences(pushed, popped):
    stack = []
    i = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return not stack

if __name__ == "__main__":
    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [1, 3, 5, 4, 2]
    print(validate_stack_sequences(pushed1, popped1))

    pushed2 = [1, 2, 3]
    popped2 = [3, 1, 2]
    print(validate_stack_sequences(pushed2, popped2))
