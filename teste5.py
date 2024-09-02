def inverter_string(s):
    invertida = ''
    
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    
    return invertida

entrada = input("Digite a string para inverter: ")

resultado = inverter_string(entrada)

print(f"String invertida: {resultado}")
