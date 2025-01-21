import random
import matplotlib.pyplot as plt # type: ignore


def generate_maze(width, height):
    # Inicjalizacja labiryntu (1 - ściana, 0 - ścieżka)
    maze = [[1] * width for _ in range(height)]

    # Funkcja DFS
    def dfs_iterative(start_x, start_y):
        stack = [(start_x, start_y)]
        while stack:
            x, y = stack[-1]
            maze[y][x] = 0

            # Losowe kierunki
            directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
            random.shuffle(directions)

            carved = False  # Flaga - czy w tej iteracji zrobiono ścieżkę
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Sprawdzenie, czy nowa pozycja jest w granicach i czy jeszcze nie odwiedzona
                if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == 1:
                    #'Zburzenie' ściany pomiędzy bieżącym polem a nowym
                    maze[y + dy // 2][x + dx // 2] = 0
                    maze[ny][nx] = 0
                    stack.append((nx, ny))
                    carved = True
                    break

            if not carved:
                stack.pop()  # Cofnięcie się, jeśli brak możliwości dalszego kopania

    # Początek w losowym punkcie (nieparzysty)
    start_x = random.randrange(1, width, 2)
    start_y = random.randrange(1, height, 2)
    dfs_iterative(start_x, start_y)

    return maze


def display_maze(maze):
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()


if __name__ == "__main__":
    width = int(input("Podaj szerokość labiryntu (liczba nieparzysta): "))
    height = int(input("Podaj wysokość labiryntu (liczba nieparzysta): "))

    try:
        if width % 2 == 1 and height % 2 == 1:
            maze = generate_maze(width, height)
            display_maze(maze)
        else:
            print("Przynajmniej jedna z podanych liczb jest liczbą parzystą.")
    except ValueError:
        print("Przynajmniej jedna z podanych wartości nie jest liczbą.")

