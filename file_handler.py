from datetime import date

# Get date
date = date.today()
date_str = str(date)

# Handler syntax

def new(fileName, item, titleText):
    with open(fileName,'w',encoding = 'utf-8') as f:
        f.write(titleText + "\n")
        f.write("------------------\n")
        f.write("Item\n")
        f.write("------------------\n")
        f.write(item + "  ☐\n")
        f.write("------------------\n")
        f.write("Printed " + date_str)
        f.close()

def new2(fileName, item, titleText):
    with open(fileName,'w',encoding = 'utf-8') as f:
        f.write(titleText + "\n")
        f.write("------------------\n")
        f.write("Item\n")
        f.write("------------------\n")
        f.write(item[0] + "  ☐\n")
        f.write(item[1] + "  ☐\n")
        f.write("------------------\n")
        f.write("Printed " + date_str)
        f.close()

def new3(fileName, item, titleText):
    with open(fileName,'w',encoding = 'utf-8') as f:
        f.write(titleText + "\n")
        f.write("------------------\n")
        f.write("Item\n")
        f.write("------------------\n")
        f.write(item[0] + "  ☐\n")
        f.write(item[1] + "  ☐\n")
        f.write(item[2] + "  ☐\n")
        f.write("------------------\n")
        f.write("Printed " + date_str)
        f.close()
