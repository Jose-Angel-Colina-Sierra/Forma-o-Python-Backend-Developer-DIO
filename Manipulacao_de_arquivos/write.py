# new_file = r"C:\Users\elloc\OneDrive\Desktop\Formação Python Backend Developer DIO\Manipulacao_de_arquivos\novo_arquivo_write.txt"

# new_file_open_write = open(new_file, "w")

# new_file_open_write.write("Escrevendo dados no novo arquivo")

# new_file_open_write.close()

# new_file_open_read = open(new_file, "r")

# new_file_reading = new_file_open_read.readlines()

# base_string = ""

# for line in new_file_reading:
#     print(base_string + line)

# new_file_open_read.close()

# new_file_open_write = open(new_file, "w")

# new_file_open_write.writelines("python")


file_path = r"C:\Users\elloc\OneDrive\Desktop\Formação Python Backend Developer DIO\Manipulacao_de_arquivos\novo_arquivo_write.txt"


file = open(file_path,"w")

file.write("I'm writing on the new document\n")
file.writelines([">I'm adding new iterable object\n",">this is other iterable item the same object\n",">It's very good\n"])

file.close()