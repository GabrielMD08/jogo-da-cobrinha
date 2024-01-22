# configurar
import pygame
import random
import time

pygame.init()
pygame.display.set_caption('Snake')
largura, altura = 1000, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# cores
preto = (0, 0, 0)
branca = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# parametros cobra
tamanho_quadrado = 20
velocidade_jogo = 15

def GerarComida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def DesenharComida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def DesenharCobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def DesenhaPontuacao(pontuação):
    fonte_pontuacao = pygame.font.SysFont('Helvetica', 25)
    texto_pontuacao  = fonte_pontuacao.render(f'Pontos: {pontuação}', True, vermelho)
    tela.blit(texto_pontuacao, [1, 1])

def FinalizaJogo():
    fim_jogo = True
    fonte_fim_jogo = pygame.font.SysFont('Helvetica', 100)
    texto_fim_jogo = fonte_fim_jogo.render('GAME OVER!!', True, vermelho)
    tela.blit(texto_fim_jogo, [largura / 2 , altura / 2 -50 ])
    time.sleep(5)
    return fim_jogo   


def MoveCobra(tecla):
    match tecla:
        case pygame.K_DOWN:
            if desl_y != -tamanho_quadrado:
                desl_x = 0
                desl_y = tamanho_quadrado
        case pygame.K_UP:
            if tecla != pygame.K_DOWN:
                desl_x = 0
                desl_y = -tamanho_quadrado
        case pygame.K_RIGHT:
            if tecla != pygame.K_LEFT:
                desl_x = tamanho_quadrado
                desl_y = 0
        case pygame.K_LEFT:
            if tecla != pygame.K_RIGHT:
                desl_x = -tamanho_quadrado
                desl_y = 0

    return desl_x, desl_y

def RodarJogo():

    fim_jogo = False

    x = largura / 2
    y = altura / 2

    desl_x = 0
    desl_y = 0
    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = GerarComida()
    # loop
    while not fim_jogo:

        tela.fill(preto)

        # interação do usuario:
        for evento in pygame.event.get():
            # fechou jogo
            match evento.type:
                case pygame.QUIT:
                    fim_jogo = True
                # teclas de moovimentação
                case pygame.KEYDOWN:
                    desl_x, desl_y = MoveCobra(evento.key)

        # comida
        DesenharComida(tamanho_quadrado, comida_x, comida_y)
        
        # aumenta cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        # bateu em si mesmo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                FinalizaJogo()
        
        # atualiza posição cobra
        x += desl_x
        y += desl_y

        # desenha cobra
        DesenharCobra(tamanho_quadrado, pixels)
        
        # bateu na parede
        if x < 0 or x > largura - tamanho_quadrado or y < 0 or y > altura - tamanho_quadrado:
            FinalizaJogo()

        # pontuação
        DesenhaPontuacao(tamanho_cobra - 1)

        # criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = GerarComida()

        # atualizar tela
        pygame.display.update()

        relogio.tick(velocidade_jogo)

RodarJogo()