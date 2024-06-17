# student_scores = input().split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
import math


def student_score():
    student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
    print(student_scores)
    highest_score = 0
    for n in student_scores:
        if n > highest_score:
            highest_score = n
    print(f"The highest score in class is {highest_score}")


def student_height():
    student_heights = [156, 178, 165, 171, 187]
    total = 0
    average = ''
    for n in student_heights:
        total += n
        average = total/len(student_heights)
    print(f"Average height : {average}")
    print(len(student_heights))


def weights():
    height = float(input("Enter your height in meters :"))
    weight = int(input("Enter your weight in kilograms:"))
    bmi = weight/(height * height)
    if bmi <= 18.5:
        print(f"Your BMI is {bmi},you are underweight.")
    elif bmi <= 25:
        print(f"Your BMI is {bmi},you are normal weight.")
    elif bmi <= 30:
        print(f"Your BMI is {bmi},you are slightly overweight.")
    elif bmi <= 40:
        print(f"Your BMI is {bmi},you are obese.")
    else:
        print(f"Your BMI is {bmi},you are clinically obese.")


# weights()


def leaps():
    year = int(input("which year do you want to check?\n"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap")
            else:
                print("!leap")
        else:
            print("leap year")
    else:
        print("Not leap")


# leaps()

def paint_calc():
    test_h = int(input("height of wall:"))
    test_w = int(input("width of wall:"))
    coverage = 5
    cans = test_h * test_w / coverage
    rounded_up_cans = math.ceil(cans)
    print(f"You ill need number of cans {rounded_up_cans}.")


# paint_calc()

def prime_number_checker(number):
    prime_num = True
    for i in range(2, number):
        if number % i == 0:
            prime_num = False
    if prime_num:
        print("it is a prime number.")
    else:
        print("It is not prime number.")


# prime_number_checker(13)

a= "Ajay".lower()
print(a)