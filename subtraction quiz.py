import random
import time

NUMBER_OF_QUESTIONS = 5  # total number of questions to give to the user
correctCount = 0  # count the number of correct answers
count = 0  # count the number of questions given

startTime = time.time()  # get the current time

while count < NUMBER_OF_QUESTIONS:
    number1 = random.randint(0, 9)
    number2 = random.randint(0, 9)

    # if number1 is < number2 swap the two

    if number1 < number2:
        number1, number2 = number2, number1

    # prompt the user to answer "What is number1 - number2?"

    answer = int(input("What is " + str(number1) + " - " + str(number2) + " ?"))

    if number1 - number2 == answer:
        print("You are correct!")

        correctCount += 1
    else:
        print("Your answer is wrong. \n", number1, "-", number2, "is", number1 - number2)

    count += 1

endTime = time.time()
testTime = int(endTime - startTime)

print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS,
      "\nTest time is", testTime, "seconds")










