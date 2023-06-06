#!/usr/bin/python3
for asci_letter in range(97, 113):
    if chr(asci_letter) != 'q' and chr(asci_letter) != 'e':
        print("{}".format(chr(asci_letter)), end="")
