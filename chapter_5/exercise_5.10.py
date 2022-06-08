# Chapter 5
# 5.9 Exercises
# 10.

from random import randint


def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)


def test_scores():
    n(1)

    test_scores = []

    for count in range(0, 5):

        input_number = eval(input(f"please enter test score: "))

        test_scores.append(input_number)

    print(f"test scores: {test_scores}")

    sorted_scores = sorted(test_scores)

    sorted_scores_min_two = sorted_scores[2:]

    print(f"sorted test scores: {sorted_scores}")
    n()

    print(f"highest score: {sorted_scores[-1]}")

    print(f"second largest score: {sorted_scores[-2]}")

    print(f"lowest score: {sorted_scores[0]}")

    print(f"average score: {sum(sorted_scores) / len(sorted_scores)}")

    print(
        f"average score minus two lowest scores: {sum(sorted_scores_min_two) / len(sorted_scores_min_two)}"
    )
    n(2)


test_scores()
