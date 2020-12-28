from datetime import date
import time
import os

# Get date
date = date.today()
date_str = str(date)

# Vars to change
itemsList = ["N/A", "Ford", "Volvo", "BMW"]
priceList = [0.00, 100, 20, 300]
fileName = "Output.txt"
fileDir = "/home/pi/Documents/Code/py-piprint"
file = fileDir + "/" + fileName
print_command = "lp -o fit-to-page " + file
removeFile = True

# More Vars
printingText = "Printing"
titleText = "Shopping"

def clear(): os.system('clear')
clear()

# Items list and length
length = len(itemsList) - 1
length_str = str(length)
print(itemsList[1:4])
selected_item = input("Enter a product id between 1 and " + length_str + ":")
selected_item_int = int(selected_item)
price = str(priceList[selected_item_int])

# Create file
with open(fileName,'w',encoding = 'utf-8') as f:
   f.write(titleText + "\n")
   f.write("------------------\n")
   f.write("Item")
   f.write("        ")
   f.write("Price\n")
   f.write("------------------\n")
   f.write(itemsList[selected_item_int] + "           " + price + "\n")
   f.write("------------------\n")
   f.write("Printed on " + date_str)
   f.close()

# Print file
# res = os.system(print_command)
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
if removeFile:
  os.remove(file)
print("Complete")
time.sleep(1)
clear()
