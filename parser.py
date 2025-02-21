from urllib.request import urlopen
file_path = "./a-coords.txt"

def read_distances_from_coord_file(path = ""):
    file = urlopen(path)
    # file = open(path, "r")
    lines = list(map(lambda line : line.replace("\n", ""), file.readlines()))
    lines = list(filter(lambda line : len(line) > 0 and "#" not in line, lines))

    def split(line = ""):
        return tuple(map(float, line.split(" ", 1)))

    coords = list(map(split, lines))
    coords.insert(0, (0.0, 0.0))

    # calculate the distance between origin and first point
    # calculate the distances between each point after the first point
    # return an array of tuples (x, y) which represent distances to travel
    distances = [
        (coords[i+1][0] - coords[i][0], coords[i+1][1] - coords[i][1]) 
        for i in range(len(coords) - 1)
    ]

    return distances



# NOTE: possible alterations of this alg would be to:
# add a third and fourth optional parameter per coord line to specify colour 
# and dispensing volume
