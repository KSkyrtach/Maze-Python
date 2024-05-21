from collections import deque
import datetime

maze1 = [
    "\n#######.#######",
    "#.............#",
    "####.#####.##.#",
    "#.#...#....#..#",
    "#.#.#.######..#",
    "#.#.#......#..#",
    "#.#.#.####.#..#",
    "#.#.#...#..##.#",
    "#...######.##.#",
    "#.#...........#",
    "#.#####...###.#",
    "#...#.....#...#",
    "#.###.#######.#",
    "#.............#",
    "###############\n"
]

maze2 = [
    "\n################.####",
    "#...##.##.##.###...##",
    "###.##........###.###",
    "###.###.####......###",
    "###.....#..##.#######",
    "#########..##.####..#",
    "#.......#..##...##..#",
    "###..#.##..###..##..#",
    "#..###.....###..##.##",
    "#..###.###.###..##..#",
    "#...#....####.......#",
    "##..####.####..#..###",
    "###.##.....##.#...###",
    "###....###......#..##",
    "###.#..#######..#####",
    "#.....##....##......#",
    "#.....##........#.#.#",
    "#.#...##..###...#..##",
    "#.....##......#..####",
    "##....##.....##.....#",
    "#####################\n"
]

maze3 = [
    "\n#######.######################",
    "#....#..#....#..#.....###..#.#",
    "#.##.#..#..#.#....#######....#",
    "#....#..#........##...#...#..#",
    "##......####...###......#..###",
    "#..###.......#..#...###......#",
    "#..#.##.#.####..###...#.....##",
    "##.#.#..#.####......#####....#",
    "##.#.#..#.####.#..#...#.#..#.#",
    "#...###...######...........###",
    "###......##....#..###........#",
    "#....#.#.#.....#..#.#..#...###",
    "#.##.##..#.....####...###....#",
    "#.#..#...#.#..#...#....#....##",
    "#.#..#...###..#..#######.....#",
    "###.#..#...#........##...###.#",
    "#...#..#.#.###..###...##.#.#.#",
    "#..##.##.#.......#.....#.....#",
    "#.#...####..###..#.#...####.##",
    "#.#.#....#..#....#.#......#.##",
    "#.#.#.#..#.##..#.###..##..#.##",
    "#...#.#....#...#...#..#...#.##",
    "#..#####..###..##..#...##.##.#",
    "#....#...........#...#.......#",
    "#..#####.#..#.#..#..###.#....#",
    "#..#...#.#..#.#..#...#....#..#",
    "#..#.#.#....#.#..#.#.#...#...#",
    "#..#.#.#.####.####.#.#.#####.#",
    "#.##.#.#....#..###.#....###..#",
    "#....#...#............#......#",
    "##############################\n"
]

print("# - scina\n$ - sciezka\n. - puste pole")
print("\nLabirynty do wyboru:\n1.Labirynt 15X15\n2.Labirynt 21X21\n3.Labirynt 30X30")
a = int(input("Który labirynt wybierasz: "))
maze = []
if a == 1:
    maze = maze1
elif a == 2:
    maze = maze2
elif a == 3:
    maze = maze3

for row in maze:
    print(row)

x = int(input("\nstart x: "))
y = int(input("start y: "))
x1 = int(input("finish x: "))
y1 = int(input("finish y: "))
start = (x, y)
finish = (x1, y1)

startTime = datetime.datetime.now()
def shortest_path(maze, start, finish):
    def is_valid_move(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == '.'

    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    visited[start[0]][start[1]] = True

    queue = deque([(start, [])])

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == finish:
            return path + [(x, y)]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append(((new_x, new_y), path + [(x, y)]))

    return None

def print_maze_with_path(maze, path):
    maze_with_path = [list(row) for row in maze]
    step_counter = 0
    for x, y in path:
        maze_with_path[x][y] = '$'
        step_counter += 1
    for row in maze_with_path:
        print("".join(row))
    return step_counter

path = shortest_path(maze, start, finish)

if path:
    step_count = print_maze_with_path(maze, path)
    print(f"Liczba wykonanych kroków: {step_count}\n")
else:
    print("\nPoczatek lub koniec sa w scianie. Sprobuj ponownie")

endTime = datetime.datetime.now()
timeElapsed = endTime - startTime
seconds = timeElapsed.seconds
microsec = timeElapsed.microseconds
if path:
    print(f"Czas wykonania: {seconds} sekund, {microsec} mikrosekund")