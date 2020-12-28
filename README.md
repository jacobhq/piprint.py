# piprint.py

### What is it?
Piprint is a bunch of python designed to allow the [Adafruit mini thermal printer](https://shop.pimoroni.com/products/mini-thermal-printer) to work like a receipt printer.

### How does it work?
The script will ask some questions, and then create a file to be printed. It will then use `os.system` to run the print command, before removing the file.
