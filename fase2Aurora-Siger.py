# Importaçao das Classes
from collections import deque
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
import time

fuso_brasilia = pytz.timezone("America/Sao_Paulo")  # Horário em tempo real
sistema_iniciado = False
while True:
    opcao = int(input("""
    Deseja iniciar o protocolo de aterrissagem?
    Encerrar Sistema? Digite 0
    Iniciar Sistema: Digite 1
    Analise de Graficos: Digite 2
    """))

    match opcao:
        case 1:
            sistema_iniciado = True
            print("Sistema iniciado com sucesso!")
            print("Inicializando o protocolo de Verificaçao dos Modulos...")
            time.sleep(0.5)
            print("Criando Ordem De Ativaçao...")
            time.sleep(0.5)
            print("Definindo Ordem De Pouso Dos Modulos...")
            time.sleep(0.5)

            # Definição dos módulos
            modulo_habitacao = {
                "id": 1,
                "nome": "Habitação",
                "descricao": "Módulo residencial da tripulação",
                "capacidade": 6,
                "status": "operacional",
                "prioridade": 2,
                "combustivel": 80,
                "massa": 12000,
                "criticidade": 5,
                "horario": datetime.now(fuso_brasilia)
            }

            modulo_energia = {
                "id": 2,
                "nome": "Energia",
                "descricao": "Geração e distribuição de energia solar",
                "capacidade": 0,
                "status": "operacional",
                "prioridade": 1,
                "combustivel": 60,
                "massa": 15000,
                "criticidade": 5,
                "horario": datetime.now(fuso_brasilia)
            }

            modulo_laboratorio = {
                "id": 3,
                "nome": "Laboratório Científico",
                "descricao": "Pesquisas e experimentos",
                "capacidade": 4,
                "status": "operacional",
                "prioridade": 3,
                "combustivel": 70,
                "massa": 10000,
                "criticidade": 4,
                "horario": datetime.now(fuso_brasilia)
            }

            modulo_logistica = {
                "id": 4,
                "nome": "Logística",
                "descricao": "Armazenamento de suprimentos",
                "capacidade": 0,
                "status": "operacional",
                "prioridade": 4,
                "combustivel": 90,
                "massa": 20000,
                "criticidade": 3,
                "horario": datetime.now(fuso_brasilia)
            }

            modulo_suporte_medico = {
                "id": 5,
                "nome": "Suporte Médico",
                "descricao": "Monitoramento de saúde",
                "capacidade": 2,
                "status": "operacional",
                "prioridade": 2,
                "combustivel": 50,
                "massa": 8000,
                "criticidade": 5,
                "horario": datetime.now(fuso_brasilia)
            }

            lista_modulos = [
                modulo_habitacao,
                modulo_energia,
                modulo_laboratorio,
                modulo_logistica,
                modulo_suporte_medico
            ]

            print("=" * 60)
            print("----------------------LISTA DE MÓDULOS----------------------")
            print("=" * 60)

            for i, m in enumerate(lista_modulos):
                print(f"[{i}] {m['nome']} - {m['descricao']}")

            # FILA
            fila = [
                modulo_energia,
                modulo_suporte_medico,
                modulo_habitacao,
                modulo_logistica,
                modulo_laboratorio
            ]

            print("\nFILA DE ATIVAÇÃO:")
            for i, m in enumerate(fila):
                print(f"{i+1}º → {m['nome']}")

            # ORDEM DE POUSO
            ordenados = sorted(lista_modulos, key=lambda m: m["prioridade"])

            print("\nORDEM DE POUSO:")
            for m in ordenados:
                print(m["nome"], "-", m["prioridade"])

            # ===============================
            # TABELA DOS MODULOS - DADOS
            # ===============================
            print("\nTABELA DE DADOS DOS MÓDULOS:\n")

            print(f"{'Nome':<25} {'Prioridade':<12} {'Combustível':<12} {'Massa':<10} {'Criticidade':<12}")
            print("-" * 75)

            for m in lista_modulos:
                print(f"{m['nome']:<25} {m['prioridade']:<12} {m['combustivel']:<12} {m['massa']:<10} {m['criticidade']:<12}")

                for m in ordenados:
                    if m["criticidade"] >= 5 and m["prioridade"] == 1:
                        print(f"{m['nome']}: POUSO IMEDIATO")

                    elif m["prioridade"] == 1 and m["combustivel"] >= 50:
                        print(f"{m['nome']}: POUSO AUTORIZADO")

                    elif m["combustivel"] < 40:
                        print(f"{m['nome']}: EMERGÊNCIA")

                    elif m["massa"] > 15000:
                        print(f"{m['nome']}: AGUARDAR")

                    elif m["prioridade"] == 2:
                        print(f"{m['nome']}: AUTORIZADO COM MONITORAMENTO")

                    else:
                        print(f"{m['nome']}: ADIADO")

        case 2:
            if not sistema_iniciado:
                print("❌ ERRO: Você precisa iniciar o sistema primeiro (opção 1)")
                continue
            print("ABRINDO INTERFACE GRAFICA DOS MODULOS....")
            time.sleep(2)
            fila_pouso = deque()

            fila_pouso.extend([
                {"nome": "Habitação", "prioridade": 2, "combustivel": 80, "massa": 12000, "criticidade": 5},
                {"nome": "Energia", "prioridade": 1, "combustivel": 60, "massa": 15000, "criticidade": 5},
                {"nome": "Laboratório Científico", "prioridade": 5, "combustivel": 70, "massa": 10000, "criticidade": 4},
                {"nome": "Logística", "prioridade": 4, "combustivel": 90, "massa": 20000, "criticidade": 3},
                {"nome": "Suporte Médico", "prioridade": 3, "combustivel": 50, "massa": 8000, "criticidade": 5}
            ])

            nomes = [m["nome"] for m in fila_pouso]
            prioridades = [m["prioridade"] for m in fila_pouso]

            # ===========================
            # ORDENAR POR PRIORIDADE
            # ===========================
            fila_ordenada = sorted(fila_pouso, key=lambda m: m["prioridade"])

            nomes = [m["nome"] for m in fila_ordenada]
            prioridades = [m["prioridade"] for m in fila_ordenada]

            # ===========================
            # CÁLCULO DA MARGEM DE ERRO
            # ===========================
            margem_erro = [
                (m["massa"] / 1000) + (100 - m["combustivel"]) + (m["criticidade"] * 2)
                for m in fila_ordenada
            ]

            # ====================================
            # GRÁFICOS
            # ====================================
            plt.figure(figsize=(12, 5))

            # Gráfico 1 - Prioridade (ordenado)
            plt.subplot(1, 2, 1)
            plt.bar(nomes, prioridades, color='green')
            plt.title("Prioridade dos Módulos (Crescente)")
            plt.xlabel("Nível de Prioridade - menor nivel + prioridade")

            # Gráfico 2 - Margem de erro (mesma ordem)
            plt.subplot(1, 2, 2)
            plt.bar(nomes, margem_erro, color='blue')
            plt.title("Margem de Erro (Risco)")
            plt.xlabel("Índice de Risco")

            plt.tight_layout()
            plt.show()

        case 0:
            print("Encerrando sistema")
            break

        case _:
            print("Opção inválida")