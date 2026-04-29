# =========================
# IMPORTAÇÕES
# =========================
from collections import deque
from datetime import datetime
import pytz
import matplotlib.pyplot as plt
import time

# =========================
# CONFIGURAÇÃO DE HORÁRIO
# =========================
fuso_brasilia = pytz.timezone("America/Sao_Paulo")

sistema_iniciado = False

# =========================
# LOOP PRINCIPAL
# =========================
while True:
    try:
        opcao = int(input("""
Deseja iniciar o protocolo de aterrissagem?
0 → Encerrar Sistema
1 → Iniciar Sistema
2 → Análise de Gráficos
"""))
    except:
        print("❌ Entrada inválida! Digite um número.")
        continue

    match opcao:

        # =========================
        # INICIAR SISTEMA
        # =========================
        case 1:
            sistema_iniciado = True
            print("\n✅ Sistema iniciado com sucesso!")
            time.sleep(1)

            # =========================
            # MÓDULOS COM HORÁRIO
            # =========================
            lista_modulos = [
                {
                    "nome": "Habitação",
                    "prioridade": 2,
                    "combustivel": 80,
                    "massa": 12000,
                    "criticidade": 5,
                    "horario": datetime.now(fuso_brasilia)
                },
                {
                    "nome": "Energia",
                    "prioridade": 1,
                    "combustivel": 60,
                    "massa": 15000,
                    "criticidade": 5,
                    "horario": datetime.now(fuso_brasilia)
                },
                {
                    "nome": "Laboratório",
                    "prioridade": 3,
                    "combustivel": 70,
                    "massa": 10000,
                    "criticidade": 4,
                    "horario": datetime.now(fuso_brasilia)
                },
                {
                    "nome": "Logística",
                    "prioridade": 4,
                    "combustivel": 90,
                    "massa": 20000,
                    "criticidade": 3,
                    "horario": datetime.now(fuso_brasilia)
                },
                {
                    "nome": "Suporte Médico",
                    "prioridade": 2,
                    "combustivel": 50,
                    "massa": 8000,
                    "criticidade": 5,
                    "horario": datetime.now(fuso_brasilia)
                }
            ]

            # =========================
            # ORDENAÇÃO
            # =========================
            ordenados = sorted(lista_modulos, key=lambda m: m["prioridade"])

            print("\n📦 ORDEM DE POUSO:")
            for m in ordenados:
                print(f"{m['nome']} - Prioridade {m['prioridade']}")

            # =========================
            # TABELA
            # =========================
            print("\n📊 TABELA DOS MÓDULOS:")
            print(f"{'Nome':<20} {'Prioridade':<10} {'Combustível':<12} {'Massa':<10} {'Criticidade':<12} {'Horário':<20}")
            print("-" * 100)

            for m in ordenados:
                horario_formatado = m["horario"].strftime("%d/%m/%Y %H:%M:%S")

                print(f"{m['nome']:<20} {m['prioridade']:<10} {m['combustivel']:<12} {m['massa']:<10} {m['criticidade']:<12} {horario_formatado:<20}")

            # =========================
            # DECISÃO DO SISTEMA
            # =========================
            print("\n🧠 DECISÃO DO SISTEMA:")
            for m in ordenados:

                horario_formatado = m["horario"].strftime("%H:%M:%S")

                if m["criticidade"] >= 5 and m["prioridade"] == 1:
                    status = "🚀 POUSO IMEDIATO"

                elif m["prioridade"] == 1 and m["combustivel"] >= 50:
                    status = "✅ POUSO AUTORIZADO"

                elif m["combustivel"] < 40:
                    status = "🚨 EMERGÊNCIA"

                elif m["massa"] > 15000:
                    status = "⏳ AGUARDAR"

                elif m["prioridade"] == 2:
                    status = "⚠️ MONITORAMENTO"

                else:
                    status = "❌ ADIADO"

                print(f"{m['nome']} ({horario_formatado}): {status}")

        # =========================
        # GRÁFICOS
        # =========================
        case 2:
            if not sistema_iniciado:
                print("❌ Inicie o sistema primeiro!")
                continue

            print("📈 Gerando gráficos...")
            time.sleep(1)

            fila = deque([
                {"nome": "Habitação", "prioridade": 2, "combustivel": 80, "massa": 12000, "criticidade": 5},
                {"nome": "Energia", "prioridade": 1, "combustivel": 60, "massa": 15000, "criticidade": 5},
                {"nome": "Laboratório", "prioridade": 5, "combustivel": 70, "massa": 10000, "criticidade": 4},
                {"nome": "Logística", "prioridade": 4, "combustivel": 90, "massa": 20000, "criticidade": 3},
                {"nome": "Suporte Médico", "prioridade": 3, "combustivel": 50, "massa": 8000, "criticidade": 5}
            ])

            ordenados = sorted(fila, key=lambda m: m["prioridade"])

            nomes = [m["nome"] for m in ordenados]
            prioridades = [m["prioridade"] for m in ordenados]

            margem_erro = [
                (m["massa"] / 1000) + (100 - m["combustivel"]) + (m["criticidade"] * 2)
                for m in ordenados
            ]

            plt.figure(figsize=(10, 4))

            plt.subplot(1, 2, 1)
            plt.bar(nomes, prioridades, color = 'Green')
            plt.title("Prioridade")

            plt.subplot(1, 2, 2)
            plt.bar(nomes, margem_erro, color = 'Blue')
            plt.title("Risco")

            plt.tight_layout()
            plt.show()

        # =========================
        # ENCERRAR
        # =========================
        case 0:
            print("🔴 Sistema encerrado.")
            break

        case _:
            print("❌ Opção inválida.")