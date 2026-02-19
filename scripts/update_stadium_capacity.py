import json
import copy

# Constante de aumento percentual
# Ex: 1.5 = aumento de 50% | 1.2 = aumento de 20% | 2.0 = dobrar a capacidade
CAPACITY_MULTIPLIER = 1.5

INPUT_FILE = "league.json"
OUTPUT_FILE = "league_new.json"


def update_stadium_capacity(data, multiplier):
    """Percorre recursivamente o JSON e atualiza todos os valores de stadiumCapacity."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "stadiumCapacity" and isinstance(value, (int, float)):
                data[key] = round(value * multiplier)
            else:
                update_stadium_capacity(value, multiplier)
    elif isinstance(data, list):
        for item in data:
            update_stadium_capacity(item, multiplier)


def main():
    # Lê o arquivo original
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Cria uma cópia profunda para não modificar o original em memória
    new_data = copy.deepcopy(data)

    # Aplica o multiplicador
    update_stadium_capacity(new_data, CAPACITY_MULTIPLIER)

    # Salva o novo arquivo
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

    print(f"Arquivo '{OUTPUT_FILE}' gerado com sucesso!")
    print(f"Multiplicador aplicado: {CAPACITY_MULTIPLIER}x "
          f"(aumento de {(CAPACITY_MULTIPLIER - 1) * 100:.0f}%)")


if __name__ == "__main__":
    main()
