# from pathlib import Path

# ROOT_PATH = Path(__file__).parent

# # Com o with o arquivo e fechado automaticamente ao finalizar o bloco de contexto, mesmo que seja gerado um erro, o que nao acontece utilizando open - close

# with open(ROOT_PATH / "lorem.txt" , "r") as arquivo:
#     1 / 0
# arquivo.close()
# print(arquivo.read())

from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Com o with o arquivo e fechado automaticamente ao finalizar o bloco de contexto, mesmo que seja gerado um erro, o que nao acontece utilizando open - close
try:
    with open(ROOT_PATH / "1lorem.txt" , "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipular arquivos em python ü")
except IOError as exc:
    name_err = type(exc).__name__
    print(f"erro ao abrir o arquivo: {name_err}")


try:
    with open(ROOT_PATH / "1lorem.txt" , "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    name_err = type(exc).__name__
    print(f"erro ao leer o arquivo: {name_err}")
except UnicodeDecodeError as exc:
    name_err = type(exc).__name__
    print(f"erro ao leer o arquivo: {name_err}")
