import pygame
import random
from sys import exit


pygame.init()
preto = (0, 0, 0)
azul = (50, 100, 213)
laranja = (205, 102, 0)
verde = (0, 255, 0)
dimensoes = (500, 600)
### VALORES INICIAIS ###
x = 300
y = 300
d = 20
lista_cobra = [[x, y]]
dx = 0
dy = 0
x_comida = round(random.randrange(0, 600 - d) / 20) * 20
y_comida = round(random.randrange(0, 600 - d) / 20) * 20
fonte = pygame.font.SysFont("Arial", 20)
tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Snake')
tela.fill(preto)
clock = pygame.time.Clock()


def desenha_cobra(lista_cobra):
    tela.fill(preto)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])


def mover_cobra(dx, dy, lista_cobra):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy
    lista_cobra.append([x_novo, y_novo])
    del lista_cobra[0]
    return dx, dy, lista_cobra


def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]
    if x not in range(0, 600) or y not in range(0, 600):
        score = fonte.render("WALL", True, verde)
        tela.blit(score, [300, 300])


def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):
    head = lista_cobra[-1]
    x_novo = head[0] + dx
    y_novo = head[1] + dy
    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
        x_comida = round(random.randrange(0, dimensoes[0] - d) / 20) * 20
        y_comida = round(random.randrange(0, dimensoes[1] - d) / 20) * 20
    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])
    return x_comida, y_comida, lista_cobra


def verifica_mordeu_cobra(listac):
    head = listac[-1]
    corp = listac.copy()
    del corp[-1]
    for x, y in corp:
        if x == head[0] and y == head[1]:
            pygame.quit()


def pontuacao(lc):
    pontos = str(len(lc) - 1)
    score = fonte.render("Pontuação: " + pontos, True, verde)
    pygame.display.set_caption("Pontuação: " + pontos)
    tela.blit(score, [0, 0])


def game(listac, dix, diy, xcomida, ycomida):
    while True:
        pygame.display.update()
        desenha_cobra(listac)
        dix, diy, listac = mover_cobra(dix, diy, listac)
        xcomida, ycomida, listac = verifica_comida(dix, diy, xcomida, ycomida, listac)
        pontuacao(listac)
        verifica_parede(listac)
        verifica_mordeu_cobra(listac)
        clock.tick(8)


game(lista_cobra, dx, dy, x_comida, y_comida)
