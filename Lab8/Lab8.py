# coding:utf-8
import math
from random import choice
from random import randint
from random import randrange
import pygame
import yaml


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Game:
    #класс обработчик игры
    def __init__(self):
        win = False
        with open('Results.yaml') as file:
            data = yaml.load(file)        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        score = 0
        self.balls = []
        targets = []
        number = 0
        sum_number = 0

        clock = pygame.time.Clock()
        gun = Gun()
        for _ in range(2):
            targets.append(SquareTarget(self.screen))

        finished = False
        enter_c = False
        enter_e = False
        final = False
        add_result = False
        enter_name = False
        name = ''

        while not finished:
            self.screen.fill(WHITE)
            live = False
            for target in targets:
                if target.live:
                    live = True
            if enter_name:
                if live:
                    # отрисовка элементов, пока цель не убита
                    for target in targets:
                        target.draw(self.screen)
                        target.move()
                        for target2 in targets[targets.index(target) + 1:]:
                            target.reflect(target2)
                    gun.draw(self.screen)
                    gun.update()
                    write_text(score, self.screen, (10, 10))
                    for ball in self.balls:
                        ball.draw(self.screen)
                        ball.move()
                        for target in targets:
                            if target.hit(ball):
                                score += 1
                                ball.live = False
                        for ball2 in self.balls[self.balls.index(ball) + 1:]:
                            ball.reflect(ball2)
                else:
                    if enter_c:
                        # старт новой игры
                        self.balls = []
                        gun = Gun()
                        targets = []
                        add_result = False
                        for _ in range(2):
                            targets.append(SquareTarget(self.screen))
                        enter_c = False

                    else:
                        if not enter_e:
                            # промежуточное состояние: текущая игра закончилась, ожидание следующих действий
                            write_text('Press C to continue', self.screen, (WIDTH / 2, HEIGHT - 100))
                            write_text('Press E to exit', self.screen, (WIDTH / 2, HEIGHT - 70))
                            # отсутствие текущей игры, демонстрация очков
                            sum_number += number
                            number = 0
                            cel = word_form(score, 'цель', 'цели', 'целей')
                            vistr = word_form(sum_number, 'выстрел', 'выстрела', 'выстрелов')
                            s1 = 'Вы, уважаемый ' + name+' ,'
                            s2 = 'уничтожили ' + str(score) + ' ' + cel + ' за ' + str(sum_number) + ' ' + vistr + '!'
                            write_text(s1, self.screen, (WIDTH / 4, HEIGHT / 2))
                            write_text(s2, self.screen, (WIDTH / 4, HEIGHT / 2 + 30))
                        else:
                            #add results and print table of results
                            if not add_result:
                                add_result = True
                                data['results'].append({'score': score, 'name': name})
                            scores = sorted([[i['score'], i['name']] for i in data['results']])
                            scores.reverse()
                            scores = [[j[1], j[0]] for j in scores]
                            y_of_line = HEIGHT / 3
                            write_text('Table of less losers of game:', self.screen, (20, y_of_line))
                            write_table(scores[0:5], self.screen, (20, y_of_line + 50))                            
            else:
                #ожидание ввода имени
                write_text('Введите имя!!!', self.screen, (100, 100))
                write_text(name, self.screen, (100, 130))
            pygame.display.update()
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            finished = True
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN:
                    # подсчет выстрелов
                    number += gun.reaction(event, self)
                if event.type == pygame.KEYDOWN and not enter_name:
                    if event.key == pygame.K_RETURN:
                        enter_name = True
                    else:
                        if event.key == pygame.K_BACKSPACE:
                            name = name[0:-1]
                        else:
                            name += event.unicode
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    enter_c = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    enter_e = True
                    
        with open('Results.yaml', 'w') as file:
            yaml.dump(data, file)
        pygame.quit()


class Moving_Objects:
    def __init__(self, screen: pygame.Surface, lost, ax, ay, l, color, x=40, y=450, vx=2, vy=0):
        """ Конструктор класса ball
        Args:
        x - начальное положение объекта по горизонтали
        y - начальное положение объекта по вертикали
        vx - начальная горизонтальная скорость объекта
        vy - начальная вертикальная скорость объекта
        lost - потеря скорости при отражении от стены
        ax - ускорение объекта по горизонтали
        ay - ускорение объекта по вертикали
        color - цвет объекта
        l - характерный размер (для круга - радиус, для квадрата - половина длины стороны)
        screen - экран для отрисовки
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.color = color
        self.live = True
        self.lost = lost

    def move(self):
        """
        Перемещение объекта за единицу времени
        """
        dt = 1 / 30
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        # изменение скорости и координат

        if abs(self.x - 800) <= self.l and self.vx > 0:
            self.vx *= -self.lost
        if self.x <= self.l and self.vx < 0:
            self.vx *= -self.lost
        # отражение от вертикальных стен

        if abs(self.y - 600) <= self.l and self.vy > 0 or \
           self.y <= self.l and self.vy < 0:
            self.vy *= -self.lost
        # отражение от горизонтальных стен

    def reflect(self, obj):
        '''
        отражение от других объектов
        obj - объект,с которым проверяется взаимодействие
        '''
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.l + obj.l) ** 2:
            #проверка сближения
            alpha = math.atan((self.y - obj.y) / (self.x - obj.x))
            vpself = self.vy * math.sin(alpha) + self.vx * math.cos(alpha)
            vpobj = obj.vy * math.sin(alpha) + obj.vx * math.cos(alpha)
            #вычисление составляющей скорости, параллельной линии, соединяющей центры шаров
            if vpself * vpobj < 0:
                #изменение сокоростей при сближении
                vparself = -self.vy * math.cos(alpha) + self.vx * math.sin(alpha)
                vparobj = -obj.vy * math.cos(alpha) + obj.vx * math.sin(alpha)
                vpself *= -1
                vpobj *= -1
                self.vx = vparself * math.sin(alpha) + vpself * math.cos(alpha)
                self.vy = - vparself * math.cos(alpha) + vpself * math.sin(alpha)
                obj.vx = vparobj * math.sin(alpha) + vpobj * math.cos(alpha)
                obj.vy = - vparobj * math.cos(alpha) + vpobj * math.sin(alpha)


class Ball(Moving_Objects):
    def __init__(self, screen: pygame.Surface, x=40, y=450, vx=2, vy=0):
        '''
        инициализация класса мячей
        screen - экран для отрисовки
        x - координата x
        y - координата y
        vx - скорость по горизонтали
        vy - скорость по вертикали
        '''
        super().__init__(screen, x=x, y=y, vx=vx, vy=vy, ax=0, ay=40, lost=0.6, color=choice(GAME_COLORS), l=10)
        self.r = self.l

    def move(self):
        '''
        передвижение мяча за единицу времени и смерть в некотором случае
        '''
        # смерть при недостаточной скорости
        if abs(self.y - 600) <= self.r and self.vy ** 2 / 2 / self.ay < self.r:
                self.live = False
        super().move()

    def draw(self, screen):
        '''
        отрисовка мяча
        '''
        if self.live:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )


class Gun:
    def __init__(self):
        '''
        инициализация класса пушек
        '''
        self.cond = False
        self.x = 10
        self.y = 450
        self.power = 4
        self.color = GREY
        self.angle = 0

        # координаты конца пушки
        self.x_final = self.x
        self.y_final = self.y

    def update(self):
        '''
        изменение координат конца пушки при прицеливании
        '''
        if self.cond and self.power < 100:
            self.power += 1
        self.x_final = self.x + self.power ** 0.85 * math.cos(self.angle)
        self.y_final = self.y - self.power ** 0.85 * math.sin(self.angle)

        # изменение цвета пушки при начале прицеливания
        if self.cond:
            self.color = RED

    def draw(self, screen):
        '''
        отрисовка пушки
        '''
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x_final, self.y_final), 10)

    def reaction(self, event, obj):
        '''
        реакции пушки на события:
        движение при движении мышки
        изменение состояния при нажатии клавиши
        отпускание при отпускании клавиши
        event - события
        obj - объект игры
        '''
        if event.type == pygame.MOUSEMOTION:
            self.motion(event)
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
            self.move(event)
        if event.type == pygame.MOUSEBUTTONUP:
            self.up(obj)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.cond = True
            return 1
        else:
            return 0

    def motion(self, event):
        '''
        event - событие pygame
        поворот пушки при прицеливании
        '''
        if event.pos[0] != self.x:
            self.angle = math.atan((-event.pos[1] + self.y) / (event.pos[0] - self.x))

    def up(self, obj):
        '''
        создание мяча, задание ему начальных скоростей при выстеле пушки
        obj - объект текущей игры
        '''
        vx = self.power ** 1.5 * math.cos(self.angle)
        vy = -self.power ** 1.5 * math.sin(self.angle)
        new_ball = Ball(screen=obj.screen, x=self.x_final, y=self.y_final, vx=vx, vy=vy)
        obj.balls.append(new_ball)
        self.power = 4
        self.cond = False

    def move(self, event):
        '''
        движение пушки при тыкании на клавиши
        event - событие тыкания
        '''
        if event.key == pygame.K_RIGHT:
            self.x += 10
        if event.key == pygame.K_LEFT:
            self.x -= 10

class Target(Moving_Objects):
    def __init__(self, screen, lost, ax, ay, x, y, vx, vy, l, color):
        '''
        инициализация класса целей
        Args:
        x - начальное положение объекта по горизонтали
        y - начальное положение объекта по вертикали
        vx - начальная горизонтальная скорость объекта
        vy - начальная вертикальная скорость объекта
        lost - потеря скорости при отражении от стены
        ax - ускорение объекта по горизонтали
        ay - ускорение объекта по вертикали
        color - цвет объекта
        l - характерный размер (для круга - радиус, для квадрата - половина длины стороны)
        screen - экран для отрисовки
        '''
        super().__init__(screen=screen, lost=1, ax=0, ay=0, x=x, y=y, vx=vx, vy=vy, l=l, color=RED)

    def hit(self, ball):
        """
        ball - объект класса мячи
        Попадание шарика в цель
        """
        if (self.x - ball.x) ** 2 + (self.y - ball.y) ** 2 <= (self.l + ball.r) ** 2 and ball.live and self.live:
            self.live = False
            return True


class CircleTarget(Target):
    def __init__(self, screen):
        """ 
        Инициализация новой цели
        screen - экран для отрисовки
        """
        x = randint(500, 780)
        y = randint(300, 550)
        vx = randrange(30, 60)
        vy = randrange(30, 60)
        l = randint(2, 50)
        super().__init__(screen=screen, lost=1, ax=0, ay=0, x=x, y=y, vx=vx, vy=vy, l=l, color=RED)
        self.r = self.l

    def draw(self, screen):
        '''
        отрисовка мяча
        '''
        if self.live:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


class SquareTarget(Target):
    def __init__(self, screen):
        """ 
        Инициализация новой цели
        screen - экран для отрисовки
        """
        x = randint(500, 780)
        y = randint(300, 550)
        vx = randrange(30, 60)
        vy = randrange(30, 60)
        l = randint(2, 50)
        super().__init__(screen=screen, lost=1, ax=0, ay=0, x=x, y=y, vx=vx, vy=vy, l=l, color=RED)

    def draw(self, screen):
        '''
        отрисовка мяча
        '''
        x = self.x - self.l
        y = self.y - self.l
        if self.live:
            pygame.draw.rect(self.screen, self.color, (x, y, self.l * 2, self.l * 2))


def write_text(text, surface, pos):
    '''
    write text on some surface
    text - wanting text
    surface - wanting surface
    pos - (x, y) - coordinates
    '''
    text = str(text)
    f = pygame.font.Font(None, 36)
    text_surface = f.render(text, True, (0, 0, 0))
    surface.blit(text_surface, pos)


def word_form(quantity, form1, form2, form5):
    '''
    форма слова, стоящего после числительного
    quantity - количество (числительное, после которого стоит слово)
    form1 - форма слова, стоящего после 1
    form2 - форма слова, стоящего после 2
    form5 - форма слова, стоящего после 5
    '''
    if quantity // 10 == 1 or quantity % 10 >= 5 or quantity % 10 == 0:
        return form5
    elif quantity % 10 == 1:
        return form1
    else:
        return form2

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

game = Game()
