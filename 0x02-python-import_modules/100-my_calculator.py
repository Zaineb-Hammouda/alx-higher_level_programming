#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    print(len(sys.argv))
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
