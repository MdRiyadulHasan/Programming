from typing import List 

def destCity( paths: List[List[str]]) -> str:
    starting_cities = {path[0] for path in paths}
    print(starting_cities)
    print(type(starting_cities))
    for path in paths:
        if path[1] not in starting_cities:
            return path[1]
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))
