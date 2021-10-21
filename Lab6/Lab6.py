import pygame
import random
import yaml

pygame.init()

FPS = 10
screen_color = (130, 219, 91)
display_size = (1200, 700)
screen = pygame.display.set_mode(display_size)
screen.fill(screen_color)


class Ball:
    def __init__(self):
        '''
        init method to class Ball
        '''
        max_velocity = 5
        self.coords = [random.randint(0, 900), random.randint(0, 600)]
        # coordinates of center
        self.color = (random.randint(0, 255), random.randint(0, 255),
                      random.randint(0, 255))  # color
        self.velocity = [random.randint(-max_velocity, max_velocity),
                         random.randint(-max_velocity, max_velocity)]
        # velocity
        self.r = random.randint(10, 40)  # radius
        self.life = True  # indicator of existence

    def move(self):
        '''
        move ball
        '''
        self.coords = [self.coords[0] + self.velocity[0],
                       self.coords[1] + self.velocity[1]]
        # change coordinates
        self.reflection(pygame.display.get_surface().get_size())

    def reflection(self, BORDER_EDGERS):
        '''
        reflection from wall
        '''
        wall_l = abs(self.coords[0] - 0) <= self.r
        wall_r = abs(self.coords[0] - BORDER_EDGERS[0]) <= self.r
        if wall_l and self.velocity[0] < 0 or wall_r and self.velocity[0] > 0:
            self.velocity[0] *= -1

        wall_u = abs(self.coords[1] - 0) <= self.r
        wall_d = abs(self.coords[1] - BORDER_EDGERS[1]) <= self.r
        if wall_u and self.velocity[1] < 0 or wall_d and self.velocity[1] > 0:
            self.velocity[1] *= -1

    def drawing(self, surface):
        '''
        draw ball
        '''
        if self.life:
            pygame.draw.circle(surface, self.color, self.coords, self.r)

    def reaction(self, event):
        '''
        reaction to some mouse actions
        '''
        type_mouse = event.type == pygame.MOUSEBUTTONDOWN
        if type_mouse:
            mouse_ball_x = (event.pos[0] - self.coords[0]) ** 2
            mouse_ball_y = (event.pos[1] - self.coords[1]) ** 2
            hit = mouse_ball_x + mouse_ball_y <= self.r ** 2
        if self.life and type_mouse and event.button == 1 and hit:
            self.life = False
            return (10 // self.r) + (self.velocity[0] ** 2 +
                                     self.velocity[1] ** 2) ** 0.5 / 5 + 1
        # score for this event
        else:
            return 0


class Ellipse:
    def __init__(self):
        '''
        init method to class Ellipse
        '''
        max_velocity = 5
        self.coords = [random.randint(0, 600), random.randint(0, 600)]
        # coordinates of left corner
        self.color = (random.randint(0, 255), random.randint(0, 255),
                      random.randint(0, 255))
        self.velocity = [random.randint(-max_velocity, max_velocity),
                         random.randint(-max_velocity, max_velocity)]
        # velocity
        self.size = (random.randint(10, 100), random.randint(10, 100))
        # weight and height of rectangle over ellipse
        self.life = True

    def move(self):
        '''
        move ellipse
        '''
        self.coords = [self.coords[0] + self.velocity[0],
                       self.coords[1] + self.velocity[1]]
        # change coordinates
        self.reflection(pygame.display.get_surface().get_size())

    def reflection(self, BORDER_EDGERS):
        '''
        reflection from wall
        '''
        ellipse_wall_r = abs(self.coords[0] - BORDER_EDGERS[0]) <= self.size[0]
        ellipse_wall_l = self.coords[0] <= 0
        if ellipse_wall_l and self.velocity[0] < 0 or (
           ellipse_wall_r and self.velocity[0] > 0):
            self.velocity[0] *= -1

        ellipse_wall_u = abs(self.coords[1] - BORDER_EDGERS[1]) <= self.size[1]
        ellipse_wall_d = self.coords[1] <= 0
        if ellipse_wall_d and self.velocity[1] < 0 or (
           ellipse_wall_u and self.velocity[1] > 0):
            self.velocity[1] *= -1

    def drawing(self, surface):
        '''
        draw ellipse
        '''
        if self.life:
            pygame.draw.ellipse(screen, self.color,
                                tuple([self.coords, self.size]))

    def reaction(self, event):
        '''
        reaction to some mouse actions
        '''
        type_mouse = event.type == pygame.MOUSEBUTTONDOWN
        if type_mouse:
            mouse_ellipse_x = event.pos[0] - self.coords[0] - self.size[0] / 2
            hit_x = abs(mouse_ellipse_x) <= self.size[0] / 2
            mouse_ellipse_y = event.pos[1] - self.coords[1] - self.size[1] / 2
            hit_y = abs(mouse_ellipse_y) <= self.size[1] / 2

        if self.life and type_mouse and event.button == 1 and hit_x and hit_y:
            self.life = False
            score = (self.velocity[0] ** 2 + self.velocity[1] ** 2) ** 0.5 / 5
            return 1 + score
        # score for this event
        else:
            return 0


class Lama:
    def __init__(self):
        '''
        init method to class Lama
        '''
        max_velocity = 5
        self.color = (random.randint(0, 255), random.randint(0, 255),
                      random.randint(0, 255))
        self.velocity = [random.randint(-max_velocity * 10,
                                        max_velocity * 10) / 10, 0]
        self.size = random.randrange(4, 10) / 10
        # size of lama
        lama_rect = pygame.image.load('Lama.png').get_rect()
        self.size_rect = [self.size * lama_rect.width,
                          self.size * lama_rect.height]
        # lama's rectangle
        self.coords = (random.randrange(0, display_size[0]),
                       random.randrange(int(self.size_rect[1]),
                       int(int(display_size[1] - 0.5 * self.size_rect[1]))))
        # lama's coordinates
        self.life = True

    def move(self):
        '''
        move lama
        '''
        self.coords = [self.coords[0] + self.velocity[0],
                       self.coords[1] + self.velocity[1]]
        # change coordinates
        self.reflection(pygame.display.get_surface().get_size())

    def reflection(self, BORDER_EDGERS):
        '''
        reflection from wall
        '''
        wall_l = (self.coords[0] - self.size_rect[0]) <= 0
        wall_r = abs(self.coords[0] - BORDER_EDGERS[0]) <= self.size_rect[0]
        if wall_l and self.velocity[0] < 0 or wall_r and self.velocity[0] > 0:
            self.velocity[0] *= -1

        wall_u = (self.coords[1] - self.size_rect[1]) <= 0
        wall_d = abs(self.coords[1] - BORDER_EDGERS[1]) <= self.size_rect[1]
        if wall_u and self.velocity[1] < 0 or wall_d and self.velocity[1] > 0:
            self.velocity[1] *= -1

    def drawing(self, surface):
        '''
        draw lama
        '''
        if self.life:
            lama_surface = pygame.image.load('Lama.png')
            if self.velocity[0] < 0:
                lama_surface = pygame.transform.flip(lama_surface, True, False)
            lama_surface = pygame.transform.rotozoom(lama_surface, 0, self.size)
            lama_surface.set_colorkey((175, 221, 233))
            surface.blit(lama_surface, lama_surface.get_rect(center=self.coords))

    def reaction(self, event):
        '''
        reaction to some mouse actions
        '''
        mouse_type = event.type == pygame.MOUSEBUTTONDOWN
        if mouse_type:
            hit_x = abs(event.pos[0] - self.coords[0]) <= self.size_rect[0] / 2
            hit_y = abs(event.pos[1] - self.coords[1]) <= self.size_rect[1] / 2
        if self.life and mouse_type and event.button == 1 and hit_x and hit_y:
            self.life = False
            return -2  # score for this event
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


def write_table(array, surface, pos):
    '''
    write table on some surface
    text - wanting text
    surface - wanting surface
    pos - (x, y) - coordinates of left corner
    '''
    font = pygame.font.Font(None, 36)
    line_size = [0 for _ in array[0]]
    # array of size of columns of table
    for i in array:
        for j in i:
            if font.size(str(j))[0] > line_size[i.index(j)]:
                line_size[i.index(j)] = font.size(str(j))[0]
    line_size = [i + font.size('   ')[0] for i in line_size]

    y_of_line = pos[1]
    line_delta = 0
    for i in array:
        for j in i:
            write_text(str(j), surface, (pos[0] + line_delta, y_of_line))
            line_delta += line_size[i.index(j)]
        y_of_line += 30
        line_delta = 0
    # print table on the surface

pool = []
n = random.randint(2, 40)
number_of_objects = n
number_of_lamas = 0
for _ in range(n):
    k = random.randint(0, 3)
    if k % 3 == 0:
        pool.append(Ball())
    elif k % 3 == 1:
        pool.append(Ellipse())
    else:
        pool.append(Lama())
        number_of_lamas += 1
# making pool of objects class Ball, Ellipse and Lama

score = 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

name = ''
enter_name = False

# take information about previous games
with open('Results.yaml') as file:
    data = yaml.load(file)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            # exit in game
        if event.type == pygame.KEYDOWN:
            # expectation of player's name
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                enter_name = True
            elif event.key == pygame.K_BACKSPACE:
                name = name[0:-1]
            else:
                name += event.unicode
        else:
            # react for some action of mouse
            for i in range(n):
                reaction = pool[i].reaction(event)
                if reaction != 0:
                    number_of_objects -= 1
                if reaction < 0:
                    number_of_lamas -= 1
                score += int(reaction)

    if enter_name:
        if number_of_objects <= number_of_lamas:
            # final of the game
            write_text('Good job, ' + name + '!', screen,
                       (display_size[0] / 2, display_size[1] / 3))
            write_text('Score: ' + str(score), screen,
                       (display_size[0] / 2, display_size[1] / 3 + 40))
            # write motivation text

            data['results'].append({'score': score, 'name': name})
            scores = sorted([[i['score'], i['name']] for i in data['results']])
            scores.reverse()
            scores = [[j[1], j[0]] for j in scores]
            y_of_line = display_size[1] / 3
            write_text('Table of less losers of game:', screen, (20, y_of_line))
            write_table(scores[0:5], screen, (20, y_of_line + 50))
            # print table with best results

        else:
            for i in range(n):
                pool[i].move()
                pool[i].drawing(screen)
                # draw objects from pool

            write_text('Score: ' + str(score), screen,
                       (display_size[0] - 160, display_size[1] - 100))
        # write text about score

    else:
        write_text('Enter your name: ', screen,
                   (display_size[0] / 3, display_size[1] / 3))
        write_text(name, screen, (display_size[0] / 3, display_size[1] / 2))
        write_text("Don't touch lamas!", screen,
                   (display_size[0] / 3, 2 * display_size[1] / 3))
        # expectation of writing player's name

    pygame.display.update()
    screen.fill(screen_color)

# write score information in file
with open('Results.yaml', 'w') as file:
    yaml.dump(data, file)
pygame.quit()
