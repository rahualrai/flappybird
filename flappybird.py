import pygame
import random

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy Bird')

background_img = pygame.image.load('background.jpeg')
bird_img = pygame.image.load('bird.png')

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.gravity = 0.5
    
    def update(self):
        self.vel += self.gravity
        self.y += self.vel
    
    def draw(self):
        game_window.blit(bird_img, (self.x, self.y))

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.top_pipe = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_pipe = pygame.Rect(self.x, self.height + 150, 50, WINDOW_HEIGHT - self.height - 150)
    
    def update(self):
        self.x -= 3
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x
    
    def draw(self):
        pygame.draw.rect(game_window, (0, 255, 0), self.top_pipe)
        pygame.draw.rect(game_window, (0, 255, 0), self.bottom_pipe)

pipes = []
for i in range(3):
    pipe = Pipe(WINDOW_WIDTH + i * 200)
    pipes.append(pipe)

clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)
game_over = False
bird = Bird(1, 200)
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.vel = -9
    
    bird.update()
    
    for pipe in pipes:
        pipe.update()
    
    if pipes[-1].x < WINDOW_WIDTH - 200:
        pipe = Pipe(WINDOW_WIDTH)
        pipes.append(pipe)
    
    for pipe in pipes:
        if bird.x + bird_img.get_width() > pipe.x and bird.x < pipe.x + 50:
            if bird.y < pipe.height or bird.y + bird_img.get_height() > pipe.height + 150:
                game_over = True
    
    game_window.blit(background_img, (0, 0))
    for pipe in pipes:
        pipe.draw()
    bird.draw()

    for pipe in pipes:
        if bird.x > pipe.x + 50:
            score += 1
            pipes.remove(pipe)

    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    game_window.blit(score_text, (10, 10))

    pygame.display.update()

    clock.tick(60)

    if game_over:
        game_over_text1 = font.render('Game Over!', True, (255, 0, 0))
        game_over_text2 = font.render('Press R to replay, Esc to quit', True, (255, 0, 0))
        game_window.blit(game_over_text1, (WINDOW_WIDTH // 2 - game_over_text1.get_width() // 2, WINDOW_HEIGHT // 2 - game_over_text1.get_height()))
        game_window.blit(game_over_text2, (WINDOW_WIDTH // 2 - game_over_text2.get_width() // 2, WINDOW_HEIGHT // 2))
        pygame.display.update()

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        pipes = []
                        for i in range(3):
                            pipe = Pipe(WINDOW_WIDTH + i * 200)
                            pipes.append(pipe)
                        score = 0
                        bird = Bird(1, 50)
                        game_over = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
