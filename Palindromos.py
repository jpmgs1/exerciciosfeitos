def limpar_texto(texto):
    texto = texto.lower()
    texto_limpo = ""
    for caractere in texto:
        if caractere.isalnum():
            texto_limpo += caractere
    return texto_limpo

def eh_palindromo(texto):
    texto_limpo = limpar_texto(texto)
    return texto_limpo == texto_limpo[::-1]

def analisar_texto(texto):
    palavras = texto.split()
    qtd_palavras = len(palavras)
    qtd_com_espaco = len(texto)
    qtd_sem_espaco = len(texto.replace(" ", ""))
    palindromo = eh_palindromo(texto)

    print(43 * "-")
    print("             Resultados Final")
    print(43 * "-")
    print(f"Quantidade de palavras: {qtd_palavras}")
    print(f"Quantidade de caracteres (com espaços): {qtd_com_espaco}")
    print(f"Quantidade de caracteres (sem espaços): {qtd_sem_espaco}")
    print("SIM é um palíndromo!" if palindromo else "NÃO é um palíndromo.")
    print(43 * "-")

texto_usuario = input("Digite um texto para ser analisado: ")
analisar_texto(texto_usuario)
