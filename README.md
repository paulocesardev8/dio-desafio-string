# dio-desafio-string

# Explicação do Código: Contar Caracteres de uma String

Este documento explica o funcionamento do código que conta a frequência de cada caractere em uma string fornecida pelo usuário. O código utiliza um dicionário para armazenar as contagens e permite identificar facilmente quantas vezes cada caractere aparece na string.

---

## **Descrição do Código**

### **Função `contar_caracteres`**
- **Propósito**: Contar a frequência de cada caractere em uma string.
- **Entrada**:
  - `string`: Uma string qualquer fornecida pelo usuário.
- **Processamento**:
  1. Cria um dicionário vazio chamado `contador`.
  2. Percorre cada caractere na string utilizando um laço `for`.
  3. Verifica se o caractere já existe como chave no dicionário:
     - Se sim, incrementa o valor associado a essa chave em 1.
     - Se não, adiciona o caractere como uma nova chave com o valor inicial 1.
  4. Retorna o dicionário contendo os caracteres como chaves e suas respectivas frequências como valores.
- **Saída**:
  - Um dicionário com os caracteres da string como chaves e seus respectivos números de ocorrências como valores.

**Exemplo de Uso**:
```python
contar_caracteres("banana")  # Retorna {'b': 1, 'a': 3, 'n': 2}
contar_caracteres("abcabc")  # Retorna {'a': 2, 'b': 2, 'c': 2}
```

---

### **Função `main`**
- **Propósito**: Gerenciar a interação com o usuário.
- **Entrada**:
  - Solicita uma string do usuário via `input()`.
- **Processamento**:
  1. Lê a string fornecida pelo usuário e a armazena na variável `entrada`.
  2. Chama a função `contar_caracteres` passando a string como argumento.
  3. Armazena o dicionário resultante em `resultado`.
- **Saída**:
  - Exibe o dicionário resultante com as contagens de caracteres no formato `{caractere: contagem}`.

### **Controle do Fluxo de Execução**
A linha:
```python
if _name_ == "_main_":
```
é usada para verificar se o arquivo está sendo executado diretamente. Contudo, está incorreta. A linha correta é:
```python
if __name__ == "__main__":
```

---

---

## **Exemplo de Execução**

### **Entrada**:
```
banana
```

### **Processo**:
1. A string fornecida é `"banana"`.
2. O programa percorre cada caractere na string e atualiza o dicionário `contador`:
   - `{'b': 1}` após processar `b`.
   - `{'b': 1, 'a': 1}` após processar o primeiro `a`.
   - `{'b': 1, 'a': 1, 'n': 1}` após processar o primeiro `n`.
   - Continua incrementando os valores conforme encontra caracteres repetidos.
3. O resultado final é `{'b': 1, 'a': 3, 'n': 2}`.

### **Saída**:
```
{'b': 1, 'a': 3, 'n': 2}
```

---


