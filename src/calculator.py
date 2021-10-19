def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def runner():
    entered = input('> ')
    try:
        a, op, b = entered.split()
    except ValueError:
        print('Invalid operation')
        return
    try:
        a = int(a)
        b = int(b)
        funcs = {
            '+': add,
            '-': subtract,
            '*': multiply
        }

        print(funcs[op](a, b))
    except ValueError:
        print('Invalid operation')


def main():
    runner()


if __name__ == '__main__':
    main()
