import sys
import os
import pygame
import random
from pygame.locals import *

preto = (0, 0, 0)
roxo = (128, 0, 128)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
verde = (0, 255, 0)
branco = (255, 255, 255)
cinza = (128, 128, 128)


class Bola():
    def __init__(self, cor, x, y, raio=7, moveu=False, valido=True):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.moveu = moveu
        self.valido = valido

    def get_cor(self):
        return self.cor

    def set_cor(self, cor):
        self.cor = cor

    def get_x_y(self):
        return self.x, self.y

    def set_x_y(self, pos):
        self.x, self.y = pos

    def muda_estado(self):
        self.valido = True if self.valido == True else False

    def cria_bola(self, playSurface):
        return pygame.draw.circle(playSurface, self.cor, (self.x, self.y), self.raio)
