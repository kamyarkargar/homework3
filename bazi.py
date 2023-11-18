#game
print("________________normal answer______________")
import random
first = 100
second = 999
guess = random.randint(first, second)
print(guess)
answer = input(" print c for correct, b for bigger and s for smaller! \n")
while answer != "c":
    if answer == "b":
        first = guess + 1 
        guess = random.randint(first, second)
        print(guess)
    elif answer == "s":
        second = guess - 1 
        guess = random.randint(first, second)
        print(guess)
    answer = input("what do you think about the new number? ")  
print("you did it!")
print("________________best answer___________________")
def computer_guess(num):
    low = 100#the start 
    high = 999#the end
    guess = (low+high)//2#براي محاسبه عدد مياني فرمولي نوشتيم تا با محاسبه اعداد مياني هر دور تکرار به عدد اصلي برسيم
    while guess != num:#قرار دادن در حلقه براي تکرار فرمول بالا
        guess = (low+high)//2#قرار دادن فرمول بالا به عنوان حدس
        print("The computer takes a guess...", guess)
        if guess > num:#اگر حدسمان بيشتر بود
            high = guess
        elif guess < num:#اگر حدسمان کمتر بود
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")


def main():#تابعي براي گرفتن عدد
    num = int(input("Enter a number: "))
    if num < 100 or num > 999:
        print("Must be in range [1, 100]")
    else:
        computer_guess(num)

if __name__ == '__main__':#فراخواني تابع
    main()
