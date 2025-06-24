# Alpaca Lips - Base Security

Um jogo de dilemas morais em um mundo pós-apocalíptico onde você é o segurança de uma base e deve decidir quem entra e quem fica do lado de fora.

## Sobre o Jogo

Em um mundo onde apenas 8% da população sobreviveu a um vírus zumbi mortal, você trabalha como segurança principal de uma base de sobreviventes. Sua responsabilidade é decidir quem pode entrar na base e quem deve ficar do lado de fora.

Cada decisão tem consequências que afetam a sobrevivência da base, a moral dos habitantes e o futuro da humanidade.

## Como Jogar

### Controles
- **Mouse**: Clique nos botões para tomar decisões
- **Espaço**: Avançar para o próximo personagem
- **ESC**: Sair do jogo

### Objetivo
Analise cada personagem que chega à base e decida se deve deixá-lo entrar ou não. Considere:
- O nível de risco que a pessoa representa
- As habilidades que podem beneficiar a base
- As necessidades que podem consumir recursos
- O impacto na moral e segurança da base

### Elementos do Jogo

#### Personagens
Cada personagem tem:
- **Nome e idade**
- **Profissão e habilidades**
- **Status de saúde**
- **Nível de risco** (1-10)
- **Histórico pessoal**
- **Necessidades específicas**

#### Dilemas Morais
O jogo apresenta dilemas complexos como:
- Devo sacrificar um para salvar cinco?
- Devo poupar o culpado?
- Devo punir o inocente?
- Devo priorizar o presente ou o futuro?

#### Consequências
Cada decisão tem consequências que afetam:
- População da base
- Moral dos habitantes
- Segurança da base
- Recursos disponíveis

### Múltiplos Finais

O jogo tem diferentes finais baseados em suas decisões:
- **O Herói da Base**: Você salvou muitas vidas e manteve a base segura
- **O Sobrevivente**: Você fez o que pôde para manter a base funcionando
- **Decisões Questionáveis**: Suas decisões foram controversas
- **O Fracasso**: Suas decisões levaram à morte de muitos

## Instalação e Execução

### Pré-requisitos
- Python 3.7 ou superior
- Pygame 2.5.2

### Instalação
1. Clone ou baixe este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Execução
```bash
python main.py
```

## Estrutura do Projeto

- `main.py`: Arquivo principal do jogo
- `character.py`: Classe para representar personagens
- `scenario_manager.py`: Gerenciador de cenários e dilemas
- `game_state.py`: Gerenciador de estado e estatísticas
- `ui_manager.py`: Gerenciador de interface do usuário
- `requirements.txt`: Dependências do projeto

## Desenvolvimento

Este jogo foi desenvolvido em Python usando Pygame para criar uma experiência visual imersiva. O foco está na narrativa e nos dilemas morais, apresentando situações complexas que não têm respostas certas ou erradas.

## Créditos

Desenvolvido como um projeto de jogo de dilemas morais em um cenário pós-apocalíptico. 