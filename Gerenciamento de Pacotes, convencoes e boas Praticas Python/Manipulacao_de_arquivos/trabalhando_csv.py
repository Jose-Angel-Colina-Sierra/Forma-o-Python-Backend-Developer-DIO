import csv

from pathlib import Path

ROOT_PATH = Path(__file__).parent
try:
    with open(ROOT_PATH / "example.csv", "w", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["ID", "Nome"])
        writer.writerow(["1", "Jose"])
        writer.writerow(["2", "Rosa"])
except IOError as exc:
    print(f"Erro ao criar o arquivo {exc}")

try:
    with open(ROOT_PATH / "example.csv", "r", newline="",encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar o arquivo {exc}")

ID_COLUMN = 0
NAME_COLUMN = 1

try:
    with open(ROOT_PATH / 'example.csv', "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            print(f"ID: {row[ID_COLUMN]}, Nome: {row[NAME_COLUMN]}")
except IOError as exc:
    print(f"Erro ao ler o arquivo {exc}")


ID_COLUMN = "ID"
NAME_COLUMN = "Nome"

try:
    with open(ROOT_PATH / 'example.csv', "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        lista_campos = reader.fieldnames

        for field in lista_campos:
            print(field)

        for row in reader:
            print(f"ID: {row[ID_COLUMN]}, Nome: {row[NAME_COLUMN]}")
except IOError as exc:
    print(f"Erro ao ler o arquivo {exc}")


