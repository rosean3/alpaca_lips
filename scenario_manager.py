from character import Character
import random

class ScenarioManager:
    def __init__(self):
        self.scenarios = []
        self.current_scenario_index = 0
        self.create_scenarios()
        # Manter o primeiro e o último fixos, embaralhar o meio
        first = self.scenarios[0:1]  # A Médica Especialista
        middle = self.scenarios[1:-1]  # Demais
        last = self.scenarios[-1:]  # O Último Dilema
        random.shuffle(middle)
        self.scenarios = first + middle + last
    
    def create_scenarios(self):
        """Cria todos os cenários do jogo"""
        
        # Cenário 1: Médico especialista
        doctor = Character(
            "Dra. Maria Silva", 45, "Médica", "Saudável",
            "Especialista em doenças infecciosas. Trabalhou no CDC antes do apocalipse.",
            2, ["Medicina", "Primeiros Socorros", "Pesquisa Médica"], ["Equipamentos médicos"],
            image_path="assets/characters/dr_maria_silva.png"
        )
        
        self.scenarios.append({
            'id': 1,
            'title': "A Médica Especialista",
            'description': "Uma médica especialista em doenças infecciosas chega à base. Ela pode salvar muitas vidas com seu conhecimento médico.",
            'character': doctor,
            'dilemma': "Deixar entrar uma médica que pode salvar muitos, mas que pode estar infectada?",
            'consequences': {
                True: "A médica salvou 5 pessoas com seu conhecimento. A base agora tem um especialista médico.",
                False: "A médica morreu do lado de fora. 3 pessoas morreram por falta de cuidados médicos."
            }
        })
        
        # Cenário 2: Família com crianças
        family_member = Character(
            "Ana Costa", 28, "Mãe", "Doente",
            "Mãe de duas crianças pequenas. Está doente mas diz que é apenas gripe.",
            6, ["Culinária", "Costura", "Cuidados infantis"], ["Remédios", "Comida para crianças"],
            image_path="assets/characters/ana_costa.png"
        )
        
        self.scenarios.append({
            'id': 2,
            'title': "A Família em Necessidade",
            'description': "Uma mãe doente com duas crianças pequenas chega à base. Elas precisam de abrigo e cuidados.",
            'character': family_member,
            'dilemma': "Aceitar uma família em necessidade ou manter a segurança da base?",
            'consequences': {
                True: "A família foi aceita. As crianças trouxeram alegria à base, mas a mãe espalhou uma doença leve.",
                False: "A família foi rejeitada. As crianças morreram de fome. A base perdeu humanidade."
            }
        })
        
        # Cenário 3: Soldado ferido
        soldier = Character(
            "Sgt. Roberto Alves", 38, "Soldado", "Ferido",
            "Sargento do exército. Ferido em combate contra zumbis. Tem experiência militar.",
            7, ["Combate", "Estratégia", "Treinamento"], ["Remédios", "Armas"],
            image_path="assets/characters/roberto_alves.png"
        )
        
        self.scenarios.append({
            'id': 3,
            'title': "O Soldado Ferido",
            'description': "Um soldado ferido chega à base. Ele pode proteger a base, mas seu ferimento pode piorar.",
            'character': soldier,
            'dilemma': "Aceitar um soldado ferido que pode proteger a base?",
            'consequences': {
                True: "O soldado protegeu a base de um ataque zumbi. Mas seu ferimento piorou.",
                False: "A base ficou mais vulnerável. Uma criança foi mordida por um zumbi."
            }
        })
        
        # Cenário 4: Criança órfã
        child = Character(
            "Pedro Santos", 12, "Estudante", "Saudável",
            "Criança órfã. Perdeu os pais para zumbis. Muito inteligente para a idade.",
            4, ["Matemática", "Observação", "Agilidade"], ["Comida", "Atenção"],
            image_path="assets/characters/pedro_santos.png"
        )
        
        self.scenarios.append({
            'id': 4,
            'title': "A Criança Órfã",
            'description': "Uma criança órfã de 12 anos chega à base sozinha. Ela é muito inteligente mas precisa de cuidados.",
            'character': child,
            'dilemma': "Aceitar uma criança órfã que pode ser o futuro da base?",
            'consequences': {
                True: "A criança cresceu e se tornou um líder importante. Mas consumiu recursos preciosos.",
                False: "A criança morreu. A base perdeu um potencial líder futuro."
            }
        })
        
        # Cenário 5: Enfermeira possivelmente infectada
        infected = Character(
            "Marina Costa", 25, "Enfermeira", "Doente",
            "Enfermeira que foi mordida por um zumbi. Diz que a mordida foi superficial.",
            9, ["Enfermagem", "Primeiros Socorros", "Cuidados"], ["Remédios", "Observação médica"],
            image_path="assets/characters/marina_costa.png"
        )
        
        self.scenarios.append({
            'id': 5,
            'title': "A Enfermeira Suspeita",
            'description': "Uma enfermeira chega à base com uma mordida de zumbi. Ela diz que foi superficial.",
            'character': infected,
            'dilemma': "Arriscar a base por uma possível cura ou manter a segurança?",
            'consequences': {
                True: "A enfermeira se transformou em zumbi. Matou 2 pessoas antes de ser contida.",
                False: "A enfermeira morreu. Perdeu-se uma chance de estudar o vírus."
            }
        })
        
        # Cenário 6: Líder militar
        leader = Character(
            "Capitão Silva", 45, "Líder Militar", "Saudável",
            "Ex-capitão do exército. Quer assumir o comando da base.",
            6, ["Liderança", "Estratégia", "Combate"], ["Autoridade", "Respeito"],
            image_path="assets/characters/capitao_silva.png"
        )
        
        self.scenarios.append({
            'id': 6,
            'title': "O Líder Militar",
            'description': "Um capitão do exército chega à base. Ele quer assumir o comando e reorganizar tudo.",
            'character': leader,
            'dilemma': "Aceitar um novo líder que pode reorganizar a base?",
            'consequences': {
                True: "O capitão assumiu o comando. A base ficou mais organizada, mas menos democrática.",
                False: "O capitão foi rejeitado. A base manteve sua autonomia, mas ficou menos eficiente."
            }
        })
        
        # Cenário 7: Idosa com sabedoria
        elderly = Character(
            "Dona Rosa", 78, "Aposentada", "Doente",
            "Idosa com problemas cardíacos. Precisa de cuidados especiais.",
            5, ["História", "Sabedoria", "Costura"], ["Remédios", "Cuidados especiais"],
            image_path="assets/characters/dona_rosa.png"
        )
        
        self.scenarios.append({
            'id': 7,
            'title': "A Idosa Sábia",
            'description': "Uma idosa de 78 anos chega à base. Ela tem muita sabedoria mas precisa de cuidados especiais.",
            'character': elderly,
            'dilemma': "Aceitar uma idosa que pode compartilhar sua sabedoria?",
            'consequences': {
                True: "A idosa compartilhou sua sabedoria. Mas consumiu recursos médicos preciosos.",
                False: "A idosa morreu. A base perdeu uma fonte de sabedoria e experiência."
            }
        })
        
        # Cenário 8: Final - O Sacrifício
        final_character = Character(
            "Você Mesmo", 30, "Segurança", "Saudável",
            "Você é o segurança da base. Sua decisão final determinará o futuro.",
            5, ["Segurança", "Decisões", "Responsabilidade"], ["Coragem", "Sabedoria"],
            image_path="assets/characters/voce_mesmo.png"
        )
        
        self.scenarios.append({
            'id': 8,
            'title': "O Último Dilema",
            'description': "Você deve decidir se vai abandonar a base para salvá-la de um ataque zumbi em massa. Seu risco de morte é grande.",
            'character': final_character,
            'dilemma': "Sacrificar-se para salvar outros ou sobreviver para continuar protegendo?",
            'consequences': {
                True: "Você sobreviveu. A base foi atacada e todos os seus amigos morreram.",
                False: "A base está bem. Você sobreviveu, mas vai demorar 3 anos para conseguir retornar."
            }
        })
        # TODO: implementar lógica de morte de personagens
    
    def has_more_scenarios(self):
        """Verifica se ainda há cenários para processar"""
        return self.current_scenario_index < len(self.scenarios)
    
    def get_next_scenario(self):
        """Retorna o próximo cenário"""
        if self.has_more_scenarios():
            scenario = self.scenarios[self.current_scenario_index]
            self.current_scenario_index += 1
            return scenario
        return None
    
    def reset_scenarios(self):
        """Reseta os cenários para o início"""
        self.current_scenario_index = 0
        # Manter o primeiro e o último fixos, embaralhar o meio
        first = self.scenarios[0:1]  # A Médica Especialista
        middle = self.scenarios[1:-1]  # Demais
        last = self.scenarios[-1:]  # O Último Dilema
        random.shuffle(middle)
        self.scenarios = first + middle + last 