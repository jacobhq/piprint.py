def choose():
    item = input("What should I print? ")
    return item

def choose2():
    item1 = input("What should I print? ")
    item = [item1]
    item2 = input("And item two: ")
    item.append(item2)
    return item

def choose3():
    item1 = input("What should I print? ")
    item = [item1]
    item2 = input("Now for item two: ")
    item.append(item2)
    item3 = input("And finally item three: ")
    item.append(item3)
    return item