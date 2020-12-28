import time
import os
def clear(): os.system('clear')

def load(printingText):
    clear()
    print(printingText + " - [....]")
    time.sleep(0.4)
    clear()
    print(printingText + " - [#...]")
    time.sleep(0.4)
    clear()
    print(printingText + " - [##..]")
    time.sleep(0.4)
    clear()
    print(printingText + " - [###.]")
    time.sleep(0.4)
    clear()
    print(printingText + " - [####]")
    clear()