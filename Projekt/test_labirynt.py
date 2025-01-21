import unittest
from labirynt import generate_maze # type: ignore

class TestMazeGeneration(unittest.TestCase):

    def test_maze_dimensions(self):
        """Test, czy labirynt ma odpowiednie wymiary."""
        width, height = 21, 21
        maze = generate_maze(width, height)
        self.assertEqual(len(maze), height, "Wysokość labiryntu jest niepoprawna")
        self.assertTrue(all(len(row) == width for row in maze), "Szerokość labiryntu jest niepoprawna")

    def test_maze_borders(self):
        """Test, czy ramy labiryntu są ścianami."""
        width, height = 21, 21
        maze = generate_maze(width, height)
        # Sprawdź górną i dolną ramkę
        self.assertTrue(all(cell == 1 for cell in maze[0]), "Górna ramka nie jest ścianą")
        self.assertTrue(all(cell == 1 for cell in maze[-1]), "Dolna ramka nie jest ścianą")
        # Sprawdź lewą i prawą ramkę
        self.assertTrue(all(row[0] == 1 for row in maze), "Lewa ramka nie jest ścianą")
        self.assertTrue(all(row[-1] == 1 for row in maze), "Prawa ramka nie jest ścianą")

    def test_maze_connectivity(self):
        """Test, czy wszystkie ścieżki są ze sobą połączone."""
        width, height = 21, 21
        maze = generate_maze(width, height)

        # BFS do sprawdzania połączenia
        def bfs(start):
            queue = [start]
            visited = set([start])
            while queue:
                x, y = queue.pop(0)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            return visited

        # Znajdź pierwszą komórkę ścieżki
        start = next((x, y) for y in range(height) for x in range(width) if maze[y][x] == 0)
        visited_cells = bfs(start)

        # Policz wszystkie ścieżki
        path_cells = sum(row.count(0) for row in maze)
        self.assertEqual(len(visited_cells), path_cells, "Labirynt ma odizolowane ścieżki")


if __name__ == "__main__":
    unittest.main()