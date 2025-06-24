class GameState:
    def __init__(self):
        self.decisions = []  # Lista de decisões tomadas
        self.consequences = []  # Lista de consequências
        self.base_population = 50  # População inicial da base
        self.base_morale = 70  # Moral da base (0-100)
        self.base_security = 80  # Segurança da base (0-100)
        self.base_resources = 75  # Recursos da base (0-100)
        self.deaths = 0  # Número de mortes causadas
        self.lives_saved = 0  # Número de vidas salvas
        
        # Estatísticas
        self.people_let_in = 0
        self.people_kept_out = 0
        self.medical_decisions = 0
        self.family_decisions = 0
        self.security_decisions = 0
        
    def add_decision(self, character, let_in, scenario):
        """Adiciona uma decisão ao histórico"""
        decision = {
            'character': character,
            'let_in': let_in,
            'scenario': scenario,
            'timestamp': len(self.decisions)
        }
        self.decisions.append(decision)
        
        # Atualizar estatísticas
        if let_in:
            self.people_let_in += 1
            self.base_population += 1
        else:
            self.people_kept_out += 1
        
        # Categorizar decisão
        if 'médic' in character.profession.lower() or 'enfermeir' in character.profession.lower():
            self.medical_decisions += 1
        elif 'mãe' in character.profession.lower() or 'criança' in character.background.lower():
            self.family_decisions += 1
        elif 'soldado' in character.profession.lower() or 'militar' in character.profession.lower():
            self.security_decisions += 1
    
    def add_consequence(self, consequence_text):
        """Adiciona uma consequência ao histórico"""
        self.consequences.append({
            'text': consequence_text,
            'timestamp': len(self.consequences)
        })
        
        # Analisar consequência para atualizar estatísticas
        if 'morreu' in consequence_text.lower() or 'morte' in consequence_text.lower():
            self.deaths += 1
            self.base_morale -= 10
        elif 'salvou' in consequence_text.lower() or 'salva' in consequence_text.lower():
            self.lives_saved += 1
            self.base_morale += 5
        
        # Ajustar limites
        self.base_morale = max(0, min(100, self.base_morale))
        self.base_security = max(0, min(100, self.base_security))
        self.base_resources = max(0, min(100, self.base_resources))
    
    def calculate_final_score(self):
        """Calcula o score final baseado nas decisões"""
        score = 0
        
        # Pontos por vidas salvas
        score += self.lives_saved * 100
        
        # Pontos por manter a base segura
        if self.base_security > 70:
            score += 500
        
        # Pontos por manter moral alta
        if self.base_morale > 70:
            score += 300
        
        # Pontos por manter recursos
        if self.base_resources > 60:
            score += 200
        
        # Penalidades por mortes
        score -= self.deaths * 150
        
        # Bônus por decisões equilibradas
        if 0.3 <= (self.people_let_in / max(1, self.people_let_in + self.people_kept_out)) <= 0.7:
            score += 200
        
        return score
    
    def get_final_ending(self):
        """Determina o final baseado nas decisões"""
        score = self.calculate_final_score()
        
        if score >= 1000:
            return {
                'type': 'heroic',
                'title': 'O Herói da Base',
                'description': 'Você salvou muitas vidas e manteve a base segura. Você é lembrado como um verdadeiro herói.',
                'score': score
            }
        elif score >= 500:
            return {
                'type': 'survivor',
                'title': 'O Sobrevivente',
                'description': 'Você fez o que pôde para manter a base funcionando. Alguns sobreviveram graças a você.',
                'score': score
            }
        elif score >= 0:
            return {
                'type': 'questionable',
                'title': 'Decisões Questionáveis',
                'description': 'Suas decisões foram controversas. A base sobreviveu, mas a um alto custo.',
                'score': score
            }
        else:
            return {
                'type': 'failure',
                'title': 'O Fracasso',
                'description': 'Suas decisões levaram à morte de muitos. A base está em ruínas.',
                'score': score
            }
    
    def get_statistics(self):
        """Retorna estatísticas do jogo"""
        total_decisions = len(self.decisions)
        if total_decisions == 0:
            return {
                'total_decisions': 0,
                'people_let_in': 0,
                'people_kept_out': 0,
                'lives_saved': 0,
                'deaths': 0,
                'base_population': self.base_population,
                'base_morale': self.base_morale,
                'base_security': self.base_security,
                'base_resources': self.base_resources
            }
        
        return {
            'total_decisions': total_decisions,
            'people_let_in': self.people_let_in,
            'people_kept_out': self.people_kept_out,
            'lives_saved': self.lives_saved,
            'deaths': self.deaths,
            'base_population': self.base_population,
            'base_morale': self.base_morale,
            'base_security': self.base_security,
            'base_resources': self.base_resources,
            'let_in_percentage': (self.people_let_in / total_decisions) * 100,
            'medical_decisions': self.medical_decisions,
            'family_decisions': self.family_decisions,
            'security_decisions': self.security_decisions
        } 