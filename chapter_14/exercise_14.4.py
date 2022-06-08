# Chapter 14
# 14.6 Exercises
# 4.

def n(x=0):
    print("\n" * x)


def dlm(x=0):
    print("-" * x)



def name():
    n(1)

    class Time:

        def __init__(self, seconds):

            self.seconds = seconds

        def convert_to_minutes(self):

            return self.seconds / 60

    time = Time(230)
    print(time.convert_to_minutes())


    n(2)


name()
