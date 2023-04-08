import string
from queue import Queue
import matplotlib.pyplot as plt

START = 'S'
END = 'E'
START_HEIGHT = 1
END_HEIGHT = 26

def calculate(lines, part):
    return len(solve(lines)[1])

def solve(lines):
    elevations = create_elevations()
    map_data = parse(lines, elevations)
    height_map = HeightMap(map_data)

    frontier = Queue()
    frontier.put(height_map.start)

    came_from = { height_map.start: None }

    while not frontier.empty():
        current = frontier.get()

        if current == height_map.end:
            break

        for next in height_map.get_neighbours(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    current = height_map.end
    path = []

    while current != height_map.start:
        path.append(current)
        current = came_from[current]

    return height_map, path

def draw_height_map(height_map):
    plt.figure()
    plt.title('Height Map')
    plt.xlabel('X')
    plt.ylabel('Y')
    c = plt.pcolor(height_map.data, edgecolors='k', linewidths=4, cmap='RdBu', vmin=0, vmax=27)
    plt.colorbar(c)
    plt.savefig('heatmap.png')

def create_elevations():
    elevations = { c: i + 1 for i, c in enumerate(string.ascii_lowercase) }
    elevations['S'] = START_HEIGHT
    elevations['E'] = END_HEIGHT

    return elevations

def parse(lines, elevations):
    return [ [ (c, elevations[c]) for c in line ] 
             for line in lines ]

class Location:
    def __init__(self, height):
        self.height = height

class HeightMap:
    VECTORS = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]

    def __init__(self, map_data):
        self.data = map_data
        self.width = len(map_data[0])
        self.height = len(map_data)
        self.start = self.__get_target_position(START)
        self.end = self.__get_target_position(END)

    def get_neighbours(self, location):
        for vector in HeightMap.VECTORS:
            if (neighbour := self.__get_neighbour(location, vector)) \
                and self.__can_visit_neighbour(location, neighbour):
                yield neighbour

    def __get_neighbour(self, location, vector):
        x, y = location[0] + vector[0], location[1] + vector[1]
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return x, y

    def __can_visit_neighbour(self, location, neighbour):
        height_location = self.__get_height_at(*location)
        height_neighbour = self.__get_height_at(*neighbour)
        height_difference = height_neighbour - height_location

        return height_difference <= 1

    def __get_height_at(self, x, y):
        return self.data[y][x][1]

    def __get_target_position(self, letter):
        for row_number, row in enumerate(self.data):
            for col_number, (location_letter, _) in enumerate(row):
                if location_letter == letter:
                    return col_number, row_number

        raise NameError(f"Unable to locate position with letter '{letter}'")