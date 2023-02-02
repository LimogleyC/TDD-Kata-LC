cities = ["Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", 
        "Amsterdam", "Vienna", "Sydney", "New York City", "London", 
        "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"]

# Purpose: Check the input is not < 2
# Input:   inp - str - User input string
# Output:  Bool - True if < 2, False if > 2
def too_short(inp):
    if len(inp) < 2:
        return True
    return False

# Purpose: Parse through list of cities to match with input
# Input:  inp - str - User input string
#         result - Empty list
# Output: result - list of cities that match input 
def parse(inp, result):
    for name in cities:
        if inp.lower() in name.lower(): # Lowers str for case insensitivity
            result.append(name)
    return(result)

# Purpose: Search through list of cities and return those that match input
# Input:  inp - str - user string input
# Output: list of cities that match input
def search(inp):
    if inp == "*":
        return(cities)
    if too_short(inp):
        return None
    result = []
    return(parse(inp, result))

# inp = input("ASDFKAJSDFHASLFD: ")
# while inp != "0":
#     print(search(inp))
#     inp = input("\nBRA bre bring bro: ")