from character import Character
import random

class ScenarioManager:
    def __init__(self):
        self.scenarios = []
        self.current_scenario_index = 0
        self.create_scenarios()
        random.shuffle(self.scenarios)
    
    def create_scenarios(self):
        """Cria todos os cenários do jogo"""
        
        # Cenário 1: Médico vs Criminoso
        doctor = Character(
            "Dr. Maria Silva", 45, "Médica", "healthy",
            "Especialista em doenças infecciosas. Trabalhou no CDC antes do apocalipse.",
            2, ["Medicina", "Primeiros Socorros", "Pesquisa Médica"], ["Equipamentos médicos"]
        )
        
        criminal = Character(
            "João 'Faca' Santos", 32, "Ex-presidiário", "injured",
            "Condenado por roubo a mão armada. Diz que mudou, mas tem tatuagens de gangue.",
            8, ["Combate", "Construção", "Mecânica"], ["Remédios", "Comida"]
        )
        
        self.scenarios.append({
            'id': 1,
            'title': "O Dilema do Médico",
            'description': "Um médico especialista em doenças infecciosas chega à base. Ele pode salvar vidas, mas também pode ser um risco se estiver infectado.",
            'character': doctor,
            'dilemma': "Deixar entrar um médico que pode salvar muitos, mas que pode estar infectado?",
            'consequences': {
                True: "O médico salvou 5 pessoas com seu conhecimento. A base agora tem um especialista médico.",
                False: "O médico morreu do lado de fora. 3 pessoas morreram por falta de cuidados médicos."
            }
        })
        
        # Cenário 2: Família vs Estrangeiro
        family_member = Character(
            "Ana Costa", 28, "Mãe", "sick",
            "Mãe de duas crianças pequenas. Está doente mas diz que é apenas gripe.",
            6, ["Culinária", "Costura", "Cuidados infantis"], ["Remédios", "Comida para crianças"]
        )
        
        engineer = Character(
            "Carlos Kim", 35, "Engenheiro", "healthy",
            "Engenheiro nuclear. Pode ajudar a manter os geradores funcionando.",
            3, ["Engenharia", "Eletrônica", "Manutenção"], ["Ferramentas"]
        )
        
        self.scenarios.append({
            'id': 2,
            'title': "Família vs Necessidade",
            'description': "Uma mãe doente com crianças pequenas vs um engenheiro que pode manter a base funcionando.",
            'character': family_member,
            'dilemma': "Priorizar uma família em necessidade ou alguém essencial para a sobrevivência da base?",
            'consequences': {
                True: "A família foi aceita. As crianças trouxeram alegria à base, mas a mãe espalhou uma doença leve.",
                False: "A família foi rejeitada. As crianças morreram de fome. A base perdeu humanidade."
            }
        })
        
        # Cenário 3: Soldado vs Civil
        soldier = Character(
            "Sgt. Roberto Alves", 38, "Soldado", "injured",
            "Sargento do exército. Ferido em combate contra zumbis. Tem experiência militar.",
            7, ["Combate", "Estratégia", "Treinamento"], ["Remédios", "Armas"]
        )
        
        teacher = Character(
            "Prof. Lúcia Mendes", 42, "Professora", "healthy",
            "Professora de história. Pode educar as crianças e manter a cultura viva.",
            2, ["Educação", "Psicologia", "Organização"], ["Livros", "Material escolar"]
        )
        
        self.scenarios.append({
            'id': 3,
            'title': "Força vs Sabedoria",
            'description': "Um soldado ferido que pode proteger a base vs uma professora que pode educar as crianças.",
            'character': soldier,
            'dilemma': "Escolher proteção militar ou educação para o futuro?",
            'consequences': {
                True: "O soldado protegeu a base de um ataque zumbi. Mas seu ferimento piorou.",
                False: "A base ficou mais vulnerável. Uma criança foi mordida por um zumbi."
            }
        })
        
        # Cenário 4: Criança vs Adulto
        child = Character(
            "Pedro Santos", 12, "Estudante", "healthy",
            "Criança órfã. Perdeu os pais para zumbis. Muito inteligente para a idade.",
            4, ["Matemática", "Observação", "Agilidade"], ["Comida", "Atenção"]
        )
        
        farmer = Character(
            "Seu José", 65, "Fazendeiro", "healthy",
            "Fazendeiro experiente. Pode ensinar agricultura e garantir comida para todos.",
            2, ["Agricultura", "Criação de animais", "Conservação"], ["Sementes", "Ferramentas"]
        )
        
        self.scenarios.append({
            'id': 4,
            'title': "Presente vs Futuro",
            'description': "Uma criança órfã vs um fazendeiro que pode garantir comida para todos.",
            'character': child,
            'dilemma': "Investir no futuro (criança) ou no presente (comida)?",
            'consequences': {
                True: "A criança cresceu e se tornou um líder importante. Mas consumiu recursos preciosos.",
                False: "A criança morreu. A base perdeu um potencial líder futuro."
            }
        })
        
        # Cenário 5: Infectado vs Saudável
        infected = Character(
            "Marina Costa", 25, "Enfermeira", "sick",
            "Enfermeira que foi mordida por um zumbi. Diz que a mordida foi superficial.",
            9, ["Enfermagem", "Primeiros Socorros", "Cuidados"], ["Remédios", "Observação médica"]
        )
        
        scientist = Character(
            "Dr. Paulo Santos", 50, "Cientista", "healthy",
            "Pesquisador que pode desenvolver uma cura para o vírus zumbi.",
            1, ["Pesquisa", "Química", "Biologia"], ["Laboratório", "Equipamentos"]
        )
        
        self.scenarios.append({
            'id': 5,
            'title': "A Última Esperança",
            'description': "Uma enfermeira possivelmente infectada vs um cientista que pode salvar a humanidade.",
            'character': infected,
            'dilemma': "Arriscar a base por uma possível cura ou manter a segurança?",
            'consequences': {
                True: "A enfermeira se transformou em zumbi. Matou 2 pessoas antes de ser contida.",
                False: "A enfermeira morreu. Perdeu-se uma chance de estudar o vírus."
            }
        })
        
        # Cenário 6: Líder vs Seguidor
        leader = Character(
            "Capitão Silva", 45, "Líder Militar", "healthy",
            "Ex-capitão do exército. Quer assumir o comando da base.",
            6, ["Liderança", "Estratégia", "Combate"], ["Autoridade", "Respeito"]
        )
        
        worker = Character(
            "Maria das Dores", 35, "Trabalhadora", "healthy",
            "Trabalhadora braçal. Pode ajudar na construção e manutenção.",
            2, ["Construção", "Limpeza", "Cozinha"], ["Ferramentas", "Comida"]
        )
        
        self.scenarios.append({
            'id': 6,
            'title': "Poder vs Trabalho",
            'description': "Um líder militar que quer assumir o comando vs uma trabalhadora que pode ajudar na base.",
            'character': leader,
            'dilemma': "Aceitar um novo líder ou manter a ordem atual?",
            'consequences': {
                True: "O capitão assumiu o comando. A base ficou mais organizada, mas menos democrática.",
                False: "O capitão foi rejeitado. A base manteve sua autonomia, mas ficou menos eficiente."
            }
        })
        
        # Cenário 7: Idoso vs Jovem
        elderly = Character(
            "Dona Rosa", 78, "Aposentada", "sick",
            "Idosa com problemas cardíacos. Precisa de cuidados especiais.",
            5, ["História", "Sabedoria", "Costura"], ["Remédios", "Cuidados especiais"]
        )
        
        young_worker = Character(
            "Lucas Silva", 22, "Técnico", "healthy",
            "Jovem técnico em informática. Pode consertar equipamentos eletrônicos.",
            3, ["Informática", "Eletrônica", "Manutenção"], ["Ferramentas", "Peças"]
        )
        
        self.scenarios.append({
            'id': 7,
            'title': "Sabedoria vs Juventude",
            'description': "Uma idosa com sabedoria vs um jovem com habilidades técnicas.",
            'character': elderly,
            'dilemma': "Valorizar experiência ou habilidades práticas?",
            'consequences': {
                True: "A idosa compartilhou sua sabedoria. Mas consumiu recursos médicos preciosos.",
                False: "A idosa morreu. A base perdeu uma fonte de sabedoria e experiência."
            }
        })
        
        # Cenário 8: Final - O Sacrifício
        final_character = Character(
            "Você Mesmo", 30, "Segurança", "healthy",
            "Você é o segurança da base. Sua decisão final determinará o futuro.",
            5, ["Segurança", "Decisões", "Responsabilidade"], ["Coragem", "Sabedoria"]
        )
        
        self.scenarios.append({
            'id': 8,
            'title': "O Último Dilema",
            'description': "Você deve decidir se sacrifica sua própria vida para salvar a base de um ataque zumbi em massa.",
            'character': final_character,
            'dilemma': "Sacrificar-se para salvar outros ou sobreviver para continuar protegendo?",
            'consequences': {
                True: "Você se sacrificou. A base foi salva, mas você morreu. Seu legado vive.",
                False: "Você sobreviveu. A base foi atacada, mas você pode reconstruí-la."
            }
        })
    
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
        random.shuffle(self.scenarios) 