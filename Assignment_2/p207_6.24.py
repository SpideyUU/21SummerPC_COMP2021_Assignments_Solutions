def reverse(number):
    rev = 0
    while number != 0:
        lastDigit = number % 10
        number //= 10
        rev = (rev * 10) + lastDigit
    return rev


def isPrime(n):
    div = 2
    while div <= n / 2:
        if n % div == 0:
            return False
        div += 1
    return True


def isPalindrome(num):
    return True if (reverse(num) == num) else False


def main():
    count = 0
    numToCheck = 1
    while count < 100:
        numToCheck += 1
        if isPrime(numToCheck) and isPalindrome(numToCheck):
            print('{:>5d} '.format(numToCheck), end='')
            if (count + 1) % 10 == 0:
                print()
            count += 1


main()
