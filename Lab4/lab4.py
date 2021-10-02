import pygame

pygame.init()


surface1 = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)
def noga(x, y, size):
    pygame.draw.ellipse(surface1, (255, 255, 255), (x + 20 * size, y + 40 * size, 25 * size, 55 * size))
    pygame.draw.ellipse(surface1, (255, 255, 255), (x + 20 * size, y + 90 * size, 25 * size, 55 * size))
    pygame.draw.ellipse(surface1, (255, 255, 255), (x + 25 * size, y + 144 * size, 25 * size, 16 * size))
    
def lama(x = 0, y = 140, size = 1):
    pygame.draw.ellipse(surface1, (255, 255, 255), (x, y, 180 * size, 80 * size))
    noga(x, y, size)
    noga(x + 35 * size, y + 20 * size, size)
    noga(x + 85 * size, y - 8 * size, size)
    noga(x + 120 * size, y + 20 * size, size) 
    pygame.draw.ellipse(surface1, (255, 255, 255), (x + 145 * size, y - 105 * size, 40 * size, 130 * size))
    pygame.draw.ellipse(surface1, (255, 255, 255), (x + 150 * size, y - 128 * size, 48 * size, 30 * size))
    pygame.draw.circle(surface1, (229, 128, 255), (x + 172 * size, y - 116 * size), 9 * size)
    pygame.draw.circle(surface1, (0, 0, 0), (x + 175 * size, y - 117 * size), 4 * size)
    pygame.draw.polygon(surface1, (255, 255, 255), [(x + 172 * size, y - 122 * size), (x + 168 * size, y - 123 * size),  (x + 172 * size, y - 122 * size)], 4)
    pygame.draw.polygon(surface1, (255, 255, 255), [(x + 154 * size, y - 118 * size), (x + 154 * size, y - 112 * size), (x + 142 * size, y - 133 * size)])
    pygame.draw.polygon(surface1, (255, 255, 255), [(x + 161 * size, y - 113 * size), (x + 164 * size, y - 122 * size), (x + 152 * size, y - 136 * size)])
    return surface1

def romashka(x = 25, y = 25, size = 1):
    surface = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)
    Lepest = pygame.Rect(x, y, 32 * size, 12 * size)
    pygame.draw.ellipse(surface, (255, 255, 255), Lepest.move(-15 * size, -8 * size))
    pygame.draw.ellipse(surface, (153, 162, 148), Lepest.move(-15 * size, -8 * size), 1)   
    pygame.draw.ellipse(surface, (255, 255, 255), Lepest.move(-1 * size, -10 * size))
    pygame.draw.ellipse(surface, (153, 162, 148), Lepest.move(-1 * size, -10 * size), 1) 
    pygame.draw.ellipse(surface, (255, 255, 255), Lepest.move(12 * size, -8 * size))
    pygame.draw.ellipse(surface, (153, 162, 148), Lepest.move(12 * size, -8 * size), 1)   
    pygame.draw.ellipse(surface, (255, 255, 0), Lepest) 
    pygame.draw.ellipse(surface, (255, 255, 255), Lepest.move(23 * size, 0 * size))
    pygame.draw.ellipse(surface, (153, 162, 148), Lepest.move(23 * size, 0 * size), 1)
    pygame.draw.ellipse(surface, (255, 255, 255), Lepest.move(15 * size, 8 * size))
    pygame.draw.ellipse(surface, (153, 162, 148), Lepest.move(15 * size, 8 * size), 1) 
    pygame.draw.ellipse(surface, (255, 255, 255), Lepest.move(-7 * size, 7 * size))
    pygame.draw.ellipse(surface, (153, 162, 148), Lepest.move(-7 * size, 7 * size), 1)   
    pygame.draw.ellipse(surface, (255, 255, 255), Lepest.move(-23 * size, 1 * size))
    pygame.draw.ellipse(surface, (153, 162, 148), Lepest.move(-23 * size, 1 * size), 1) 
    return surface

def polyana(x = 25, y = 25, size = 1):
    surfaces = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)
    pygame.draw.circle(surfaces, (113, 200, 55), (150, 150), 150)
    surfaces.blit(romashka(x, y, size), (150, 20))
    surfacewrong = pygame.transform.rotate(romashka(x, y, size), 30)
    surfaces.blit(surfacewrong, (30, -350))  
    surfacewrong = pygame.transform.rotozoom(romashka(x, y, size), -20, 1.2)
    surfaces.blit(surfacewrong, (-240, 60))   
    surfacewrong = pygame.transform.rotate(romashka(x, y, size), -15)
    surfaces.blit(surfacewrong, (-250, 90))  
    surfacewrong = pygame.transform.rotate(romashka(x, y, size), -8)
    surfaces.blit(surfacewrong, (60, 150))  
    surfacewrong = pygame.transform.rotozoom(romashka(x, y, size), 8, 0.8)
    surfaces.blit(surfacewrong, (130, 20)) 
    return surfaces
    

FPS = 30
alp = 0.5
screen = pygame.display.set_mode((int(790 * alp), int(1100 * alp)))
screen.fill ([175, 221, 233])
surface2 = pygame.Surface((800, 1100), pygame.SRCALPHA, 32)

gora =  [(0, 595), (0, 342), (95, 107), (165, 272), (271, 146), (475, 451), (617, 140), (667, 193), (792, 41), (790, 665), (469, 666), (444, 657), (446, 599), (439, 596), (440, 577), (433, 566), (414, 562), (179, 562), (97, 575), (76, 571), (41, 578)]
for i in range(len(gora)):
    gora[i] = tuple([gora[i][0] * alp, gora[i][1] * alp])
pygame.draw.polygon(surface2, (179, 179, 179), gora)
pygame.draw.polygon(surface2, (0, 0, 0), gora, 1)


trava = [(790, 665), (469, 666), (444, 657), (446, 599), (439, 596), (440, 577), (433, 566), (414, 562), (179, 562), (97, 575), (76, 571), (41, 578), (0, 592), (0, 1100), (800, 1100), (790, 665)]
for i in range(len(trava)):
    trava[i] = tuple([trava[i][0] * alp, trava[i][1] * alp])
pygame.draw.polygon(surface2, (170, 222, 135), trava)
pygame.draw.polygon(surface2, (0, 0, 0), trava, 1)



surface2.blit(pygame.transform.rotozoom(lama(), 0, 0.5), (50, 250))
surface2.blit(pygame.transform.rotozoom(polyana(), 0, 0.4), (270, 400))
screen.blit(surface2, (0, 0))



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()