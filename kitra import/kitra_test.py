import kitra

loop = 1
while loop < 2:
    text_enter = input("Enter your text: ")
    if text_enter == "end":
        loop += 1
    
    elif text_enter == "hello":
        kitra.hello("Kitra")
    
    elif text_enter == "hi":
        kitra.hi("Kitra")
    
    elif text_enter == "hey":
        kitra.hey("Kitra")

    elif loop == 2:
        break
    
    else:
        print("unsure...")

#Thanks KittenzExe for the elif help lmao#
