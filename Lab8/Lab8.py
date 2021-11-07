import math
from random import choice
from random import randint
from random import randrange
import pygame


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
    def __init__(self):
        win = False
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
                    # ��������� ���������, ���� ���� �� �����
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
                        # ����� ����� ����
                        self.balls = []
                        gun = Gun()
                        targets = []
                        for _ in range(2):
                            targets.append(SquareTarget(self.screen))
                        enter_c = False

                    else:
                        if not enter_e:
                            # ������������� ���������: ������� ���� �����������, �������� ��������� ��������
                            write_text('Press C to continue', self.screen, (WIDTH / 2, HEIGHT - 100))
                            write_text('Press E to exit', self.screen, (WIDTH / 2, HEIGHT - 70))

                        # ���������� ������� ����, ������������ �����
                        sum_number += number
                        number = 0
                        cel = word_form(score, '����', '����', '�����')
                        vistr = word_form(sum_number, '�������', '��������', '���������')
                        s1 = '��, ���������, ' + name
                        s2 = '���������� ' + str(score) + ' ' + cel + ' �� ' + str(sum_number) + ' ' + vistr + '!'
                        write_text(s1, self.screen, (WIDTH / 4, HEIGHT / 2))
                        write_text(s2, self.screen, (WIDTH / 4, HEIGHT / 2 + 30))
            else:
                write_text('������� ���!!!', self.screen, (100, 100))
                write_text(name, self.screen, (100, 130))
            pygame.display.update()
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            finished = True
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    # ������� ���������
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

        pygame.quit()


class Moving_Objects:
    def __init__(self, screen: pygame.Surface, lost, ax, ay, l, color, x=40, y=450, vx=2, vy=0):
        """ ����������� ������ ball
        Args:
        x - ��������� ��������� ������� �� �����������
        y - ��������� ��������� ������� �� ���������
        vx - ��������� �������������� �������� �������
        vy - ��������� ������������ �������� �������
        lost - ������ �������� ��� ��������� �� �����
        ax - ��������� ������� �� �����������
        ay - ��������� ������� �� ���������
        color - ���� �������
        l - ����������� ������ (��� ����� - ������, ��� �������� - �������� ����� �������)
        screen - ����� ��� ���������
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
        ����������� ������� �� ������� �������
        """
        dt = 1 / 30
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        # ��������� �������� � ���������

        if abs(self.x - 800) <= self.l and self.vx > 0:
            self.vx *= -self.lost
        if self.x <= self.l and self.vx < 0:
            self.vx *= -self.lost
        # ��������� �� ������������ ����

        if abs(self.y - 600) <= self.l and self.vy > 0 or \
           self.y <= self.l and self.vy < 0:
            self.vy *= -self.lost
        # ��������� �� �������������� ����

    def reflect(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.l + obj.l) ** 2:
            alpha = math.atan((self.y - obj.y) / (self.x - obj.x))
            vpself = self.vy * math.sin(alpha) + self.vx * math.cos(alpha)
            vpobj = obj.vy * math.sin(alpha) + obj.vx * math.cos(alpha)
            if vpself * vpobj < 0:
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
        ������������� ������ �����
        '''
        super().__init__(screen, x=x, y=y, vx=vx, vy=vy, ax=0, ay=40, lost=0.6, color=choice(GAME_COLORS), l=10)
        self.r = self.l

    def move(self):
        '''
        ������������ ���� �� ������� ������� � ������ � ��������� ������
        '''
        # ������ ��� ������������� ��������
        if abs(self.y - 600) <= self.r and self.vy ** 2 / 2 / self.ay < self.r:
                self.live = False
        super().move()

    def draw(self, screen):
        '''
        ��������� ����
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
        ������������� ������ �����
        '''
        self.cond = False
        self.x = 10
        self.y = 450
        self.power = 4
        self.color = GREY
        self.angle = 0

        # ���������� ����� �����
        self.x_final = self.x
        self.y_final = self.y

    def update(self):
        '''
        ��������� ��������� ����� ����� ��� ������������
        '''
        if self.cond and self.power < 100:
            self.power += 1
        self.x_final = self.x + self.power ** 0.85 * math.cos(self.angle)
        self.y_final = self.y - self.power ** 0.85 * math.sin(self.angle)

        # ��������� ����� ����� ��� ������ ������������
        if self.cond:
            self.color = RED

    def draw(self, screen):
        '''
        ��������� �����
        '''
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x_final, self.y_final), 10)

    def reaction(self, event, obj):
        '''
        ������� ����� �� �������:
        �������� ��� �������� �����
        ��������� ��������� ��� ������� �������
        ���������� ��� ���������� �������
        '''
        if event.type == pygame.MOUSEMOTION:
            self.motion(event)
        if event.type == pygame.MOUSEBUTTONUP:
            self.up(obj)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.cond = True
            return 1
        else:
            return 0

    def motion(self, event):
        '''
        event - ������� pygame
        ������� ����� ��� ������������
        '''
        if event.pos[0] != self.x:
            self.angle = math.atan((-event.pos[1] + self.y) / (event.pos[0] - self.x))

    def up(self, obj):
        '''
        �������� ����, ������� ��� ��������� ��������� ��� ������� �����
        '''
        vx = self.power ** 1.5 * math.cos(self.angle)
        vy = -self.power ** 1.5 * math.sin(self.angle)
        new_ball = Ball(screen=obj.screen, x=self.x_final, y=self.y_final, vx=vx, vy=vy)
        obj.balls.append(new_ball)
        self.power = 4
        self.cond = False


class Target(Moving_Objects):
    def __init__(self, screen, lost, ax, ay, x, y, vx, vy, l, color):
        '''
        ������������� ������ �����
        Args:
        x - ��������� ��������� ������� �� �����������
        y - ��������� ��������� ������� �� ���������
        vx - ��������� �������������� �������� �������
        vy - ��������� ������������ �������� �������
        lost - ������ �������� ��� ��������� �� �����
        ax - ��������� ������� �� �����������
        ay - ��������� ������� �� ���������
        color - ���� �������
        l - ����������� ������ (��� ����� - ������, ��� �������� - �������� ����� �������)
        screen - ����� ��� ���������
        '''
        super().__init__(screen=screen, lost=1, ax=0, ay=0, x=x, y=y, vx=vx, vy=vy, l=l, color=RED)

    def hit(self, ball):
        """
        ball - ������ ������ ����
        ��������� ������ � ����
        """
        if (self.x - ball.x) ** 2 + (self.y - ball.y) ** 2 <= (self.l + ball.r) ** 2 and ball.live and self.live:
            self.live = False
            return True


class CircleTarget(Target):
    def __init__(self, screen):
        """ 
        ������������� ����� ����
        screen - ����� ��� ���������
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
        ��������� ����
        '''
        if self.live:
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


class SquareTarget(Target):
    def __init__(self, screen):
        """ 
        ������������� ����� ����
        screen - ����� ��� ���������
        """
        x = randint(500, 780)
        y = randint(300, 550)
        vx = randrange(30, 60)
        vy = randrange(30, 60)
        l = randint(2, 50)
        super().__init__(screen=screen, lost=1, ax=0, ay=0, x=x, y=y, vx=vx, vy=vy, l=l, color=RED)

    def draw(self, screen):
        '''
        ��������� ����
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
    ����� �����, �������� ����� �������������
    quantity - ���������� (������������, ����� �������� ����� �����)
    form1 - ����� �����, �������� ����� 1
    form2 - ����� �����, �������� ����� 2
    form5 - ����� �����, �������� ����� 5
    '''
    if quantity // 10 == 1 or quantity % 10 >= 5 or quantity % 10 == 0:
        return form5
    elif quantity % 10 == 1:
        return form1
    else:
        return form2


game = Game()
