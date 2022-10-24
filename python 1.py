loop = 1
while loop < 2:
    text_enter = input("Enter your text: ")
    if text_enter == "end":
        loop += 1
    
    elif text_enter == "hello":
        print("hello there!")
    
    elif text_enter == "hi":
        print("hi there!")
    
    elif text_enter == "hey":
        print("hey there!")

    elif loop == 2:
        break
    
    else:
        print("unsure...")

#Thanks KittenzExe for the elif help lmao#
