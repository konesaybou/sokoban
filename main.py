import pygame
from grille import *
pygame.init()
pygame.display.set_caption("Sokoban")
icon_32x32 = pygame.image.load("img/vbcv.jpg")
pygame.display.set_icon(icon_32x32)

# Generer la fenetre de notre de jeu
def play(jeu):
    size = jeu.level.shape()
    # Generer la fenetre de notre de jeu
    pygame.display.set_caption("Sokoban")
    screen = pygame.display.set_mode((size[0] * 38, size[1] * 38))
    mur = pygame.image.load("img/wall.png").convert_alpha()
    chemin = pygame.image.load("img/empty.png").convert_alpha()
    caisse = pygame.image.load("img/box.png").convert_alpha()
    cible = pygame.image.load("img/target.png").convert_alpha()
    gardien = pygame.image.load("img/sokoban.png").convert_alpha()
    rocher = pygame.image.load("img/empty_modifier.png").convert_alpha()
    clock = pygame.time.Clock()
    fps_cap = 120
    run = 1
    while run:
        clock.tick(fps_cap)

        # appliquer la  fenetre du jeu
        """ traduire  le contenu du level en image """
        for i in range(len(jeu.level.grille)):
            for j in range(len(jeu.level.grille[i])):
                chr = jeu.level.grille[i][j]
                if (chr == "#"):
                    screen.blit(mur, (i * 38, j * 38))
                elif (chr == "@"):
                    screen.blit(gardien, (i * 38, j * 38))
                elif (chr == ' '):
                    screen.blit(chemin, (i * 38, j * 38))
                elif (chr == '.'):
                    screen.blit(cible, (i * 38, j * 38))
                elif (chr == "$"):
                    screen.blit(caisse, (i * 38, j * 38))
                elif (chr == "*"):
                    screen.blit(rocher, (i * 38, j * 38))
        # mettre  à jour l'ecran
        pygame.display.flip()
        # si le joueur ferme cette fenetre
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                run = 0
                pygame.quit()
            elif event.type == pygame.KEYDOWN and keys[pygame.K_DOWN]:
                jeu.deplaceGardien(3)
            elif event.type == pygame.KEYDOWN and keys[pygame.K_UP]:
                jeu.deplaceGardien(1)
            elif event.type == pygame.KEYDOWN and keys[pygame.K_LEFT]:
                jeu.deplaceGardien(0)
            elif event.type == pygame.KEYDOWN and keys[pygame.K_RIGHT]:
                jeu.deplaceGardien(2)
            elif event.type == pygame.KEYDOWN and keys[pygame.K_SPACE]:
                jeu.play()
#nvo=int(input(" donner niveau à jouer a jouer : "))
#play(nvo)d
def aide():
    img2 = pygame.image.load("img/1.png").convert_alpha()
    img3 = pygame.image.load("img/2.png").convert_alpha()
    img4 = pygame.image.load("img/3.png").convert_alpha()
    img5 = pygame.image.load("img/4.png").convert_alpha()
    img6 = pygame.image.load("img/5.png").convert_alpha()
    img7 = pygame.image.load("img/6.png").convert_alpha()
    screen = pygame.display.set_mode((800,600))
    img = pygame.image.load("img/background-image.png").convert_alpha()
    font1 = pygame.font.SysFont('impact', 48)
    font = pygame.font.SysFont(None, 48)
    button1 = pygame.Rect(17, 535, 150, 60)
    
    while True:
        screen.blit(img,(0,0))
        screen.blit(img7,(400,170))
        screen.blit(img2,(55,210))
        screen.blit(font.render('à gauche', True, (0,0,0)), (122, 220))
        screen.blit(img3,(55,270))
        screen.blit(font.render('en haut', True, (0,0,0)), (122, 280))
        screen.blit(img4,(55,330))
        screen.blit(font.render('à droite', True, (0,0,0)), (122, 340))
        screen.blit(img5,(55,390))
        screen.blit(font.render('en bas ', True, (0,0,0)), (122, 400))
        screen.blit(img6,(55,450))
        screen.blit(font.render('recommencer', True, (0,0,0)), (122, 460))
        #pygame.draw.rect(screen, [252, 252, 111], button1,border_radius = 15)
        screen.blit(font1.render(' Retour', True, (0,0,0)), (17, 535))
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.collidepoint(event.pos): # si on click sur jouer
                        start()
        pygame.display.update()
def credit():
    screen = pygame.display.set_mode((800,600))
    img = pygame.image.load("img/background-image.png").convert_alpha()
    
    font1 = pygame.font.SysFont('impact', 48)
    font2 = pygame.font.SysFont(None, 48)
    font = pygame.font.SysFont('impact', 48)
    button1 = pygame.Rect(17, 535, 150, 60)
    while True:
        screen.blit(img,(0,0))
        
        #pygame.draw.rect(screen, [252, 252, 111], button1,border_radius = 15)
        screen.blit(font1.render(' Retour', True, (0,0,0)), (17, 535))
        screen.blit(font2.render('Jeu realisé par :  ', True, (0,0,0)), (152, 189))
        screen.blit(font.render('Abdelghafour Bakry', True, (0,0,0)), (293, 275))
        screen.blit(font.render('Saybou Kone', True, (0,0,0)), (293, 325))
        screen.blit(font.render('Robert Alphanor', True, (0,0,0)), (293, 375))
        screen.blit(font2.render('L1 Informatique 2B', True, (0,0,0)), (424, 481))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.collidepoint(event.pos): # si on click sur jouer
                        start()
        pygame.display.update()


    
def start():
    screen = pygame.display.set_mode((800,600)) #création fnêtre
    img = pygame.image.load("img/background-image.png").convert_alpha()
    font = pygame.font.SysFont('impact', 48) #définir le font
    button1 = pygame.Rect(325, 230, 150, 60) #création btn
    button2 = pygame.Rect(325, 300, 150, 60)
    button3 = pygame.Rect(325, 370, 150, 60)
    button4 = pygame.Rect(325, 440, 150, 60)
    
    while True:
        #remplissage fenêtre
        screen.blit(img,(0,0))

        
        screen.blit(font.render('Jouer', True, (0,0,0)), (346, 230))
        screen.blit(font.render(' Quitter', True, (0,0,0)), (326, 300))
        screen.blit(font.render(' Credit', True, (0,0,0)), (332, 365))
        screen.blit(font.render(' Aide', True, (0,0,0)), (348, 440))

        #changement couleur du btn
        if button1.collidepoint(pygame.mouse.get_pos()):

            screen.blit(font.render('Jouer', True, (1, 184, 29)), (346, 230))
            
        if button2.collidepoint(pygame.mouse.get_pos()):

            screen.blit(font.render(' Quitter', True, (203, 5, 23)), (326, 300))
            
        if button3.collidepoint(pygame.mouse.get_pos()):

            screen.blit(font.render(' Credit', True, (0, 230, 240)), (332, 365))

        if button4.collidepoint(pygame.mouse.get_pos()):

            screen.blit(font.render(' Aide', True, (255, 102, 0)), (348, 440))    
    
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos): # si on click sur jouer
                    jeu = Jeu(1, play)
                    jeu.play()
                if button2.collidepoint(event.pos):
                    pygame.quit()
                if button3.collidepoint(event.pos):
                    credit()
                if button4.collidepoint(event.pos):
                    aide()
                    
                    
        
        pygame.display.update()


start()

