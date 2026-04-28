# MissaoAurora-Aterrisagem
🚀 Missão Aurora Siger – Sistema de Aterrissagem (MGPEB)
📌 Descrição do Projeto

Este projeto simula o sistema de aterrissagem de uma missão espacial em Marte, chamado MGPEB (Módulo de Gerenciamento de Pouso e Estabilização de Base).

O objetivo é integrar conceitos de:

Matemática aplicada
Física
Programação em Python
Lógica computacional

O sistema é responsável por monitorar, analisar e decidir o pouso de módulos essenciais para a construção de uma base em Marte.

🧠 Conceitos Aplicados
📊 Modelagem Matemática

O projeto utiliza diferentes funções para simular variáveis reais da aterrissagem:

Altura da nave (movimento uniformemente acelerado)
h(t) = h₀ − v₀t − ½at²
Energia da nave (decaimento exponencial)
E(t) = E₀e⁻ᵏᵗ
Energia solar (função senoidal)
Representa variação ao longo do tempo
Pressão do combustível (função linear)
P(t) = P₀ − kt
Função erro
e(t) = h_sensor(t) − h_modelo(t)

Essa modelagem permite prever e corrigir o comportamento da nave em tempo real.

🖥️ Funcionalidades do Sistema

O sistema foi desenvolvido em Python e possui três principais modos:

▶️ 1. Inicialização do Sistema
Criação dos módulos da missão:
Habitação
Energia
Laboratório Científico
Logística
Suporte Médico
Organização em:
Lista
Fila de ativação (FIFO)
Ordem de pouso (por prioridade)
Exibição de tabela com:
Prioridade
Combustível
Massa
Criticidade
⚙️ 2. Sistema de Decisão

O sistema analisa cada módulo com base em regras como:

Combustível disponível
Prioridade
Massa
Criticidade

E retorna estados como:

✅ POUSO IMEDIATO
⚠️ AUTORIZADO COM MONITORAMENTO
❌ ADIADO
🚨 EMERGÊNCIA
📈 3. Análise Gráfica

Geração de gráficos utilizando Matplotlib:

📊 Prioridade dos módulos
⚠️ Margem de erro (risco)

A margem de erro é calculada com base em:

Massa
Combustível restante
Criticidade
🔌 Lógica de Decisão (Portas Lógicas)

O pouso só é autorizado se todas as condições forem verdadeiras:

AUTORIZAR = C AND A AND P AND S
ADIAR = NOT (C AND A AND P AND S)

Onde:

C = Combustível suficiente
A = Atmosfera adequada
P = Pista disponível
S = Sensores operacionais

✔️ Segurança máxima: qualquer falha impede o pouso

🧱 Estruturas de Dados Utilizadas
list → armazenamento dos módulos
deque → fila de ativação
dict → representação dos módulos
sorted() → ordenação por prioridade
⏱️ Recursos do Sistema
Simulação em tempo real com datetime e pytz
Interface via terminal (CLI)
Visualização gráfica com matplotlib
Lógica de decisão automatizada
🌱 Princípios ESG Aplicados

O projeto também considera:

🌍 Ambiental: uso de energia solar
👥 Social: segurança da tripulação
🏛️ Governança: decisões baseadas em dados
🚀 Como Executar o Projeto
Pré-requisitos

Instale as bibliotecas necessárias:

pip install matplotlib pytz
Execução
python fase2Aurora-Siger.py
Menu do sistema:
0 → Encerrar
1 → Iniciar sistema
2 → Análise de gráficos

👨‍🚀 Tripulação

Nome:                                RM:
Calebe Gonçalves Garcia de Souza     RM568743
Filipe Souza Nascimento              RM573758
Lucas Ribeiro Gesini                 RM569383
Paulo Henrique Gonçalves Bueno       RM570456
Raphael de Freitas Silva             RM570089

O MGPEB representa um sistema embarcado capaz de tomar decisões críticas em tempo real, simulando desafios reais da exploração espacial.
