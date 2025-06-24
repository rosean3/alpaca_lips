import pygame
import random
import os

class Character:
    def __init__(self, name, age, profession, health_status, background, risk_level, skills, needs, image_path=None):
        self.name = name
        self.age = age
        self.profession = profession
        self.health_status = health_status  # "healthy", "Doente", "injured", "unknown"
        self.background = background
        self.risk_level = risk_level  # 1-10, onde 10 é muito arriscado
        self.skills = skills  # Lista de habilidades úteis
        self.needs = needs  # Lista de necessidades (comida, remédios, etc.)
        
        # Atributos visuais
        self.avatar_size = 150

        self.image_path = image_path
        self.avatar_image = None
        if image_path and os.path.exists(image_path):
            self.avatar_image = pygame.image.load(image_path)
            self.avatar_image = pygame.transform.scale(self.avatar_image, (self.avatar_size, self.avatar_size))
        else:
            self.avatar_color = self.generate_avatar_color()
        
    def generate_avatar_color(self):
        """Gera uma cor única para o avatar do personagem"""
        colors = [
            (255, 100, 100),  # Vermelho
            (100, 255, 100),  # Verde
            (100, 100, 255),  # Azul
            (255, 255, 100),  # Amarelo
            (255, 100, 255),  # Magenta
            (100, 255, 255),  # Ciano
            (255, 150, 100),  # Laranja
            (150, 100, 255),  # Roxo
        ]
        return random.choice(colors)
    
    def get_health_color(self):
        """Retorna a cor baseada no status de saúde"""
        if self.health_status == "healthy":
            return (100, 255, 100)  # Verde
        elif self.health_status == "Doente":
            return (255, 255, 100)  # Amarelo
        elif self.health_status == "injured":
            return (255, 150, 100)  # Laranja
        else:
            return (150, 150, 150)  # Cinza
    
    def get_risk_color(self):
        """Retorna a cor baseada no nível de risco"""
        if self.risk_level <= 3:
            return (100, 255, 100)  # Verde
        elif self.risk_level <= 6:
            return (255, 255, 100)  # Amarelo
        elif self.risk_level <= 8:
            return (255, 150, 100)  # Laranja
        else:
            return (255, 100, 100)  # Vermelho
    
    def get_summary(self):
        """Retorna um resumo do personagem"""
        return f"{self.name}, {self.age} anos, {self.profession}"
    
    def get_detailed_info(self):
        """Retorna informações detalhadas do personagem"""
        info = f"Nome: {self.name}\n"
        info += f"Idade: {self.age} anos\n"
        info += f"Profissão: {self.profession}\n"
        info += f"Saúde: {self.health_status}\n"
        info += f"Nível de Risco: {self.risk_level}/10\n"
        info += f"Histórico: {self.background}\n"
        info += f"Habilidades: {', '.join(self.skills)}\n"
        info += f"Necessidades: {', '.join(self.needs)}"
        return info 