import sys
def collatz(number):
    while True:
        print(number, end=" ")
        if number == 1:
            return number
        elif number % 2 ==0:
            return collatz(number // 2)
        else:
            return collatz(3* number + 1)




while True:
    user_input= input("Enter a positive integer: ")
    try:
        x= int(user_input)
        if x < 1:
            print("Please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("That is not a number please enter an integer:")
collatz(x)