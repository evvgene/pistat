import os
import time

def pi_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return(temp)