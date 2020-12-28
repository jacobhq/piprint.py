# piprint.py

### What is it?
Piprint is a bunch of python designed to allow the [adafruit mini thermal printer](https://shop.pimoroni.com/products/mini-thermal-printer) to work like a receipt printer.

### Setup
To have your printer ready for setup, make sure you have followed [this guide](https://learn.adafruit.com/networked-thermal-printer-using-cups-and-raspberry-pi/overview). You will definitely need to change variable `4`, and all the others can be left unless you wish to change tham.

### How does it work?
The script will ask some questions, and then create a file to be printed. It will then use `os.system` to run the print command, which can be set from a handy variable, before removing the file.

### Customizing the script
There are a selection of variables at the start of the file that allow for easy customization:
| Variable        | Type         | Function                                                | Number |
| :-------------- | :----------: | :-----------------------------------------------------: | -----: |
| `itemsList`     | List         | An array of items that will be offered as products      | 1      |
| `priceList`     | List         | An array of items that will be used as prices           | 2      |
| `fileName`      | String       | The name of the file that will be printed               | 3      |
| `fileDir`       | String       | The location of the file on your computer               | 4      |
| `print_command` | String       | The command that the script will use to print your file | 5      |
| `removeFile`    | Boolean      | Set to `false` if you want to keep the txt output file  | 6      |
