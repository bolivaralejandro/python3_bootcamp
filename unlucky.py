for num in range(1,21):
    if num == 4 or num == 13:
        state = "UNLUCKY!"
    elif num % 3 == 0:
        state = "odd"
    else:
        state = "even"
    print(f"{num} is {state}")
    
    
    
        