def fizzbuzz(num):
    fb = ""             # str to be concatenated
    
    # remainders to check division
    rem3 = num % 3 
    rem5 = num % 5      
    
    if rem3 == 0:       # If divisible by 3 add "fizz"
        fb += "fizz"
    if rem5 == 0:       # If divisible by 5 add "buzz"
        fb += "buzz"
    
    return fb           # Return str