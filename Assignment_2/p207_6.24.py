import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int((n/2) + 1), 1):
        if n % i == 0:
            return False
    return True
def reverse(number):
    reverse = 0
    while number != 0:
        reverse *= 10
        reverse += number % 10
        number /= 10
    return reverse
def isPalindrome(number):
    return number == reverse(number)
def main():
    count = 0
    for i in range(0, 100, 1):
        if isPrime(i) and isPalindrome(i):
            print("%10d", i)
            count += 1
            if count % 10 == 0 and i != 0:
                print("")
main()
