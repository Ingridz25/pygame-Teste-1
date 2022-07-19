import sys

import pygame
import random

from pygame import color

# Inicialização do pygame e mixer
pygame.init()
pygame.mixer.init()

# Variáveis para cores
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (7, 51, 31)
RED = (135, 0, 16)
WIDHT = 400
HEIGHT = 500

# Carregando as imagens do jogo
player = pygame.transform.scale(pygame.image.load("images/jump.png"), (50, 50))
background_image1 = pygame.image.load("images/bg.png")
background_image2 = pygame.image.load("images/bg2.jpg")
background_image3 = pygame.image.load("images/bg3.png")
background_image4 = pygame.image.load("images/bg4.png")
background_image5 = pygame.image.load("images/bg5.png")
background_image6 = pygame.image.load("images/bg6.jpg")
background_image7 = pygame.image.load("images/bg7.jpg")
menu_image = pygame.image.load("images/TELAMENU.png")
platform_image = pygame.transform.scale(pygame.image.load("images/wood.png"), (70, 10))
game_over_screen = pygame.image.load("images/Gameoverscreen.jpg")

# Carregando os sons do jogo
pygame.mixer.music.load("C:/Users/ingri/PycharmProjects/pygame 4/sounds/best part.wav")
pygame.mixer.music.play(-1)
'''
pygame.mixer.music.load("sounds/assets_jump (1).mp3")
gameover_sfx = pygame.mixer.load("sounds/assets_death.mp3")
'''
# Constantes de pontuação e framerate para o jogo
fps = 60
timer = pygame.time.Clock()
score = 0
high_score = 0
game_over = False
score_last = 0
jump = False

class Menutext(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("images/TELAMENU1.png"))
        self.sprites.append(pygame.image.load("images/TELAMENU2.png"))
        self.sprites.append(pygame.image.load("images/TELAMENU3.png"))
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,0

sprites_all = pygame.sprite.Group()
menutext = Menutext()
sprites_all.add(menutext)




# Variáveis de texto
font = pygame.font.Font("Mario-Kart-DS.ttf", 20)
font1 = pygame.font.Font("FreeSansBold.ttf", 20)

# Constantes do personagem
y_change = 0
x_change = 0
player_speed = 3
super_jump = 2
jump_last = 0
jump_height = 9

# Variaveis de posicionamento do jogo
player_x = 170
player_y = 400
platforms = [[160, 480], [90, 370], [270, 370], [180, 260], [90, 150],
             [270, 150], [80, 40]]  # posição x, y inicial dos blocos

# Criar a tela
screen = pygame.display.set_mode([WIDHT, HEIGHT])
pygame.display.set_caption("jump game")


# função para checar as colisões com as plataformas
def check_colisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x, player_y, 50,
                                     50]) and jump == False and y_change > 0:  # Aqui no player_y eu posso ajustar o tamano da plataforma
            j = True
    return j


# Como fazero jogo dar game over ao tocar em um retangulo?
def enemies(enemy_rect):
    global player_x
    global player_y
    global game_over
    if enemy_rect.colliderect([player_x, player_y, 50, 50]) and game_over == False:
        game_over = True


# Função para atualizar a posição relativa ao eixo y do personagem
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 9.5
    gravity = 0.4
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos


# Função para atualização das plataformas e gerar novas
def update_platforms(my_list, y_pos, change):
    global score

    if y_pos < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            new_x = random.randint(0, 330)
            new_y = random.randint(-50, -10)
            my_list[item] = [new_x, new_y, 70, 10]

            score += 1
    return my_list


'''
    def change_background():
        global score
        global score_last
        while score - score_last == score - score_last + 10:
            screen.blit(background_image2, (0, 0))
            screen.blit(player, (player_x, player_y))
    return change_background()
'''

'''
menu = "run"
while menu == "run":
screen.blit(background_image2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    menu = "false"
'''
# Loop principal do jogo
running = True
state = 'run'
while running == True:
    timer.tick(fps)
    if state == 'run':
        #background = screen.blit(background_image1, (0,0)) #Desenha o plano de fundo inicial

        screen.blit(player, (player_x, player_y)) #Desenha o player
        blocks = [] #Lista onde é adicionada as plataformas geradas pelo radint
        score_last



        # Aqui o plano de fundo muda de acordo com a pontuação que o jogador faz
        if score - score_last > 15 and not game_over and not jump:
            screen.blit(background_image2, (0, 0))
            screen.blit(player, (player_x, player_y))

        if score - score_last > 30 and not game_over and not jump:
            screen.blit(background_image3, (0, 0))
            screen.blit(player, (player_x, player_y))

        if score - score_last > 40 and not game_over and not jump:
            screen.blit(background_image4, (0, 0))
            screen.blit(player, (player_x, player_y))

        if score - score_last > 50 and not game_over and not jump:
            screen.blit(background_image5, (0, 0))
            screen.blit(player, (player_x, player_y))

        if score - score_last > 60 and not game_over and not jump:
            screen.blit(background_image6, (0, 0))
            screen.blit(player, (player_x, player_y))

        if score - score_last > 70 and not game_over and not jump:
            screen.blit(background_image7, (0, 0))
            screen.blit(player, (player_x, player_y))

        # Escrevendo Highscore e Score na tela
        score_text = font.render("SCORE ", True, RED)
        score_text1 = font1.render(": " + str(score), True, RED)
        high_score_text = font.render("HIGH SCORE ", True, RED)
        high_score_text1 = font1.render(": " + str(score), True, RED)

        # Posicionando corretamente as strings de pontuação na tela
        screen.blit(high_score_text, (9, 9))
        screen.blit(high_score_text1, (133, 4))
        screen.blit(score_text, (9, 30))
        screen.blit(score_text1, (80, 24))

        # Escrevendo o Super_jump na tela:
        superjump_text = font.render("SUPER JUMPS ", True, RED)
        superjump_text1 = font1.render(": " + str(super_jump), True, RED)
        screen.blit(superjump_text, (220, 9))
        screen.blit(superjump_text1, (365, 4))

        # Para adicionar as plataformas no vetor
        for i in range(len(platforms)):
            screen.blit(platform_image, platforms[i])  # desenha imagem(bloco) na posição do retangulo
            block = platform_image.get_rect(x=platforms[i][0], y=platforms[i][1])  # cria novo retangulo block com a dimensão da imagem e na posição do retangulo
            blocks.append(block)  # adiciona esse novo retangulo com a dimimensão da imagem a uma lista

        # Mapeando as teclas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Definindo condição para o game over
                if event.key == pygame.K_SPACE and game_over:
                    game_over = False
                    score = 0
                    player_x = 170
                    player_y = 400
                    background = screen.blit(background_image1, (0, 0))
                    score_last = 0
                    super_jump = 2
                    jump_last = 0
                    platforms = [[170, 480], [85, 370], [265, 370], [175, 260], [85, 150],
                                 [265, 150], [175, 40]]

                if event.key == pygame.K_a:
                    x_change = -player_speed
                if event.key == pygame.K_d:
                    x_change = player_speed
                if event.key == pygame.K_w and super_jump > 0:
                    super_jump -= 1
                    y_change = -15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    x_change = 0
                if event.key == pygame.K_d:
                    x_change = 0

        jump = check_colisions(blocks, jump)
        player_x += x_change

        # Deixa o personagem parado no game over
        if player_y < 440:
            player_y = update_player(player_y)
        else:
            game_over = True
            y_change = 0
            x_change = 0

        platforms = update_platforms(platforms, player_y, y_change)

        # Estabelecendo limites para o personagem na tela
        if player_x < -20:
            player_x = -20
        elif player_x > 350:
            player_x = 350
        # Fazendo a sprite do personagem olhar para direita ou esquerda de acordo com o comando do jogador
        if x_change > 0:
            player = pygame.transform.scale(pygame.image.load("images/jump.png"), (50, 50))
        elif x_change < 0:
            player = (
                pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/jump.png"), (50, 50)), 1, 0))

        # Não deixa o personagem subir para longe na vertical
        if player_y < 0:
            player_y = 0
        # Definindo o Highscore
        if score > high_score:
            high_score = score

        # Adicionando um superpulo ao personagem quando ele faz 50 pontos
        if score - jump_last > 50:
            jump_last = score
            super_jump += 1

        # Escrevendo o game over na tela
        if game_over:
            screen.blit(game_over_screen, (0, 0))

        pygame.display.flip()
    else:
        screen.blit(menu_image, (0,0))
        screen.blit(player, (player_x, player_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
pygame.quit()
