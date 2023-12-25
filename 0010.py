import math
def  isPrime(num):
    if (num < 2 or num % 2 == 0):
        return (num == 2)
    divisor = 3
    while (divisor <= math.sqrt(num)):
        if (num % divisor == 0):
            return False
        else:
            divisor += 2
    return True

def  findNextPrime(num):
    if (num < 2):
        return 2
    if (num % 2 == 0):
        num -= 1
    guess = num + 2
    while (not isPrime(guess)):
        guess += 2      
    return guess
def main():
    f = [2]
    while f[-1] < 2 * 10**6:
        f.append(findNextPrime(f[-1]))
    print(sum(f[:-1]))
main()