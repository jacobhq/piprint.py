from datetime import date
import os

date = date.today()
date_str = str(date)
itemsList = ["N/A", "Ford", "Volvo", "BMW"]
length = len(itemsList) - 1
length_str = str(length)
priceList = [0.00, 100, 20, 300]
print(itemsList[1:4])
print("Enter a product id between 1 and " + length_str + ":")
selected_item = input()
selected_item_int = int(selected_item)
price = str(priceList[selected_item_int])
print("Printing")

# Create file
with open("output.txt",'w',encoding = 'utf-8') as f:
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
print_command = "lp -o fit-to-page /home/pi/Documents/Code/py-piprint/output.txt"
res = os.system(print_command)
print("Complete")
os.remove("/home/pi/Documents/Code/py-piprint/output.txt")
