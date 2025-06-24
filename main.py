import pygame
import sys
import random
from game_state import GameState
from character import Character
from ui_manager import UIManager
from scenario_manager import ScenarioManager

class ZombieApocalypseGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Alpaca Lips - Base Security")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Inicializar componentes do jogo
        self.game_state = GameState()
        self.ui_manager = UIManager(self.screen_width, self.screen_height)
        self.scenario_manager = ScenarioManager()
        
        # Estado atual
        self.current_character = None
        self.current_scenario = None
        self.game_finished = False
        
    def run(self):
        """Loop principal do jogo"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
    
    def handle_events(self):
        """Processa eventos do pygame"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos)
            
            if event.type == pygame.KEYDOWN:
                self.handle_key_press(event.key)
    
    def handle_mouse_click(self, pos):
        """Processa cliques do mouse"""
        if self.game_finished:
            # Se o jogo terminou, qualquer clique reinicia
            self.restart_game()
            return
            
        if self.current_character:
            # Verificar se clicou no botão "Deixar Entrar"
            if self.ui_manager.let_in_button.collidepoint(pos):
                self.make_decision(True)
            
            # Verificar se clicou no botão "Deixar Fora"
            elif self.ui_manager.keep_out_button.collidepoint(pos):
                self.make_decision(False)
    
    def handle_key_press(self, key):
        """Processa teclas pressionadas"""
        if self.game_finished:
            if key == pygame.K_SPACE or key == pygame.K_RETURN:
                self.restart_game()
            elif key == pygame.K_ESCAPE:
                self.running = False
            return
            
        if key == pygame.K_SPACE and not self.current_character:
            self.next_character()
        elif key == pygame.K_ESCAPE:
            self.running = False
    
    def next_character(self):
        """Carrega o próximo personagem"""
        if self.scenario_manager.has_more_scenarios():
            self.current_scenario = self.scenario_manager.get_next_scenario()
            self.current_character = self.current_scenario['character']
        else:
            self.end_game()
    
    def make_decision(self, let_in):
        """Processa a decisão do jogador"""
        if self.current_character:
            # Registrar a decisão
            self.game_state.add_decision(self.current_character, let_in, self.current_scenario)
            
            # Mostrar consequência
            consequence = self.current_scenario['consequences'][let_in]
            self.game_state.add_consequence(consequence)
            
            # Próximo personagem
            self.current_character = None
            self.current_scenario = None
    
    def end_game(self):
        """Finaliza o jogo e mostra o resultado"""
        self.game_state.calculate_final_score()
        self.game_finished = True
    
    def restart_game(self):
        """Reinicia o jogo"""
        self.game_state = GameState()
        self.scenario_manager.reset_scenarios()
        self.current_character = None
        self.current_scenario = None
        self.game_finished = False
    
    def update(self):
        """Atualiza a lógica do jogo"""
        pass
    
    def render(self):
        """Renderiza o jogo"""
        # Limpar tela
        self.screen.fill((20, 20, 30))
        
        if self.game_finished:
            # Renderizar tela final
            self.ui_manager.render_final_screen(self.screen, self.game_state)
        elif self.current_character:
            # Renderizar personagem atual
            self.ui_manager.render_character(self.screen, self.current_character, self.current_scenario)
        else:
            # Renderizar tela de transição
            self.ui_manager.render_transition_screen(self.screen, self.game_state)
        
        pygame.display.flip()

if __name__ == "__main__":
    game = ZombieApocalypseGame()
    game.run() 