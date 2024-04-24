import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class RubiksCubeVisualizer:
    def __init__(self, cube):
        self.cube = cube

    def plot_cube(self):
        colors = {'w': 'white', 'o': 'orange', 'g': 'green', 'r': 'red', 'b': 'blue', 'y': 'yellow'}
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection='3d')

        for x in range(self.cube.n):
            for y in range(self.cube.n):
                for z in range(self.cube.n):
                    color = colors[self.cube.cube[x][y][z]]
                    ax.scatter(x, y, -z, color=color, s=1000, edgecolor='k')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()

class RubiksCube:
    def __init__(self, n=3, colours=['w', 'o', 'g', 'r', 'b', 'y'], state=None):
        if state is None:
            self.n = n
            self.colours = colours
            self.reset()
        else:
            self.n = int((len(state) / 6) ** (.5))
            self.colours = []
            self.cube = [[[]]]
            for i, s in enumerate(state):
                if s not in self.colours:
                    self.colours.append(s)
                self.cube[-1][-1].append(s)
                if len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) < self.n:
                    self.cube[-1].append([])
                elif len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) == self.n and i < len(state) - 1:
                    self.cube.append([[]])

    def reset(self):
        self.cube = [[[c for x in range(self.n)] for y in range(self.n)] for c in self.colours]

    def solved(self):
        for side in self.cube:
            hold = []
            check = True
            for row in side:
                if len(set(row)) == 1:
                    hold.append(row[0])
                else:
                    check = False
                    break
            if not check:
                break
            if len(set(hold)) > 1:
                check = False
                break
        return check

    def stringify(self):
        return ''.join([i for r in self.cube for s in r for i in s])

    def show(self):
        spacing = f'{" " * (len(str(self.cube[0][0])) + 2)}'
        l1 = '\n'.join(spacing + str(c) for c in self.cube[0])
        l2 = '\n'.join('  '.join(str(self.cube[i][j]) for i in range(1, 5)) for j in range(len(self.cube[0])))
        l3 = '\n'.join(spacing + str(c) for c in self.cube[5])
        print(f'{l1}\n\n{l2}\n\n{l3}')

    def horizontal_twist(self, row, direction):
        if row < len(self.cube[0]):
            if direction == 0:
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[2][row],
                                                                                              self.cube[3][row],
                                                                                              self.cube[4][row],
                                                                                              self.cube[1][row])

            elif direction == 1:
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[4][row],
                                                                                              self.cube[1][row],
                                                                                              self.cube[2][row],
                                                                                              self.cube[3][row])
            else:
                print(f'ERROR - direction must be 0 (left) or 1 (right)')
                return
            if direction == 0:
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*reversed(self.cube[0]))]
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*reversed(self.cube[5]))]
            elif direction == 1:
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*self.cube[0])][::-1]
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*self.cube[5])][::-1]
        else:
            print(
                f'ERROR - desired row outside of rubiks cube range. Please select a row between 0-{len(self.cube[0])-1}')
            return

    def vertical_twist(self, column, direction):
        if column < len(self.cube[0]):
            for i in range(len(self.cube[0])):
                if direction == 0:
                    self.cube[0][i][column], self.cube[2][i][column], self.cube[4][-i - 1][-column - 1], \
                    self.cube[5][i][column] = (self.cube[4][-i - 1][-column - 1],
                                               self.cube[0][i][column],
                                               self.cube[5][i][column],
                                               self.cube[2][i][column])
                elif direction == 1:
                    self.cube[0][i][column], self.cube[2][i][column], self.cube[4][-i - 1][-column - 1], \
                    self.cube[5][i][column] = (self.cube[2][i][column],
                                               self.cube[5][i][column],
                                               self.cube[0][i][column],
                                               self.cube[4][-i - 1][-column - 1])
                else:
                    print(f'ERROR - direction must be 0 (down) or 1 (up)')
                    return
            if direction == 0:
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(*self.cube[1])][::-1]
                elif column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(*self.cube[3])][::-1]
            elif direction == 1:
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(*reversed(self.cube[1]))]
                elif column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(*reversed(self.cube[3]))]
        else:
            print(
                f'ERROR - desired column outside of rubiks cube range. Please select a column between 0-{len(self.cube[0])-1}')
            return

    def side_twist(self, column, direction):
        if column < len(self.cube[0]):
            for i in range(len(self.cube[0])):
                if direction == 0:
                    self.cube[0][column][i], self.cube[1][-i - 1][column], self.cube[3][i][-column - 1], \
                    self.cube[5][-column - 1][-1 - i] = (self.cube[3][i][-column - 1],
                                                         self.cube[0][column][i],
                                                         self.cube[5][-column - 1][-1 - i],
                                                         self.cube[1][-i - 1][column])
                elif direction == 1:
                    self.cube[0][column][i], self.cube[1][-i - 1][column], self.cube[3][i][-column - 1], \
                    self.cube[5][-column - 1][-1 - i] = (self.cube[1][-i - 1][column],
                                                         self.cube[5][-column - 1][-1 - i],
                                                         self.cube[0][column][i],
                                                         self.cube[3][i][-column - 1])
                else:
                    print(f'ERROR - direction must be 0 (down) or 1 (up)')
                    return
            if direction == 0:
                if column == 0:
                    self.cube[4] = [list(x) for x in zip(*reversed(self.cube[4]))]
                elif column == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(*reversed(self.cube[2]))]
            elif direction == 1:
                if column == 0:
                    self.cube[4] = [list(x) for x in zip(*self.cube[4])][::-1]
                elif column == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(*self.cube[2])][::-1]
        else:
            print(
                f'ERROR - desired column outside of rubiks cube range. Please select a column between 0-{len(self.cube[0])-1}')
            return

class IDA_star:
    def __init__(self, heuristic, max_depth=10):
        self.max_depth = max_depth
        self.threshold = max_depth
        self.min_threshold = None
        self.heuristic = heuristic
        self.moves = []

    def run(self, state):
        while True:
            status = self.search(state, 1)
            if status:
                return self.moves
            self.moves = []
            self.threshold = self.min_threshold
        return []

    def search(self, state, g_score):
        cube = RubiksCube(state=state)
        if cube.solved():
            return True
        elif len(self.moves) >= self.threshold:
            return False
        min_val = float('inf')
        best_action = None
        for a in [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]:
            cube = RubiksCube(state=state)
            if a[0] == 'h':
                cube.horizontal_twist(a[1], a[2])
            elif a[0] == 'v':
                cube.vertical_twist(a[1], a[2])
            elif a[0] == 's':
                cube.side_twist(a[1], a[2])
            s = cube.stringify()
            if s in self.heuristic:
                h = self.heuristic[s]
            else:
                h = cube.solved()
            if not h and s in self.heuristic:
                h = self.heuristic[s]
            if h is not None:
                f_score = g_score + h
                if f_score < self.threshold:
                    self.moves.append((a[0], a[1], a[2]))
                    status = self.search(s, g_score + 1)
                    if status:
                        return True
                    self.moves.pop()
                if f_score < min_val:
                    min_val = f_score
                    best_action = (a[0], a[1], a[2])
        self.min_threshold = min_val
        return False

def load_cube_state_from_txt(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
        state = ''.join(lines)
    return state

def format_solution(solution):
    formatted_solution = []
    for move in solution:
        face = ""
        if move[0] == "h":
            face = "Horizontal"
        elif move[0] == "v":
            face = "Vertical"
        elif move[0] == "s":
            face = "Side"
        direction = ""
        if move[2] == 0:
            direction = "clockwise"
        else:
            direction = "counter-clockwise"
        formatted_solution.append(f"{face} {direction} ({move[0].upper()}{move[2] if move[2] == 0 else move[2]}')")
    return formatted_solution

if __name__ == "__main__":
    filename = 'cube.txt'
    initial_state = load_cube_state_from_txt(filename)
    print("Estado inicial cargado del archivo:", initial_state)
    heuristic = {
        "wwgwwgrrgoowoowoowggoggyggyyyyrrrrrrrbbwbbwbboobyybyyb": 2,
        "rrrwwwrrrwowwowwowgggggggggyryyryyrybbbbbbbbboooyyyooo": 2,
        "wwwrrrrrrowwowwowwgggggggggyyryyryyrbbbbbbbbbooooooyyy": 2,
        "ooowwwrrryowyowyowgggggggggyrwyrwyrwbbbbbbbbboooyyyrrr": 2,
        "wwwooorrroywoywoywgggggggggywrywrywrbbbbbbbbbooorrryyy": 2,
        "wowwowwowgggoyooyorwrggggggbbbrwrrwroyobbbbbbyyyrrryyy": 2,
        "wwwooowwwoyogggoyogggrwrgggrwrbbbrwrbbboyobbbyyyrrryyy": 2,
        "wwwooowwwoyooyogggggggggrwrrwrrwrbbbbbbbbboyoyryyryyry": 2,
        "wowwowwowbbboyooyooyogggggggggrwrrwrrwrbbbbbbyyyrrryyy": 2,
        "wwwooowwwoyobbboyogggoyogggrwrgggrwrbbbrwrbbbyyyrrryyy": 2,
        "wwwooowwwoyooyobbbggggggoyorwrrwrgggbbbbbbrwryryyryyry": 2,
        "bwwboobwwoooyyyooowggoggwggrwrrwrrwrbbybbrbbygyygrrgyy": 2,
        "wbwobowbwoyooyooyogwggoggwgrwrrwrrwrbybbrbbybygyrgrygy": 2,
        "wwboobwwboyooyooyoggwggoggwrrrwwwrrrybbrbbybbyygrrgyyg": 2,
        "gwwgoogwwoooyyyoooyggrggyggrwrrwrrwrbbwbbobbwbyybrrbyy": 2,
        "wgwogowgwoyooyooyogyggrggygrwrrwrrwrbwbbobbwbybyrbryby": 2,
        "wwgoogwwgoyooyooyoggyggrggyrrrwwwrrrwbbobbwbbyybrrbyyb": 2,
        "rrrooowwwwyowyowyogggggggggrwyrwyrwybbbbbbbbbyyyrrrooo": 2}
    solver = IDA_star(heuristic)
    solution = solver.run(initial_state)
    formatted_solution = format_solution(solution)
    print("Longitud de la solución:", len(formatted_solution))
    print("Solución:")
    for step in formatted_solution:
        print(step)

    rubiks_cube = RubiksCube()
    
    visualizer = RubiksCubeVisualizer(rubiks_cube)
    visualizer.plot_cube()
