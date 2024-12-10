import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 8
NUTRITIOUS_FRUIT_LIFETIME = 80
POISONOUS_FRUIT_LIFETIME = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def get_random_position():
    return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)


class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)

        if new_head in self.body:
            raise ValueError("Snake collided with itself!")

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        if (self.direction[0] + new_direction[0], self.direction[1] + new_direction[1]) == (0, 0):
            raise ValueError("Illegal move!")
        self.direction = new_direction

    def eat_fruit(self):
        self.grow = True

    def shrink(self):
        if len(self.body) > 1:
            self.body.pop()


class Fruit:
    def __init__(self, position, color, is_poisonous=False):
        self.position = position
        self.color = color
        self.is_poisonous = is_poisonous
        if is_poisonous:
            self.lifetime = POISONOUS_FRUIT_LIFETIME
        else:
            self.lifetime = NUTRITIOUS_FRUIT_LIFETIME

snake = Snake()
fruit = None
score = 0
speed = FPS
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))
            except ValueError as e:
                print(e)
                running = False

    try:
        snake.move()
    except ValueError:
        print("Game over! Snake collided with itself.")
        running = False

    if fruit is None or fruit.lifetime <= 0:
        is_poisonous = random.choice([True, False])
        color = RED if is_poisonous else GREEN
        fruit = Fruit(get_random_position(), color, is_poisonous)

    fruit.lifetime -= 1

    if snake.body[0] == fruit.position:
        if fruit.is_poisonous:
            print("Ate poisonous fruit!")
            snake.shrink()
            score -= 1
        else:
            print("Ate nutritious fruit!")
            snake.eat_fruit()
            score += 1

        fruit = None

    for segment in snake.body:
        x, y = segment
        pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if fruit:
        x, y = fruit.position
        pygame.draw.rect(screen, fruit.color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

    clock.tick(speed)

print(f"Final score: {score}")
pygame.quit()
