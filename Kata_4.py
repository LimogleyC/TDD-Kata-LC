cities = ["Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", 
        "Amsterdam", "Vienna", "Sydney", "New York City", "London", 
        "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"]

def too_short(inp):
    if len(inp) < 2:
        return True

def search(inp):
    if too_short(inp):
        return None
    for name in cities:
        if inp in name:
            return name