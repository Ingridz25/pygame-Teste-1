import pygame
import random

from pygame import color

# Inicialização do pygame
pygame.init()

# Variáveis para cores
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
BLUE = (0, 0, 255)
WIDHT = 400
HEIGHT = 500
background = white

# Carregando as imagens do personagem,fundo e plataformas
player = pygame.transform.scale(pygame.image.load("images/jump.png"), (50, 50))
player_mask = pygame.mask.from_surface(player)
background_image = pygame.image.load("images/bg.png")
platform_image = pygame.transform.scale(pygame.image.load("images/wood.png"), (100, 20))
platform_image_mask = pygame.mask.from_surface(platform_image)

# Constantes de pontuação e framerate para o jogo
fps = 60
timer = pygame.time.Clock()
score = 0
high_score = 0
game_over = False
score_last = 0
jump = False

# Variáveis de texto
font = pygame.font.Font("Mario-Kart-DS.ttf", 16)
font1 = pygame.font.Font("FreeSansBold.ttf", 16)

# Constantes do personagem
y_change = 0
x_change = 0
player_speed = 3

# Variaveis de posicionamento do jogo
player_x = 170
player_y = 400
platforms = [[170, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10], [85, 150, 70, 10],
             [265, 150, 70, 10], [175, 40, 70, 10]]

# Criar a tela
screen = pygame.display.set_mode([WIDHT, HEIGHT])
pygame.display.set_caption("jump game")


# função para checar as colisões com as plataformas
def check_colisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x + 20, player_y + 60, 30, 5]) and jump == False and y_change > 0: #Aqui no player_y eu posso ajustar o tamano da plataforma
            j = True
    return j


# Função para atualizar a posição relativa ao eixo y do personagem
def update_player(y_pos):
    global jump
    global y_change
    jump_height = 10
    gravity = 0.4
    if jump:
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity
    return y_pos


# Função para atualização das plataformas e gerar novas
def update_platforms(my_list, y_pos, change,):
    global score

    if y_pos < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(0, 320), random.randint(-40, -10), 70, 10]
            score += 1
    return my_list


# Loop principal do jogo
running = True
while running == True:
    timer.tick(fps)
    screen.fill(background)  # Aq ao invés de white eel colocou background
    screen.blit(player, (player_x, player_y))
    blocks = []
    score_last
    player_mask.overlap(platform_image_mask,(0,0))
    print(player_mask.overlap(platform_image_mask,(0,0)))
    # Escrevendo Highscore e Score na tela
    score_text = font.render("SCORE ", True, BLUE)
    score_text1 = font1.render(": " + str(score), True, BLUE)
    high_score_text = font.render("HIGH SCORE ", True, BLUE)
    high_score_text1 = font1.render(": " + str(score), True, BLUE)
    # Posicionando corretamente as strings de pontuação na tela
    screen.blit(high_score_text, (9, 9))
    screen.blit(high_score_text1, (105, 5))
    screen.blit(score_text, (9, 25))
    screen.blit(score_text1, (63, 22))

    # Definindo o Highscore
    if score > high_score:
        high_score = score

    if score - score_last > 15:
        score_last = score
        background = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    # Para adicionar as plataformas no vetor
    for i in range(len(platforms)):
        screen.blit(platform_image,platforms[i])
        #print(platforms[i])
       # block = platform_image.get_rect(x=platforms[i].x, y = platforms[i].y)
        block = pygame.draw.rect(screen, black, platforms[i], 0, 1) #
       # blocks.append(block)

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
                background = white
                score_last = 0
                platforms = [[170, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [175, 260, 70, 10],
                             [85, 150, 70, 10],
                             [265, 150, 70, 10], [175, 40, 70, 10]]

            if event.key == pygame.K_a:
                x_change = -player_speed
            if event.key == pygame.K_d:
                x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0

    jump = check_colisions(blocks, jump)
    player_x += x_change
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
    elif player_x > 330:
        player_x = 330
    # Fazendo a sprite do personagem olhar para direita ou esquerda de acordo com o comando do jogador
    if x_change > 0:
        player = pygame.transform.scale(pygame.image.load("images/jump.png"), (50, 50))
    elif x_change < 0:
        player = (pygame.transform.flip(pygame.transform.scale(pygame.image.load("images/jump.png"), (50, 50)), 1, 0))

    pygame.display.flip()
pygame.quit()
