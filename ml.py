import sys

from time import sleep

words = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
for char in words:
    sleep(0.5)
    sys.stdout.write(char)
    sys.stdout.flush()
