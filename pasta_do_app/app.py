import random
import string

def gerar_senha(tamanho, incluir_maiusculas=True, incluir_numeros=True, incluir_especiais=True):
  
    if tamanho < 1 or tamanho > 30 :
        raise ValueError("O tamanho da senha deve ser maior que 0 e menor que 30.")
    
    #Strings agrupando chars de diferentes categorias
    grupo_minusculas = string.ascii_lowercase
    grupo_maiusculas = string.ascii_uppercase if incluir_maiusculas else ""
    grupo_numeros = string.digits if incluir_numeros else ""
    grupo_especiais = "!@#" if incluir_especiais else ""
    
    todos_chars = grupo_minusculas + grupo_maiusculas + grupo_numeros + grupo_especiais
    
    senha = []
    if incluir_maiusculas:
        senha.append(random.choice(grupo_maiusculas))
    if incluir_numeros:
        senha.append(random.choice(grupo_numeros))
    if incluir_especiais:
        senha.append(random.choice(grupo_especiais))
    
    resto_da_senha = tamanho - len(senha)
    senha += random.choices(todos_chars, k=resto_da_senha)
    
    random.shuffle(senha)
    
    return ''.join(senha)
