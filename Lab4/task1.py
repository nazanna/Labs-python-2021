import math
import pygame

def naklrect(x, y, a, b, fi):
    pygame.draw.polygon(screen, (0, 0, 0), [(x, y), (x + a * math.cos(fi), y + a * math.sin(fi)), (x + a * math.cos(fi) + b * math.cos (math.pi / 2 - fi), y + a * math.sin(fi) - b * math.sin(math.pi / 2 - fi)), (x + b * math.cos (math.pi / 2 - fi), y - b * math.sin(math.pi / 2 - fi)), (x, y)])
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))
screen.fill ([150, 150, 150])

pygame.draw.circle(screen, (255, 255, 0), (400, 300), 150)
pygame.draw.circle(screen, (0, 0, 0), (400, 300), 150, 1)


pygame.draw.circle(screen, (255, 0, 0), (470, 250), 20)
pygame.draw.circle(screen, (0, 0, 0), (470, 250), 20, 1)
pygame.draw.circle(screen, (0, 0, 0), (470, 250), 10)

pygame.draw.circle(screen, (255, 0, 0), (330, 250), 25)
pygame.draw.circle(screen, (0, 0, 0), (330, 250), 25, 1)
pygame.draw.circle(screen, (0, 0, 0), (330, 250), 10)

x = 280
y = 183
a = 100
b = 15
fi = math.pi / 5
naklrect(x, y, a, b, fi)

x = 440
y = 242
a = 100
b = 10
fi = -math.pi / 7
naklrect(x, y, a, b, fi)

pygame.draw.rect(screen, (0, 0, 0), (328, 376, 150, 28))




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
            