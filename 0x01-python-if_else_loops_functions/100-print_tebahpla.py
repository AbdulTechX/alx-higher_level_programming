#!/usr/bin/python3


"""prints the ASCII alphabet, in reverse order, alternating
lowercase and uppercase"""

index = 0
for alphabet in range(ord('z'), ord('a') - 1, -1):
    if alphabet % 2 == 0:
        index = 0
    else:
        index = 32
    print("{}".format(chr(alphabet - index)), end="")
