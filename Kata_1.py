def fizzbuzz(num):
    fb = ""             # str to be concatenated
    
    if num == 0:
        return fb
    if not(num % 3):       # If divisible by 3 add "fizz"
        fb += "fizz"
    if not(num % 5):       # If divisible by 5 add "buzz"
        fb += "buzz"
    
    return fb           # Return str

if __name__ == "__main__":
    inp = 1
    while inp:
        inp = int(input("Enter Int: "))
        print(fizzbuzz(inp))