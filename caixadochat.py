import pygame


preto = (0, 0, 0)
roxo = (128, 0 ,128)
vermelho = (255, 0, 0)
amarelo =  (255, 255, 0)
verde = (0, 255, 0)
branco = (255, 255, 255)
brancola = (255, 255, 254)

cinza = (128, 128, 128)


# Inicializa a caixa do chat
class CaixaChat:
    def __init__(self, screen, x, y, largura, altura, cor):
        self.screen = screen
        self.largura = largura
        self.rect = pygame.draw.rect(screen, cor, (x, y, largura, altura))
        pygame.display.flip()
        self.font = pygame.font.SysFont("Corbel", 20)
        self.chatarray = []
        self.texts = []

    # adiciona o texto para a janela de chat e verifica se tem 11, q e o tanto de mensagem q cabe na janela se tiver, deleta a primeira enviada
    def adiciona_texto(self, jogador_atual, texto):
        if len(self.chatarray) == 11:
            self.chatarray.pop(0)

        self.chatarray.append((jogador_atual, texto))

    def pega_todos_textos(self):
        return self.chatarray

    def reseta_interface(self):
        self.screen.fill(branco)

    # manda as mensagems pra tela do chat nao to entendendo pq ta mudando a cor de todas as mensagems pra cor do ultimo que enviou a mensagem
    def atualiza_tela_chatarray(self, jogador_atual):
        for index, value in enumerate(self.chatarray):
            (jogador_atual_da_mensagem, texto) = value
            font = pygame.font.SysFont("Corbel", 20).render(texto, True, (0, 0, 0))
            render_font = font
            pygame.draw.rect(self.screen, brancola, (500, 90 + (30 * index), self.largura, 30))
            self.screen.blit(render_font, (510, 90 + (30 * index)))
            pygame.display.flip()
            # if jogador_atual_da_mensagem == "verde":
            #     #texto = (f"Jogador verde: {texto}")
            #     font = pygame.font.SysFont("Corbel", 20).render(texto,True, green)
            #     render_font = font
            #     pygame.draw.rect(self.screen, branco, (500, 90 + (30 * index), self.largura, 30))
            #     self.screen.blit(render_font, (510, 90 + (30 * index)))
            #     pygame.display.flip()
            # else:
            #     #texto = (f"Jogador vermelho: {texto}")
            #     font = pygame.font.SysFont("Corbel", 20).render(texto,True, red)
            #     render_font = font
            #     pygame.draw.rect(self.screen, branco, (500, 90 + (30 * index), self.largura, 30))
            #     self.screen.blit(render_font, (510, 90 + (30 * index)))
            #     pygame.display.flip()
