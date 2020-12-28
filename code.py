from datetime import date
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
removeFile = true

# More Vars


# Items list and length
length = len(itemsList) - 1
length_str = str(length)
print(itemsList[1:4])
print("Enter a product id between 1 and " + length_str + ":")
selected_item = input()
selected_item_int = int(selected_item)
price = str(priceList[selected_item_int])
print("Printing")

# Create file
with open(fileName,'w',encoding = 'utf-8') as f:
   f.write("Shopping\n")
   f.write("------------------\n")
   f.write("Item")
   f.write("        ")
   f.write("Price\n")
   f.write("------------------\n")
   f.write(itemsList[selected_item_int])
   f.write("           ")
   f.write(price)
   f.write("\n")
   f.write("------------------\n")
   f.write("Printed on ")
   f.write(date_str)
   f.close()

# Print file
res = os.system(print_command)
if removeFile:
  os.remove(file)
print("Complete")
