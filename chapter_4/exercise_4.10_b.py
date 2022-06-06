import random


def multiplication_game():

    correct = []
    incorrect = []

    def start_game():

        question = 1

        def add_correct():
            correct.append(1)

        def add_incorrect():
            incorrect.append(1)

        for x in range(0, 11):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = a * b

            ask = print("Question", question, ":", a, "x", b, "=", end=" ")

            askq = int(input())
            if askq == c:
                print("Correct")
                add_correct()
            else:
                print("Incorrect, the answer is", c)
                add_incorrect()
            question = question + 1

        print("\n")
        print("correct: ", sum(correct))
        print("incorrect: ", sum(incorrect))

    start_game()


multiplication_game()
