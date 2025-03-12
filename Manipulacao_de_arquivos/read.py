#existem diferentes modos de abertura, Leitura r , gravacao w, anexar a


# #read() -----------------------------------------------------------

# file_path = "C:/Users/elloc/OneDrive/Desktop/Formação Python Backend Developer DIO/Manipulacao_de_arquivos/example_file.txt"

# documento_aberto = open(file_path, "r")

# lorem = documento_aberto.read()

# print(lorem)

# documento_aberto.close()


#readline() -----------------------------------------------------------

file_path = "C:/Users/elloc/OneDrive/Desktop/Formação Python Backend Developer DIO/Manipulacao_de_arquivos/lorem.txt"

lorem_aberto = open(file_path, "r")


while len(linha := lorem_aberto.readline()):
    print(linha)
lorem_aberto.close()

# #readlines() -----------------------------------------------------------

# file_path = "C:/Users/elloc/OneDrive/Desktop/Formação Python Backend Developer DIO/Manipulacao_de_arquivos/example_file.txt"

# documento_aberto_linha_a_linha = open(file_path, "r")

# mi_string = ""

# for linha in documento_aberto_linha_a_linha.readlines(1):
#     mi_string += linha + " o "

# print(mi_string)

# documento_aberto_linha_a_linha.close()

# #write
# file = open("","w")

# #attach
# file = open("","a")




