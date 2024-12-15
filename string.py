def contar_caracteres(string):
    # Inicializa um dicionário vazio para armazenar as contagens de caracteres
    contador = {}
    
    # Itera através de cada caractere na string
    for caractere in string:
        # Verifica se o caractere já está no dicionário
        if caractere in contador:
            # Incrementa o valor associado a essa chave
            contador[caractere] += 1
        else:
            # Adiciona a chave ao dicionário com valor inicial 1
            contador[caractere] = 1
    
    return contador

# Função principal para testar a função contar_caracteres
def main():
    # Lê a entrada do usuário
    entrada = input()
    
    # Obtém o dicionário de contagem de caracteres
    resultado = contar_caracteres(entrada)
    
    # Exibe o resultado no formato especificado
    print(resultado)

# Chama a função principal
if __name__ == "__main__":
    main()
