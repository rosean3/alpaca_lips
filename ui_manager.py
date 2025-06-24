import pygame
import os

class UIManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Cores
        self.colors = {
            'background': (20, 20, 30),
            'panel': (40, 40, 50),
            'text': (255, 255, 255),
            'text_secondary': (200, 200, 200),
            'accent': (100, 150, 255),
            'success': (100, 255, 100),
            'danger': (255, 100, 100),
            'warning': (255, 255, 100),
            'border': (80, 80, 90)
        }
        
        # Fontes
        pygame.font.init()
        font_path = os.path.join("assets", "fonts", "PressStart2P-Regular.ttf")
        self.fonts = {
            'title': pygame.font.Font(font_path, 32),
            'subtitle': pygame.font.Font(font_path, 20),
            'body': pygame.font.Font(font_path, 14),
            'small': pygame.font.Font(font_path, 10),
            'button': pygame.font.Font(font_path, 16)
        }
        
        # Botões
        button_width = 230
        button_height = 60
        button_y = screen_height - 100
        
        self.let_in_button = pygame.Rect(
            screen_width // 2 - button_width - 20,
            button_y,
            button_width,
            button_height
        )
        
        self.keep_out_button = pygame.Rect(
            screen_width // 2 + 20,
            button_y,
            button_width,
            button_height
        )
        
        # Painéis
        self.character_panel = pygame.Rect(50, 50, 400, 500)
        self.info_panel = pygame.Rect(500, 50, 650, 500)
    
    def render_character(self, screen, character, scenario):
        """Renderiza a tela com o personagem atual"""
        # Limpar tela
        screen.fill(self.colors['background'])
        
        # Renderizar painel do personagem (lado esquerdo)
        self.render_character_panel(screen, character)
        
        # Renderizar painel de informações (lado direito)
        self.render_info_panel(screen, character, scenario)
        
        # Renderizar botões
        self.render_decision_buttons(screen)
        
        # Renderizar título do cenário
        self.render_scenario_title(screen, scenario)
    
    def render_character_panel(self, screen, character):
        """Renderiza o painel do personagem"""
        # Painel de fundo
        pygame.draw.rect(screen, self.colors['panel'], self.character_panel)
        pygame.draw.rect(screen, self.colors['border'], self.character_panel, 3)
        
        # Avatar do personagem
        avatar_rect = pygame.Rect(
            self.character_panel.centerx - character.avatar_size // 2,
            self.character_panel.y + 50,
            character.avatar_size,
            character.avatar_size
        )
        
        # Desenhar avatar (imagem ou cor)
        if hasattr(character, 'avatar_image') and character.avatar_image:
            screen.blit(character.avatar_image, avatar_rect)
        else:
            pygame.draw.rect(screen, character.avatar_color, avatar_rect)
        pygame.draw.rect(screen, self.colors['border'], avatar_rect, 3)
        
        # Nome do personagem
        name_text = self.fonts['subtitle'].render(character.name, True, self.colors['text'])
        name_rect = name_text.get_rect(centerx=self.character_panel.centerx, y=avatar_rect.bottom + 20)
        screen.blit(name_text, name_rect)
        
        # Informações básicas
        info_y = name_rect.bottom + 30
        info_lines = [
            f"Idade: {character.age} anos",
            f"Profissão: {character.profession}",
            f"Saúde: {character.get_health_status_translated()}",
            f"Nível de Risco: {character.risk_level}/10"
        ]
        
        for line in info_lines:
            text = self.fonts['body'].render(line, True, self.colors['text'])
            text_rect = text.get_rect(x=self.character_panel.x + 20, y=info_y)
            screen.blit(text, text_rect)
            info_y += 30
        
        # Barra de risco
        risk_bar_rect = pygame.Rect(
            self.character_panel.x + 20,
            info_y + 20,
            360,
            20
        )
        pygame.draw.rect(screen, (50, 50, 50), risk_bar_rect)
        
        risk_fill_width = (character.risk_level / 10) * 360
        risk_fill_rect = pygame.Rect(
            self.character_panel.x + 20,
            info_y + 20,
            risk_fill_width,
            20
        )
        pygame.draw.rect(screen, character.get_risk_color(), risk_fill_rect)
        
        # Texto da barra de risco
        risk_text = self.fonts['small'].render(f"Risco: {character.risk_level}/10", True, self.colors['text'])
        risk_text_rect = risk_text.get_rect(centerx=risk_bar_rect.centerx, y=risk_bar_rect.bottom + 5)
        screen.blit(risk_text, risk_text_rect)
    
    def render_info_panel(self, screen, character, scenario):
        """Renderiza o painel de informações"""
        # Painel de fundo
        pygame.draw.rect(screen, self.colors['panel'], self.info_panel)
        pygame.draw.rect(screen, self.colors['border'], self.info_panel, 3)
        
        # Título do cenário (com quebra de linha)
        title_lines = self.wrap_text(scenario['title'], self.fonts['subtitle'], self.info_panel.width - 40)
        title_y = self.info_panel.y + 20
        for line in title_lines:
            title_text = self.fonts['subtitle'].render(line, True, self.colors['accent'])
            title_rect = title_text.get_rect(x=self.info_panel.x + 20, y=title_y)
            screen.blit(title_text, title_rect)
            title_y += 36
        
        # Descrição (com quebra de linha)
        desc_lines = self.wrap_text(scenario['description'], self.fonts['body'], self.info_panel.width - 40)
        desc_y = title_y + 10
        for line in desc_lines:
            desc_text = self.fonts['body'].render(line, True, self.colors['text'])
            desc_rect = desc_text.get_rect(x=self.info_panel.x + 20, y=desc_y)
            screen.blit(desc_text, desc_rect)
            desc_y += 26
        
        # Dilema (comentado por enquanto)
        # dilemma_y = desc_y + 20
        # dilemma_text = self.fonts['subtitle'].render("O Dilema:", True, self.colors['warning'])
        # dilemma_rect = dilemma_text.get_rect(x=self.info_panel.x + 20, y=dilemma_y)
        # screen.blit(dilemma_text, dilemma_rect)
        
        # Texto do dilema (quebrado em linhas) - comentado por enquanto
        # dilemma_lines = self.wrap_text(scenario['dilemma'], self.fonts['body'], self.info_panel.width - 40)
        # dilemma_y += 36
        # for line in dilemma_lines:
        #     text = self.fonts['body'].render(line, True, self.colors['text'])
        #     text_rect = text.get_rect(x=self.info_panel.x + 20, y=dilemma_y)
        #     screen.blit(text, text_rect)
        #     dilemma_y += 26
        
        # Informações detalhadas do personagem
        details_y = desc_y + 20  # Mudou de dilemma_y para desc_y
        details_title = self.fonts['subtitle'].render("Informações Detalhadas:", True, self.colors['accent'])
        details_title_rect = details_title.get_rect(x=self.info_panel.x + 20, y=details_y)
        screen.blit(details_title, details_title_rect)
        details_y += 36
        
        # Histórico (com quebra de linha)
        history_lines = self.wrap_text(f"Histórico: {character.background}", self.fonts['body'], self.info_panel.width - 40)
        for line in history_lines:
            if line.startswith("Histórico:"):
                # Renderizar "Histórico:" em roxo
                keyword_text = self.fonts['body'].render("Histórico:", True, (150, 100, 255))
                keyword_rect = keyword_text.get_rect(x=self.info_panel.x + 20, y=details_y)
                screen.blit(keyword_text, keyword_rect)
                
                # Renderizar o resto em branco
                rest_text = self.fonts['body'].render(line[10:], True, self.colors['text'])
                rest_rect = rest_text.get_rect(x=self.info_panel.x + 20 + keyword_text.get_width(), y=details_y)
                screen.blit(rest_text, rest_rect)
            else:
                # Linhas que não começam com "Histórico:" (quebra de linha)
                history_text = self.fonts['body'].render(line, True, self.colors['text'])
                history_rect = history_text.get_rect(x=self.info_panel.x + 20, y=details_y)
                screen.blit(history_text, history_rect)
            details_y += 26
        
        # Espaçamento entre seções
        details_y += 15
        
        # Habilidades (com quebra de linha)
        skills_lines = self.wrap_text(f"Habilidades: {', '.join(character.skills)}", self.fonts['body'], self.info_panel.width - 40)
        for line in skills_lines:
            if line.startswith("Habilidades:"):
                # Renderizar "Habilidades:" em verde
                keyword_text = self.fonts['body'].render("Habilidades:", True, self.colors['success'])
                keyword_rect = keyword_text.get_rect(x=self.info_panel.x + 20, y=details_y)
                screen.blit(keyword_text, keyword_rect)
                
                # Renderizar o resto em branco
                rest_text = self.fonts['body'].render(line[12:], True, self.colors['text'])
                rest_rect = rest_text.get_rect(x=self.info_panel.x + 20 + keyword_text.get_width(), y=details_y)
                screen.blit(rest_text, rest_rect)
            else:
                # Linhas que não começam com "Habilidades:" (quebra de linha)
                skills_text = self.fonts['body'].render(line, True, self.colors['text'])
                skills_rect = skills_text.get_rect(x=self.info_panel.x + 20, y=details_y)
                screen.blit(skills_text, skills_rect)
            details_y += 26
        
        # Espaçamento entre seções
        details_y += 15
        
        # Necessidades (com quebra de linha)
        needs_lines = self.wrap_text(f"Necessidades: {', '.join(character.needs)}", self.fonts['body'], self.info_panel.width - 40)
        for line in needs_lines:
            if line.startswith("Necessidades:"):
                # Renderizar "Necessidades:" em amarelo
                keyword_text = self.fonts['body'].render("Necessidades:", True, self.colors['warning'])
                keyword_rect = keyword_text.get_rect(x=self.info_panel.x + 20, y=details_y)
                screen.blit(keyword_text, keyword_rect)
                
                # Renderizar o resto em branco
                rest_text = self.fonts['body'].render(line[13:], True, self.colors['text'])
                rest_rect = rest_text.get_rect(x=self.info_panel.x + 20 + keyword_text.get_width(), y=details_y)
                screen.blit(rest_text, rest_rect)
            else:
                # Linhas que não começam com "Necessidades:" (quebra de linha)
                needs_text = self.fonts['body'].render(line, True, self.colors['text'])
                needs_rect = needs_text.get_rect(x=self.info_panel.x + 20, y=details_y)
                screen.blit(needs_text, needs_rect)
            details_y += 26
    
    def render_decision_buttons(self, screen):
        """Renderiza os botões de decisão"""
        # Botão "Deixar Entrar"
        pygame.draw.rect(screen, self.colors['success'], self.let_in_button)
        pygame.draw.rect(screen, self.colors['border'], self.let_in_button, 3)
        
        let_in_text = self.fonts['button'].render("DEIXAR ENTRAR", True, self.colors['text'])
        let_in_text_rect = let_in_text.get_rect(center=self.let_in_button.center)
        screen.blit(let_in_text, let_in_text_rect)
        
        # Botão "Deixar Fora"
        pygame.draw.rect(screen, self.colors['danger'], self.keep_out_button)
        pygame.draw.rect(screen, self.colors['border'], self.keep_out_button, 3)
        
        keep_out_text = self.fonts['button'].render("DEIXAR FORA", True, self.colors['text'])
        keep_out_text_rect = keep_out_text.get_rect(center=self.keep_out_button.center)
        screen.blit(keep_out_text, keep_out_text_rect)
    
    def render_scenario_title(self, screen, scenario):
        """Renderiza o título do cenário no topo"""
        title_text = self.fonts['title'].render(scenario['title'], True, self.colors['accent'])
        title_rect = title_text.get_rect(centerx=self.screen_width // 2, y=10)
        screen.blit(title_text, title_rect)
    
    def render_transition_screen(self, screen, game_state):
        """Renderiza a tela de transição entre personagens"""
        # Título
        title_text = self.fonts['title'].render("Decisão Tomada", True, self.colors['accent'])
        title_rect = title_text.get_rect(centerx=self.screen_width // 2, y=100)
        screen.blit(title_text, title_rect)
        
        # Mostrar última consequência
        if game_state.consequences:
            last_consequence = game_state.consequences[-1]
            consequence_text = self.fonts['body'].render(last_consequence['text'], True, self.colors['text'])
            consequence_rect = consequence_text.get_rect(centerx=self.screen_width // 2, y=200)
            screen.blit(consequence_text, consequence_rect)
        
        # Instruções
        instruction_text = self.fonts['subtitle'].render("Pressione ESPAÇO para o próximo personagem", True, self.colors['text_secondary'])
        instruction_rect = instruction_text.get_rect(centerx=self.screen_width // 2, y=400)
        screen.blit(instruction_text, instruction_rect)
        
        # Estatísticas
        stats = game_state.get_statistics()
        stats_y = 500
        stats_lines = [
            f"Pessoas deixadas entrar: {stats['people_let_in']}",
            f"Pessoas deixadas fora: {stats['people_kept_out']}",
            f"Vidas salvas: {stats['lives_saved']}",
            f"Mortes: {stats['deaths']}",
            f"População da base: {stats['base_population']}",
            f"Moral da base: {stats['base_morale']}%"
        ]
        
        for line in stats_lines:
            text = self.fonts['small'].render(line, True, self.colors['text_secondary'])
            text_rect = text.get_rect(centerx=self.screen_width // 2, y=stats_y)
            screen.blit(text, text_rect)
            stats_y += 25
    
    def render_final_screen(self, screen, game_state):
        """Renderiza a tela final do jogo"""
        ending = game_state.get_final_ending()
        
        # Título do final
        title_text = self.fonts['title'].render(ending['title'], True, self.colors['accent'])
        title_rect = title_text.get_rect(centerx=self.screen_width // 2, y=100)
        screen.blit(title_text, title_rect)
        
        # Descrição do final
        desc_lines = self.wrap_text(ending['description'], self.fonts['body'], self.screen_width - 100)
        desc_y = 200
        for line in desc_lines:
            text = self.fonts['body'].render(line, True, self.colors['text'])
            text_rect = text.get_rect(centerx=self.screen_width // 2, y=desc_y)
            screen.blit(text, text_rect)
            desc_y += 30
        
        # Score
        score_text = self.fonts['subtitle'].render(f"Score Final: {ending['score']}", True, self.colors['warning'])
        score_rect = score_text.get_rect(centerx=self.screen_width // 2, y=desc_y + 50)
        screen.blit(score_text, score_rect)
        
        # Estatísticas finais
        stats = game_state.get_statistics()
        stats_y = score_rect.bottom + 50
        stats_lines = [
            f"Total de decisões: {stats['total_decisions']}",
            f"Taxa de aceitação: {stats['let_in_percentage']:.1f}%",
            f"Vidas salvas: {stats['lives_saved']}",
            f"Mortes causadas: {stats['deaths']}",
            f"População final: {stats['base_population']}",
            f"Moral final: {stats['base_morale']}%"
        ]
        
        for line in stats_lines:
            text = self.fonts['body'].render(line, True, self.colors['text_secondary'])
            text_rect = text.get_rect(centerx=self.screen_width // 2, y=stats_y)
            screen.blit(text, text_rect)
            stats_y += 30
        
        # Instruções para reiniciar
        restart_y = stats_y + 50
        restart_text = self.fonts['subtitle'].render("Clique ou pressione ESPAÇO para jogar novamente", True, self.colors['accent'])
        restart_rect = restart_text.get_rect(centerx=self.screen_width // 2, y=restart_y)
        screen.blit(restart_text, restart_rect)
        
        # Instrução para sair
        exit_text = self.fonts['body'].render("Pressione ESC para sair", True, self.colors['text_secondary'])
        exit_rect = exit_text.get_rect(centerx=self.screen_width // 2, y=restart_y + 40)
        screen.blit(exit_text, exit_rect)
    
    def wrap_text(self, text, font, max_width):
        """Quebra texto em linhas para caber na largura especificada"""
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + " " + word if current_line else word
            test_width = font.size(test_line)[0]
            
            if test_width <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines 