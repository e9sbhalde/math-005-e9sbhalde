"""Write a program to find the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?"""


def answer(number):
    """This function returns the smallest positive number that is evenly
    divisible by all of the numbers from 1 to 20"""
    num = 1
    while True:
        if all(num % i == 0 for i in range(1, number + 1)):
            return num
        num += 1


if __name__ == "__main__":
    print(answer(20))
