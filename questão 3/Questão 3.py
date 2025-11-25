def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Valor inválido! Digite um número.")

def ler_status(resposta):
    while True:
        try:
            status = str(input(resposta))
            print(status)
            if (status == "Lido"):
                return status
            elif (status == "Lendo"):
                return status
            elif (status == "Na Fila"):
                return status
            else:
                print('Resposta inválida!')
        except IndexError:
            print('Resposta inválida, digite novamente')

try:
   
    with open("livros.txt", "r") as arquivo:
        livros = arquivo.readlines()

    with open("livros_avaliacao.txt", "w") as arquivo:
        arquivo.write(",Nota\n")

    for livro in livros:
        livro = livro.strip()  

      
        nota = ler_nota(f"Digite a nota de 0 a 10 para o livro '{livro}': ")
        status = ler_status(f"Digite o Status de Lido, Lendo ou Na fila '{livro}: ")

        

       
        with open("livros_avaliacao.txt", "a") as arquivo:
            arquivo.write(f"{livro},{nota}, {status}\n")

            break

    print("Avaliações salvas em 'livros_avaliacao.txt' com sucesso!")

except FileNotFoundError:
    print("Erro: o arquivo 'Livros.txt' não foi encontrado.")
