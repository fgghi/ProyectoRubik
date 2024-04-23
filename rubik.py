from queue import PriorityQueue

class CubeSolver:
    def __init__(self):
        self.faces = ['U', 'F', 'L', 'R', 'D', 'B']
        self.moves = ['U', 'F', 'L', 'R', 'D', 'B', 'U\'', 'F\'', 'L\'', 'R\'', 'D\'', 'B\'']
        self.cube = {}

    def load_cube_configuration(self, file_path):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if len(lines) != 6:
                    raise ValueError("Invalid cube configuration: Incorrect number of faces")
                for i, line in enumerate(lines):
                    colors = line.strip().split()
                    if len(colors) != 9:
                        raise ValueError(f"Invalid cube configuration: Incorrect number of colors in face {self.faces[i]}")
                    self.cube[self.faces[i]] = colors
        except FileNotFoundError:
            print("Error: File not found")
        except ValueError as e:
            print(f"Error: {e}")

    def print_cube_configuration(self):
        for face in self.faces:
            print(f"{face}: {' '.join(self.cube[face])}")

    def validate_cube_configuration(self):
        colors_count = {color: 0 for color in set(sum(self.cube.values(), []))}
        for face in self.faces:
            for color in self.cube[face]:
                colors_count[color] += 1
        for count in colors_count.values():
            if count != 9:
                return False
        return True

    def heuristic(self, cube_state):
        # Esta heurística es simple y puede ser mejorada para obtener una búsqueda más eficiente
        return 0

    def solve_optimal(self):
        if not self.validate_cube_configuration():
            print("Error: Invalid cube configuration")
            return
        start_state = tuple(self.cube[face] for face in self.faces)
        goal_state = (('U',) * 9, ('F',) * 9, ('L',) * 9, ('R',) * 9, ('D',) * 9, ('B',) * 9)
        frontier = PriorityQueue()
        frontier.put((0, start_state, []))
        explored = set()

        while not frontier.empty():
            cost, current_state, path = frontier.get()
            if current_state == goal_state:
                print("Optimal solution found!")
                print("Steps:", len(path))
                print("Sequence of moves:", path)
                return
            if current_state in explored:
                continue
            explored.add(current_state)
            for move in self.moves:
                next_state = self.apply_move(current_state, move)
                if next_state not in explored:
                    new_cost = len(path) + 1 + self.heuristic(next_state)
                    frontier.put((new_cost, next_state, path + [move]))

    def apply_move(self, state, move):
        next_state = list(list(face) for face in state)

        if move == 'U':
            next_state[0][:3], next_state[2][:3], next_state[1][:3], next_state[5][:3] = \
                next_state[2][:3], next_state[5][:3], next_state[0][:3], next_state[1][:3]
            next_state[4] = self.rotate_face_clockwise(next_state[4])
        elif move == 'U\'':
            next_state[0][:3], next_state[1][:3], next_state[2][:3], next_state[5][:3] = \
                next_state[1][:3], next_state[2][:3], next_state[5][:3], next_state[0][:3]
            next_state[4] = self.rotate_face_counter_clockwise(next_state[4])
        elif move == 'F':
            next_state[0][6:9], next_state[3][:3], next_state[2][6:9], next_state[1][6:9] = \
                next_state[1][6:9], next_state[0][6:9], next_state[3][:3], next_state[2][6:9]
            next_state[5] = self.rotate_face_clockwise(next_state[5])
        elif move == 'F\'':
            next_state[0][6:9], next_state[1][6:9], next_state[2][6:9], next_state[3][:3] = \
                next_state[3][:3], next_state[0][6:9], next_state[1][6:9], next_state[2][6:9]
            next_state[5] = self.rotate_face_counter_clockwise(next_state[5])
        elif move == 'L':
            next_state[0][0::3], next_state[4][0::3], next_state[2][0::3], next_state[5][0::3] = \
                next_state[5][0::3], next_state[0][0::3], next_state[4][0::3], next_state[2][0::3]
            next_state[3] = self.rotate_face_clockwise(next_state[3])
        elif move == 'L\'':
            next_state[0][0::3], next_state[5][0::3], next_state[2][0::3], next_state[4][0::3] = \
                next_state[5][0::3], next_state[2][0::3], next_state[4][0::3], next_state[0][0::3]
            next_state[3] = self.rotate_face_counter_clockwise(next_state[3])
        elif move == 'R':
            next_state[0][2::3], next_state[2][2::3], next_state[4][2::3], next_state[5][2::3] = \
                next_state[5][2::3], next_state[0][2::3], next_state[2][2::3], next_state[4][2::3]
            next_state[1] = self.rotate_face_clockwise(next_state[1])
        elif move == 'R\'':
            next_state[0][2::3], next_state[4][2::3], next_state[2][2::3], next_state[5][2::3] = \
                next_state[4][2::3], next_state[2][2::3], next_state[5][2::3], next_state[0][2::3]
            next_state[1] = self.rotate_face_counter_clockwise(next_state[1])
        elif move == 'D':
            next_state[1][6:9], next_state[2][6:9], next_state[3][6:9], next_state[4][6:9] = \
                next_state[2][6:9], next_state[3][6:9], next_state[4][6:9], next_state[1][6:9]
            next_state[0] = self.rotate_face_clockwise(next_state[0])
        elif move == 'D\'':
            next_state[1][6:9], next_state[4][6:9], next_state[3][6:9], next_state[2][6:9] = \
                next_state[4][6:9], next_state[3][6:9], next_state[2][6:9], next_state[1][6:9]
            next_state[0] = self.rotate_face_counter_clockwise(next_state[0])
        elif move == 'B':
            next_state[0][0:3], next_state[1][0:3], next_state[3][2::-1], next_state[4][0:3] = \
                next_state[1][0:3], next_state[3][2::-1], next_state[4][0:3], next_state[0][0:3]
            next_state[5] = self.rotate_face_clockwise(next_state[5])
        elif move == 'B\'':
            next_state[0][0:3], next_state[4][0:3], next_state[3][2::-1], next_state[1][0:3] = \
                next_state[4][0:3], next_state[3][2::-1], next_state[1][0:3], next_state[0][0:3]
            next_state[5] = self.rotate_face_counter_clockwise(next_state[5])
        return tuple(tuple(face) for face in next_state)

    def rotate_face_clockwise(self, face):
        return [face[6], face[3], face[0], face[7], face[4], face[1], face[8], face[5], face[2]]

    def rotate_face_counter_clockwise(self, face):
        return [face[2], face[5], face[8], face[1], face[4], face[7], face[0], face[3], face[6]]

    def solve_suboptimal(self):
        if not self.validate_cube_configuration():
            print("Error: Invalid cube configuration")
            return
        start_state = tuple(self.cube[face] for face in self.faces)
        goal_state = (('U',) * 9, ('F',) * 9, ('L',) * 9, ('R',) * 9, ('D',) * 9, ('B',) * 9)
        frontier = [([], start_state)]
        explored = set()

        while frontier:
            path, current_state = frontier.pop(0)
            if current_state == goal_state:
                print("Suboptimal solution found!")
                print("Steps:", len(path))
                print("Sequence of moves:", path)
                return
            if current_state in explored:
                continue
            explored.add(current_state)
            for move in self.moves:
                next_state = self.apply_move(current_state, move)
                if next_state not in explored:
                    frontier.append((path + [move], next_state))



solver = CubeSolver()
solver.load_cube_configuration('cube_configuration.txt')
solver.print_cube_configuration()
solver.solve_optimal()
solver.solve_suboptimal()
