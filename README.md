# RPG Overworld 2

Um RPG de texto em Python, jogado inteiramente pelo terminal — sem
bibliotecas gráficas, só lógica, estrutura e imaginação.

Este projeto nasceu como evolução direta do meu primeiro RPG em Python
(também neste perfil). Enquanto a primeira versão era um script único
baseado em variáveis globais e dicionários, o Overworld 2 foi
reconstruído do zero com Programação Orientada a Objetos, persistência
real em banco de dados e uma estrutura de mundo muito mais robusta.

## O que mudou da V1 para a V2

- **De variáveis globais para classes**: heróis, inimigos, itens,
  zonas e progressão agora são objetos com seu próprio estado e
  comportamento, não dicionários soltos.
- **Save/Load persistente com SQLite**: o progresso é salvo em banco
  de dados real (herói, inventário, magias, habilidades, eventos e
  amuletos do ferreiro), não se perde ao fechar o jogo.
- **Mundo dividido em zonas progressivas**, cada uma com seus próprios
  inimigos, chefe principal e um chefe especial opcional, mais difícil
  e com recompensas exclusivas.
- **Sistema de Fúria/Foco** além de mana, abrindo espaço para
  habilidades específicas de combate com custo próprio.
- **Ferreiro com amuletos de ataque e defesa**, incluindo itens
  exclusivos por vila.
- **Eventos e diálogos narrativos com efeito de digitação**, dando
  ritmo às cutscenes e reviravoltas da história (incluindo múltiplos
  finais).
- **Código modular**, separado por responsabilidade (herói, itens,
  inimigos, mundo, eventos, lore, habilidades), em vez de um único
  arquivo monolítico.

## Sobre o projeto

Esse é um projeto pessoal de aprendizado — cada sistema aqui foi uma
desculpa para aprender um conceito novo de Python: POO, SQLite,
manipulação de estado entre módulos, controle de fluxo mais complexo
e organização de projeto em múltiplos arquivos.
