from colorama import Fore, Style, init

init(autoreset=True)

niveis_reservatorio = [
    ("Nível 1", "Muito baixo (crítico)", Fore.RED),
    ("Nível 2", "Baixo", Fore.YELLOW),
    ("Nível 3", "Médio", Fore.GREEN),
    ("Nível 4", "Alto", Fore.CYAN),
    ("Nível 5", "Muito alto (alerta)", Fore.BLUE)
]

def exibir_alerta(nivel):
    nome, situacao, cor = nivel
    print(cor + f"{nome} - {situacao}" + Style.RESET_ALL)

print("=== Controle de Níveis de Água ===\n")

for nivel in niveis_reservatorio:
    exibir_alerta(nivel)

print("\nMonitoramento finalizado.")