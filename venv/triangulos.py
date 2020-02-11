import sys
import os
import pygame
import random
from pygame.locals import *



preto = (0, 0, 0)
roxo = (128, 0 ,128)
vermelho = (255, 0, 0)
amarelo =  (255, 255, 0)
verde = (0, 255, 0)
branco = (255, 255, 255)
cinza = (128, 128, 128)


class Triangulo():
    def __init__(self, cor, x1, y1, x2, y2, x3, y3):
        self.cor = cor
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def get_cor(self):
        return self.cor

    def get_x_y_z(self):
        return self.x1, self.y1, self.x2, self.y2, self.x3, self.y3


    def cria_triangulo(self, screen):
        return pygame.draw.polygon(screen, self.cor, [[self.x1, self.y1], [self.x2, self.y2], [self.x3, self.y3]])

