# def exponencial ( n ):
#     if n == 0:
#         return 1
#     return n * exponencial(n-1)

# def main():
#     n2 = int(input('Please enter a number for base: '))
#     n = int(input('Please enter a number for exponential: '))
#     n = exponencial(n)
#     result = n2**n
#     print(result)

# main()

def exponential(base, exp):
    if exp == 0:
        return 1
    return base * exponential(base, exp-1)

def main():
    print(exponential(int(input('please enter a base: ')), (int(input('Please enter a exponential')))))

main()