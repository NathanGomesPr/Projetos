# Solicita a entrada do usuário
num_hex = input("Digite um número na base hexadecimal: ")

# Converter hexadecimal para binário
num_bin = bin(int(num_hex, 16))[2:]

# Converter hexadecimal para octal
num_oct = oct(int(num_hex, 16))[2:]

# Converter hexadecimal para heptadecimal
num_hep = ""
for i in range(0, len(num_hex), 7):
    # Obter um grupo de até 7 dígitos hexadecimais
    hex_group = num_hex[i:i+7]
    # Converter o grupo para decimal e depois para heptadecimal
    hep_digit = oct(int(hex_group, 16))[2:]
    # Adicionar o dígito heptadecimal ao resultado final
    num_hep += hep_digit

# Imprimir os resultados
print("Hexadecimal: " + num_hex)
print("Binário: " + num_bin)
print("Octal: " + num_oct)
print("Heptadecimal: " + num_hep)