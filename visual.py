import time
import random

import pygame

WHITE = (0xFF, 0xFF, 0xFF)
BLACK = (0, 0, 0)
RED = (0xFF, 0, 0)

class Visualizer:

    def __init__(self, automata, screen_size, delay, rule_change_interval = None):
        self.automata = automata
        self.screen_size = screen_size
        self.delay = delay
        self.rule_change_interval = rule_change_interval
        self.rule_change_counter = 0
        self.square_size = round(screen_size[0] / automata.size)

        pygame.init()

        pygame.display.set_caption("Automata")
        self.display = pygame.display.set_mode(screen_size)

        diagram = pygame.Surface(self.display.get_size())
        self.diagram = diagram.convert()
        self.diagram.fill(BLACK)

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 40)
        self.update_text()

        self.line_index = 0
        self.quit = False
    
    def loop(self):
        self.quit = False
        while not self.quit:
            self.handle_events()
            self.draw()
            self.automata.tick()
            if self.rule_change_interval:
                if self.rule_change_counter >= self.rule_change_interval:
                    self.update_rule()
                    self.rule_change_counter = 0
                else:
                    self.rule_change_counter += 1

            if self.automata.is_zero() or self.automata.is_one():
                self.automata.randomize_state()

            pygame.time.delay(self.delay)

    def update_text(self):
        self.text_surface = self.font.render("Rule{}".format(self.automata.rule_number), True, WHITE, BLACK)

    def update_rule(self):
        self.automata.randomize_rule()
        self.update_text()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.constants.QUIT:
                self.quit = True
            elif event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.K_e:
                    self.automata.randomize_state()
                elif event.key == pygame.K_r:
                    self.update_rule()

    def draw(self):
        for (index, cell) in enumerate(self.automata.cells):
            if cell:
                rect = pygame.rect.Rect(
                    index * self.square_size,
                    self.line_index * self.square_size,
                    self.square_size,
                    self.square_size
                )
                pygame.draw.rect(self.diagram, WHITE, rect)

        self.display.blit(self.diagram, (0, 0))


        self.line_index += 1
        if self.line_index * self.square_size >= self.screen_size[1]:
            self.diagram.scroll(dy = -self.square_size)
            self.line_index -= 1
            rect = pygame.rect.Rect(
                0,
                self.line_index * self.square_size,
                self.screen_size[0],
                self.square_size
            )
            pygame.draw.rect(self.diagram, BLACK, rect)
        
        self.display.blit(self.text_surface, (0, 0))
        pygame.display.flip()



