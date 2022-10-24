loop = 1
while loop < 2:
    text_enter = input("Enter your text: ")
    if text_enter == "end":
        loop += 1
    
    if text_enter == "hello":
        print("hello there!")
    
    if text_enter == "hi":
        print("hi there!")
    
    if text_enter == "hey":
        print("hey there!")

    if loop == 2:
        break
    
    else:
        print("unsure...")
