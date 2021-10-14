import pygame
import random

pygame.init()

FPS = 10
screen_color = (255, 255, 255)
screen = pygame.display.set_mode((1200, 700))
screen.fill(screen_color)


class Ball:
    def __init__(self):
        '''
        init method to class Ball
        '''
        max_velocity = 5
        self.coords = [random.randint(0, 900), random.randint(0, 600)]  # coordinates of center
        self.color = (random.randint(0, 255), random.randint(0, 255),
                      random.randint(0, 255))  # color
        self.velocity = [random.randint(-max_velocity, max_velocity),
                         random.randint(-max_velocity, max_velocity)]  # velocity
        self.r = random.randint(10, 40)  # radius
        self.life = True  # indicator of existence

    def move(self):
        '''
        move ball
        '''
        self.coords = [self.coords[0] + self.velocity[0],
                       self.coords[1] + self.velocity[1]]
        self.reflection(pygame.display.get_surface().get_size())

    def reflection(self, BORDER_EDGERS):
        '''
        reflection from wall
        '''
        if abs(self.coords[0] - 0) <= self.r  and self.velocity[0] < 0 or (
            abs(self.coords[0] - BORDER_EDGERS[0]) <= self.r and  self.velocity[0] > 0):
            self.velocity[0] *= -1

        if abs(self.coords[1] - 0) <= self.r  and self.velocity[1] < 0 or (
            abs(self.coords[1] - BORDER_EDGERS[1]) <= self.r and  self.velocity[1] > 0):
            self.velocity[1] *= -1

    def drawing(self, surface):
        '''
        draw ball
        '''
        if self.life:
            pygame.draw.circle(surface, self.color, self.coords, self.r)

    def reaction(self, event):
        '''
        reaction to some actions
        '''
        if self.life and (
                event.type == pygame.MOUSEBUTTONDOWN) and event.button == 1 and (
                event.pos[0] - self.coords[0]) ** 2 + (
                event.pos[1] - self.coords[1]) ** 2 <= self.r ** 2:
            self.life = False
            return (10 // self.r) + (self.velocity[0] ** 2 +
                                     self.velocity[1] ** 2) ** 0.5 / 5 + 1  # score for this event
        else:
            return 0


class Ellipse:
    def __init__(self):
        '''
        init method to class Ball
        '''
        max_velocity = 5
        self.coords = [random.randint(0, 600), random.randint(0, 600)]
        self.color = (random.randint(0, 255), random.randint(0, 255),
                      random.randint(0, 255))
        self.velocity = [random.randint(-max_velocity, max_velocity),
                         random.randint(-max_velocity, max_velocity)]
        self.size = (random.randint(10, 100), random.randint(10, 100))
        self.life = True

    def move(self):
        '''
        move ball
        '''
        self.coords = [self.coords[0] + self.velocity[0],
                       self.coords[1] + self.velocity[1]]
        self.reflection(pygame.display.get_surface().get_size())

    def reflection(self, BORDER_EDGERS):
        '''
        reflection from wall
        '''
        if self.coords[0] <= 0 and self.velocity[0] < 0 or (
            abs(self.coords[0] - BORDER_EDGERS[0]) <= self.size[0] and self.velocity[0] > 0):
            self.velocity[0] *= -1

        if self.coords[1] <= 0 and self.velocity[1] < 0 or (
            abs(self.coords[1] - BORDER_EDGERS[1]) <= self.size[1] and self.velocity[1] > 0):
            self.velocity[1] *= -1

    def drawing(self, surface):
        '''
        draw ball
        '''
        if self.life:
            pygame.draw.ellipse(screen, self.color, tuple([self.coords, self.size]))

    def reaction(self, event):
        '''
        reaction to some actions
        '''
        if self.life and event.type == pygame.MOUSEBUTTONDOWN and (
                event.button == 1) and abs(
            event.pos[0] - self.coords[0] - self.size[0] / 2) <= self.size[0] / 2 and abs(
            event.pos[1] - self.coords[1] - self.size[1] / 2) ** 2 <= self.size[1] / 2:
            self.life = False
            return 1 + (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** 0.5 / 5 + 1  # score for this event
        else:
            return 0


def write_text(text, surface, pos):
    '''
    write text on some surface
    text - wanting text
    surface - wanting surface
    pos - (x, y) - coordinates
    '''
    f = pygame.font.Font(None, 36)
    text_surface = f.render(text, True, (0, 0, 0))
    surface.blit(text_surface, pos)


pool = []
n = random.randint(2, 30)
number_of_existing = n
for _ in range(n):
    k = random.randint(0, 2)
    if k == 0:
        pool.append(Ball())
    else:
        pool.append(Ellipse())
# making pool of objects class Ball and Ellipse

score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

name = ''
enter_name = False
display_size_x = pygame.display.get_surface().get_size()[0]
display_size_y = pygame.display.get_surface().get_size()[1]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            # exit in game
        if event.type == pygame.KEYDOWN:
            # expectation of player's name
            if event.key == pygame.K_KP_ENTER:
                enter_name = True
            else:
                name += event.unicode
        else:
            # react for some action of mouse
            for i in range(n):
                reaction = pool[i].reaction(event)
                if reaction > 0:
                    number_of_existing -= 1
                score += int(reaction)

    if enter_name:
        for i in range(n):
            pool[i].move()
            pool[i].drawing(screen)
            # draw objects from pool

        if number_of_existing == 0:
            write_text('Good job, ' + name + '!', screen,
                       (display_size_x / 2 - 100, display_size_y / 2 - 100))
            write_text('Score: ' + str(score), screen,
                       (display_size_x / 2 - 100, display_size_y / 2))

        else:
            write_text('Score: ' + str(score), screen,
                       (display_size_x - 160, display_size_y - 100))
        # write text about score

    else:
        write_text('Enter your name: ', screen,
                   (display_size_x / 3, display_size_y / 3))
        write_text(name, screen, (display_size_x / 3, display_size_y / 2))
        # expectation of writing player's name

    pygame.display.update()
    screen.fill(screen_color)

# write score information in file
file = open('Results.txt', 'a')
print(name, score, file=file)
file.close()
pygame.quit()
