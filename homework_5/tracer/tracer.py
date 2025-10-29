import functools
import inspect


def trace_recursive(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        frame = inspect.currentframe()
        call_stack = []

        while frame:
            call_stack.append(frame)
            frame = frame.f_back

        depth = len(call_stack) - 1

        indent = '    ' * depth
        print(f"{indent}Вход: {func.__name__} с args {args} kwargs {kwargs}")

        result = func(*args, **kwargs)

        print(f"{indent}Выход: {func.__name__} с результатом {result}")

        return result
    return wrapper


@trace_recursive
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    print("Последовательность Фибоначчи с трассировкой:")
    fibonacci(5) 


