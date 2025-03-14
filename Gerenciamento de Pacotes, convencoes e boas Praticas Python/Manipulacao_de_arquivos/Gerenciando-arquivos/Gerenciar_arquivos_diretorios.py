import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent  # Obtém o diretório onde o script está

# # Definir o caminho do novo diretório corretamente
# novo_diretorio = ROOT_PATH / "Formação Python Backend Developer DIO" / "aqui alguma coisa"


# os.makedirs(novo_diretorio)

# # os.mkdir(ROOT_PATH / "novo_diretorio")

# # arquivo = open(ROOT_PATH / "novo.txt", "w")

# # arquivo.close()

# # os.rename(ROOT_PATH / "novo_nome.txt", ROOT_PATH / "novo_nome_alterado.txt")

# # arquivo_novo = open("novo_diretorio.txt")

# # os.remove(ROOT_PATH / "novo.txt")


# # shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo_diretorio" / "novo.txt")


# os.mkdir(ROOT_PATH / "Gerenciado-arquivos")


shutil.move(ROOT_PATH / "Gerenciar_arquivos_diretorios.py", ROOT_PATH / "Gerenciando-arquivos" / "Gerenciar_arquivos_diretorios.py")