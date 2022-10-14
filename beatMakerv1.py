# Building your own Beat Maker
import pygame
from pygame import mixer
pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Beat Maker")
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]


def draw_grid(clicked):
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hi_hat_text = label_font.render("Hi Hat", True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render("Snare", True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render("Bass Drum", True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render("Crash", True, white)
    screen.blit(crash_text, (30, 330))
    kick_text = label_font.render("Clap", True, white)
    screen.blit(kick_text, (30, 430))
    crash_text = label_font.render("Floor Tom", True, white)
    screen.blit(crash_text, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (200, (i * 100) + 100), 3)

    for i in range(beats):
        for j in range(instruments):
            if clicked[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen, color,
                                    [i * ((WIDTH - 200) // beats) + 205, (j * 100) + 5, ((WIDTH - 200) // beats) - 10,
                                     ((HEIGHT - 200)//instruments) - 10], 0, 3)
            pygame.draw.rect(screen, gold,
                             [i * ((WIDTH - 200) // beats) + 200, (j * 100),
                                     ((WIDTH - 200) // beats), ((HEIGHT - 200) // instruments)], 5, 5)
            pygame.draw.rect(screen, black,
                             [i * ((WIDTH - 200) // beats) + 200, (j * 100),
                                     ((WIDTH - 200) // beats), ((HEIGHT - 200) // instruments)], 2, 5)
            boxes.append((rect, (i,j)))
    return boxes

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1


    pygame.display.flip()
pygame.quit()

