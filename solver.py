"""Write a function in python that returns the smallest positive number 
that is evenly divisible by all of the numbers between the range p and q, inclusive.
Use the range from the lesser of p and q to the greater of p and q. 
Make no assumption about which is lesser or greater."""

def solver(p, q):
    """This function eturns the smallest positive number 
    that is evenly divisible by all of the numbers between the range p and q, inclusive.
    Use the range from the lesser of p and q to the greater of p and q. 
    Make no assumption about which is lesser or greater."""
    start = min(p, q)
    end = max(p, q)
    num = 1

    while True:
        if all(num % i == 0 for i in range(start, end + 1)):
            return num
        num += 1


if __name__ == "__main__":
    print(solver(10, 1))
