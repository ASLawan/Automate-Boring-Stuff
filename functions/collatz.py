#!/usr/bin/python3

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    return result

def main():
    value = int(input("Enter a number: "))
    try:
        if isinstance(value, int):
            while value != 1:
                value = collatz(value)
                print(value)
        return value
    except: 
        print("Input must be an integer")


if __name__ == "__main__":
    main()
