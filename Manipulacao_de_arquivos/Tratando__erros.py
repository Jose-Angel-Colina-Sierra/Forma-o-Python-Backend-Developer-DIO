from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt" , "r")
except FileNotFoundError as exc:
    nome_erro = type(exc).__name__
    print(nome_erro)
    print(f"Arquivo não encontrado {nome_erro}")
except IsADirectoryError as exc:
    nome_erro = type(exc).__name__
    print(nome_erro)
    print(f"Tentou abrir um diretório como arquivo {nome_erro}")
except IOError as exc:
    nome_erro = type(exc).__name__
    print(nome_erro)
    print(f"Erro ao abrir o arquivo:{nome_erro}")
except Exception as exc:
    nome_erro = type(exc).__name__
    print(nome_erro)
    print(f"Ocorreu um erro inesperado {nome_erro}")