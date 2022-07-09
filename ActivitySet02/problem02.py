
def add(a, b):
    return a+b


def output(a, b, sum):
    print(f'{a} + {b} = {sum}')


def main():
    a, b = input("Enter the numbers = ").split()
    sum = add(int(a), int(b))

    output(a, b, sum)


if __name__ == '__main__':
    main()
