import pygame

preto = (0, 0, 0)
roxo = (128, 0, 128)
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
verde = (0, 255, 0)
branco = (255, 255, 255)
brancola = (255, 255, 254)

cinza = (128, 128, 128)


class Botao():
    def __init__(self, texto, cor, cor_do_texto):
        pygame.init()
        self.texto = texto
        self.cor = cor
        self.cor_do_texto = cor_do_texto
        self.font = pygame.font.SysFont("Arial", 20, bold=True)

    def desenha_botao(self, playSurface, x, y, largura, altura):
        rect = pygame.draw.rect(playSurface, self.cor, (x, y, largura, altura))
        render_font = self.font.render(self.texto, True, self.cor_do_texto)
        largura_do_texto, altura_do_texto = render_font.get_size()
        posicao_fonte_x = (x + largura / 2) - (largura_do_texto / 2)
        posicao_fonte_y = (y - altura / 2) - (altura_do_texto / 2)
        playSurface.blit(render_font, (posicao_fonte_x, posicao_fonte_y))
        pygame.display.flip()
        return rect
