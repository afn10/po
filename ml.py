import sys

from time import sleep

prints = "\033[1;32;40m Bright Green\nsa"
for char in prints:
    sleep(0.5)
    sys.stdout.write(char)
    sys.stdout.flush()
