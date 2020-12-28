import time
import os
import modes
import loader
import numcheck
import file_handler

# Vars to change
fileName = "Output.txt"
fileDir = "/home/pi/Documents/Code/py-piprint"
file = fileDir + "/" + fileName
print_command = "lp -o fit-to-page " + file
removeFile = False

# More Vars
printingText = "Printing"
titleText = "Shopping"

# Vars you probably don't need to change
def clear(): os.system('clear')

clear()

# Items list and length
item_int = numcheck.check()
i = item_int
if i == 1:
    item = modes.choose()
    file_handler.new(fileName, item, titleText)
if i == 2:
    item = modes.choose2()
    file_handler.new2(fileName, item, titleText)
if i == 3:
    item = modes.choose3()
    file_handler.new3(fileName, item, titleText)

# Create file


# Print file
res = os.system(print_command)
loader.load(printingText)
if removeFile:
  os.remove(file)
print("Complete")
time.sleep(1)
clear()
