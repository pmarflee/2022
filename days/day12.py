import string
from abc import ABC, abstractmethod
from queue import SimpleQueue

START = 'S'
END = 'E'
START_HEIGHT = 1
END_HEIGHT = 26

def calculate(lines, part):
    elevations = create_elevations()
    map_data = parse(lines, elevations)
    height_map = HeightMap(map_data)

    match part:
        case 1:
            solver = Part1Solver(height_map)
        case 2:
            solver = Part2Solver(height_map)
        case _:
            raise ValueError('Invalid part')

    return solver.solve()

def create_elevations():
    elevations = { c: i + 1 for i, c in enumerate(string.ascii_lowercase) }
    elevations['S'] = START_HEIGHT
    elevations['E'] = END_HEIGHT

    return elevations

def parse(lines, elevations):
    return [ [ (c, elevations[c]) for c in line ] 
             for line in lines ]

class HeightMap:
    VECTORS = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]

    def __init__(self, map_data):
        self.data = map_data
        self.width = len(map_data[0])
        self.height = len(map_data)

    def get_position(self, letter):
        for row_number, row in enumerate(self.data):
            for col_number, (position_letter, _) in enumerate(row):
                if position_letter == letter:
                    return col_number, row_number

        raise NameError(f"Unable to locate position with letter '{letter}'")

    def get_neighbours(self, position):
        return (neighbour for vector in HeightMap.VECTORS 
                if (neighbour := self.__get_neighbour(position, vector)) != None)

    def __get_neighbour(self, position, vector):
        x, y = position[0] + vector[0], position[1] + vector[1]
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return x, y

    def get_details_at_position(self, x, y):
        return self.data[y][x]

class Solver(ABC):
    def __init__(self, height_map, start_letter):
        self.height_map = height_map
        self.start_position = height_map.get_position(start_letter)

    @abstractmethod
    def can_visit_neighbour(self, height_from, height_to):
        pass

    @abstractmethod
    def is_target(self, letter, height):
        pass

    def solve(self):
        frontier = SimpleQueue()
        frontier.put(self.start_position)

        came_from = { self.start_position: None }

        while not frontier.empty():
            current = frontier.get()
            letter_current, height_current = self.height_map.get_details_at_position(*current)

            if self.is_target(letter_current, height_current):
                break

            for next in self.height_map.get_neighbours(current):
                if next not in came_from:
                    _, height_next = self.height_map.get_details_at_position(*next)
                    if self.can_visit_neighbour(height_current, height_next):
                        frontier.put(next)
                        came_from[next] = current

        path = []

        while current != self.start_position:
            path.append(current)
            current = came_from[current]

        return len(path)

class Part1Solver(Solver):
    def __init__(self, height_map):
        super().__init__(height_map, START)
    
    def is_target(self, letter, height):
        return letter == END

    def can_visit_neighbour(self, height_from, height_to):
         return height_to - height_from <= 1

class Part2Solver(Solver):
    def __init__(self, height_map):
        super().__init__(height_map, END)
    
    def is_target(self, letter, height):
        return height == 1

    def can_visit_neighbour(self, height_from, height_to):
         return height_from - height_to <= 1