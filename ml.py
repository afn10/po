import sys
import subprocess
import time
import os

done = 'False'

def animate():
    while done == 'false':
        sys.stdout.write('\rconnecting server! |')
        time.sleep(0.1)
        sys.stdout.write('\rconnecting server! /')
        time.sleep(0.1)
        sys.stdout.write('\rconnecting server! -')
        time.sleep(0.1)
        sys.stdout.write('\rconnecting server! \\')
        time.sleep(0.1)
    sys.stdout.write('\rSelesai!!!     ')

animate()
done = 'false'

time.sleep(3.0)
subprocess.run("python2 m1.py",shell=True,check=True)

from time import sleep

prints = "MOBILE LEGENDS \n\033[1;32;40m bagaimana cara membuat makan dengan sangat mudah"
for char in prints:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

    
