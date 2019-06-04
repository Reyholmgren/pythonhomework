# The attached python program has a couple errors. Debug and fix the errors so that the program runs to completion and
# provides the expected output. Do not modify the test parameters, only modify the code so that it provides the
# expected output.(hint: there are 3 “bugs” in the code that need to be fixed).


def fibonacci(starting_number, sequence_length):
    if starting_number == 0:
        a, b = 0, 1
    elif starting_number == 1:
        a, b = 1, 1
    # there was no outcome for a situation where any number other than 1 or 0 were entered
    else:
        print("Please enter a 0 or 1!")
        a = None
        b = None

    sequence = starting_number
    for i in range(sequence_length - 1):
        # sequence needed to be cast to a string
        sequence = str(sequence) + " {}".format(b)
        a, b = b, a + b
# this may not be one of the 3 bugs, but "print sequence" needed to be "print(sequence)" to run properly with new Python
    print(sequence)


# DO NOT ADJUST THE TEST PARAMETERS BELOW
# THE CONSOLE OUTPUT SHOULD MATCH THIS:
#     Please enter a 0 or 1!
#     0 1 1 2 3
#     1 1 2 3 5
#     1 1 2 3 5 8 13 21 34 55
fibonacci(2, 5)
fibonacci(0, 5)
fibonacci(1, 5)
fibonacci(1, 10)
