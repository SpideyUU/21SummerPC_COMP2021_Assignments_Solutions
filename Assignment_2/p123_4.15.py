import math
import random

lottery = int(random.randrange(100, 1000))
guess = eval(input("Please enter your lottery pick. Three Digits Only: \n"))

lotteryDigit_1 = str(lottery % 100 % 10)
lotteryDigit_2 = str((lottery % 100) // 10)
lotteryDigit_3 = str(lottery // 100)

guessDigit_1 = str(guess % 100 % 10)
guessDigit_2 = str((guess % 100) // 10)
guessDigit_3 = str(guess // 100)

print("The lottery numbers are:", lottery)
if guess == lottery:
    print("Exact match!!! You have won $10,000!!!")
elif lottery == guessDigit_1 + guessDigit_3 + guessDigit_2 \
        or lottery == guessDigit_2 + guessDigit_1 + guessDigit_3 \
        or lottery == guessDigit_2 + guessDigit_3 + guessDigit_1 \
        or lottery == guessDigit_3 + guessDigit_1 + guessDigit_2 \
        or lottery == guessDigit_3 + guessDigit_2 + guessDigit_1:
    print("All numbers matched!!! You have won $3,000 Prize!!!")

    """There is no requirement for the case of two numbers matched, 
                    so that I don't really care about this condition."""
elif guessDigit_1 == lotteryDigit_1 or guessDigit_1 == lotteryDigit_2 or guessDigit_1 == lotteryDigit_3 \
        or guessDigit_2 == lotteryDigit_1 or guessDigit_2 == lotteryDigit_2 or guessDigit_2 == lotteryDigit_3 \
        or guessDigit_3 == lotteryDigit_1 or guessDigit_3 == lotteryDigit_2 or guessDigit_3 == lotteryDigit_3:
    print("One number matched!!! You have won $1,000 Prize!!!")
else:
    print("No number match, wish you have better luck next time!")
