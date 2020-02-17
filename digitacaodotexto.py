import pygame

pygame.init()
preto = (0, 0, 0)
roxo = (128, 0 ,128)
vermelho = (255, 0, 0)
amarelo =  (255, 255, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)
brancola = (255, 255, 254)

cinza = (128, 128, 128)
FONT = pygame.font.SysFont("Corbel", 15)
FONT2 = pygame.font.SysFont("Corbel", 15)


class TextoEntrada:

    def __init__(self, screen, x, y, largura, altura, cor, texto):
        self.screen = screen
        self.entrada_usuario = []
        self.ativo = False
        self.rect = pygame.draw.rect(screen, brancola, (x, y, largura, altura))
        self.texto = texto
        self.surface_texto = FONT.render(texto, True, (0, 0, 0))
        self.quantity_of_number = FONT2.render('0/60', True, (0, 0, 0))
        self.screen.blit(self.quantity_of_number, (850, 540))
        self.cor = cor
        pygame.display.flip()

    def get_input_text_rect(self):
        return self.rect

    # Se a pessoa clicar no quadrado pra digitar a mensagem fica azul, se apertar enter apaga o texto, etc.
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.ativo = True
            else:
                self.ativo = False
            self.cor = brancola if self.ativo else (255, 120, 155)
            self.draw(self.screen)
        if event.type == pygame.KEYDOWN:
            if self.ativo:
                # if event.key == pygame.K_RETURN:
                #     self.texto = " "
                if event.key == pygame.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                elif event.key != pygame.K_RETURN:
                    if len(self.texto) < 60:
                        self.texto += event.unicode
                self.surface_texto = FONT.render(self.texto, True, (0, 0, 0))
                self.quantity_of_number = FONT2.render(f"{len(self.texto)}/60", True, (0, 0, 0))

    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, self.rect)
        pygame.draw.rect(screen, self.cor, (500, 460, 400, 30))
        self.screen.blit(self.surface_texto, (500, 460))
        if len(self.texto) < 60:
            pygame.draw.rect(screen, self.cor, (850, 540, 50, 30))
        else:
            pygame.draw.rect(screen, vermelho, (850, 540, 50, 30))
        self.screen.blit(self.quantity_of_number, (850, 540))
        pygame.display.flip()
        return self.texto

    def clean_input(self):
        self.texto = ""
        self.surface_texto = FONT.render(self.texto, True, (0, 0, 0))
        self.quantity_of_number = FONT2.render(f"{len(self.texto)}/60", True, (0, 0, 0))
        self.cor = azul
        self.draw(self.screen)
        #print(self.texto)
        pygame.display.flip()
