########################################################
# Task A10_T5
# Developer Andrei Kuga
# Date 2025-12-2
########################################################

def recursiveFactorial(PNum: int) -> int:
    if PNum > 1:
        PResult = PNum * recursiveFactorial(PNum-1)
        return PResult
    else:
        return PNum

def main() -> None:
    print('Program starting.')
    try:
        factorial = int(input('Insert factorial: '))
        print('Factorial {}!'.format(factorial))
        result = recursiveFactorial(factorial)
        for i in range(1,factorial):
            print(i, end='*')
        print('{} = {}'.format(factorial, result))

    except ValueError:
        print('Invalid input, must be integer.')
    print('Program ending.')

if __name__ == "__main__":
    main()