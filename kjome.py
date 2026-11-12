import pygame
import random
pygame.init()

clock = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

color = pygame.Color(0)
darkerColor = pygame.Color(0)
evenDarkerColor = pygame.Color(0)


font = pygame.font.SysFont("Arial", 50)
shadow = pygame.font.SysFont("Arial", 54)
small = pygame.font.SysFont("Arial", 20)
running = True
    
while running:
    targetPos = (WIDTH / 2, HEIGHT / 2.5)
    tTargetPos = (WIDTH / 2, HEIGHT / 1.6)
    ttTargetPos = (WIDTH / 2, (HEIGHT / 1.6) + 25)
    tttTargetPos = (WIDTH / 2, (HEIGHT / 1.6) + 50)
    t4TargetPos = (WIDTH / 2, (HEIGHT / 1.6) + 75)
    evenDarkerColor.hsva = ((pygame.time.get_ticks() // 10) % 360, 100, 100 - 90, 100)
    screen.fill(evenDarkerColor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Thank you for trying the thing out!")
            running = False
    darkerColor.hsva = ((pygame.time.get_ticks() // 10) % 360, 100, 100 - 70, 100)
    textShadow = shadow.render("Thank you, Ms. Kjome!", True, darkerColor)

    color.hsva = ((pygame.time.get_ticks() // 10) % 360, 100, 100, 100)
    text = font.render("Thank you, Ms. Kjome!", True, color)

    textBelow = small.render("Your hard work and kindness will never be forgotten.", True, color)
    otherTextBelow = small.render("You have brought happiness and peace to us all over the years.", True, color)
    otherOtherTextBelow = small.render("The things you have brought us will never be ignored.", True, color)
    oooTextBelow = small.render("Thank you.", True, color)
    backText = textShadow.get_rect(center=targetPos)
    frontText = text.get_rect(center=targetPos)
    tText = textBelow.get_rect(center=tTargetPos)
    ttText = otherTextBelow.get_rect(center=ttTargetPos)
    tttText = otherOtherTextBelow.get_rect(center=tttTargetPos)
    t4text = oooTextBelow.get_rect(center=t4TargetPos)
    screen.blit(textShadow, backText)
    screen.blit(text, frontText)
    screen.blit(textBelow, tText)
    screen.blit(otherTextBelow, ttText)
    screen.blit(otherOtherTextBelow, tttText)
    screen.blit(oooTextBelow, t4text)
    pygame.display.flip()
    clock.tick(120)