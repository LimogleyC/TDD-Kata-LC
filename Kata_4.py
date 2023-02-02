cities = ["Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", 
        "Amsterdam", "Vienna", "Sydney", "New York City", "London", 
        "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"]

def too_short(inp):
    if len(inp) < 2:
        return True

def parse(inp, result):
    for name in cities:
        if inp.lower() in name.lower():
            result.append(name)
    return(result)

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