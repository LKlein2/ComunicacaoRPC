import sys
import json
import xmlrpc.client

def jsonPrettyPrint(jsonString):
    parsed = json.loads(jsonString)
    return json.dumps(parsed, indent=4, sort_keys=False)

def criarJson(codigoLivro, tituloLivro, autorLivro, edicaoLivro, anoPublicacaoLivro):
    livros = {}

    if (codigoLivro > 0)        : livros["codigoLivro"] = codigoLivro
    if (tituloLivro != "")      : livros["tituloLivro"] = tituloLivro
    if (autorLivro != "")       : livros["autorLivro"]  = autorLivro
    if (edicaoLivro != "")      : livros["edicaoLivro"] = edicaoLivro
    if (anoPublicacaoLivro > 0) : livros["anoPublicacaoLivro"] = anoPublicacaoLivro

    json_output = json.dumps(livros)
    return json_output

def comunicarServidor(operation, json_input):
    servidor = xmlrpc.client.ServerProxy('http://' + ip + ':' + porta)

    if (operation == "CriarLivro") :
        response = servidor.CriarLivro(json_input)
    elif (operation == "ConsultarLivroAutor") :
        response = servidor.ConsultarLivroAutor(json_input)
    elif (operation == "ConsultarLivroTitulo") :
        response = servidor.ConsultarLivroTitulo(json_input)
    elif (operation == "ConsultarLivroPorAnoEdicao") :
        response = servidor.ConsultarLivroPorAnoEdicao(json_input)
    elif (operation == "RemoverLivro") :
        response = servidor.RemoverLivro(json_input)
    elif (operation == "AlterarLivro") :
        response = servidor.AlterarLivro(json_input)

    return response    

def menuPrincipal():
    print('''
            [Consulta de livros] - Selecione uma opção:
            [1] - Criar livro
            [2] - Consultar livro
            [3] - Consultar por ano e edição
            [4] - Remover livro
            [5] - Alterar livro
            [6] - Sair
        ''')

def menu1():
    print("Título:")
    tituloLivro = str(input())

    print("Autor:")
    autorLivro = str(input())

    print("Edição:")
    edicaoLivro = str(input())

    print("Ano de publicação:")
    anoPublicacaoLivro = int(input())
    
    livroString = criarJson(0,tituloLivro,autorLivro,edicaoLivro,anoPublicacaoLivro)
    
    msg = comunicarServidor("CriarLivro",livroString)
    print(msg)

def menu2():
    escolhaMenu2 = 0

    print('''           
            [Consultar livro]
            [1] - Consultar pelo autor
            [2] - Consultar pelo título
            [3] - Voltar
    ''')
    escolhaMenu2 = int(input('Escolha uma opção: '))

    if (escolhaMenu2 == 1):
        print("Autor:")
        autorLivro = str(input())

        livroString = criarJson(0,"",autorLivro,"",0)
        msg = comunicarServidor("ConsultarLivroAutor",livroString)
        print(jsonPrettyPrint(msg))

    elif (escolhaMenu2 == 2):
        print("Título:")
        tituloLivro = str(input())

        livroString = criarJson(0,tituloLivro,"","",0)
        msg = comunicarServidor("ConsultarLivroTitulo",livroString)
        print(jsonPrettyPrint(msg))

    elif (escolhaMenu2 == 3):
        return

    elif (escolhaMenu2 > 3):
        print("Opção inválida! Tente novamente.")

def menu3():
    print("Ano do livro: ")
    anoPublicacaoLivro = int(input())

    print("Numero da edição livro: ")
    edicaoLivro = str(input())

    livroString = criarJson(0,"","",edicaoLivro,anoPublicacaoLivro)
    msg = comunicarServidor("ConsultarLivroPorAnoEdicao",livroString)
    print(jsonPrettyPrint(msg))

def menu4():
    print("Título:")
    tituloLivro = str(input())

    livroString = criarJson(0,tituloLivro,"","",0)
    msg = comunicarServidor("RemoverLivro",livroString)
    print(msg)

def menu5():
    print("Título:")
    tituloLivro = str(input())

    livroString = criarJson(0,tituloLivro,"","",0)
    msg = comunicarServidor("ConsultarLivroTitulo",livroString)
    if (msg == "[]"):
        print("Nenhum livro encontrado!")
        return

    json_input = json.loads(msg)

    escolhaMenu5 = 0
    while (escolhaMenu5 != 5):
        print('''            
            [Alterar livro]
            [1] - Alterar autor
            [2] - Alterar título
            [3] - Alterar edição
            [4] - Alterar ano de publicação"
            [5] - Voltar
        ''')
        escolhaMenu5 = int(input('Escolha uma opção: '))

        if (escolhaMenu5 == 1):
            print("Autor:")
            autorLivro = str(input())

            for livro in json_input:
                livro['autorLivro'] = autorLivro
                msg = comunicarServidor("AlterarLivro", json.dumps(livro))
                print(msg)
                return

        elif (escolhaMenu5 == 2): 
            print("Título:")
            tituloLivro = str(input())

            for livro in json_input:
                livro['tituloLivro'] = tituloLivro
                msg = comunicarServidor("AlterarLivro", json.dumps(livro))
                print(msg)                
                return

        elif (escolhaMenu5 == 3):
            print("Edição:")
            edicaoLivro = str(input())

            for livro in json_input:
                livro['edicaoLivro'] = edicaoLivro
                msg = comunicarServidor("AlterarLivro", json.dumps(livro))
                print(msg)
                return

        elif (escolhaMenu5 == 4):
            print("Ano de publicação:")
            anoPublicacaoLivro = int(input())

            for livro in json_input:
                livro['anoPublicacaoLivro'] = anoPublicacaoLivro
                msg = comunicarServidor("AlterarLivro", json.dumps(livro))
                print(msg)
                return

        elif (escolhaMenu5 == 5):
            return

        elif (escolhaMenu5 > 5):
            print("Opção inválida! Tente novamente.")
            

def mainMenu():
	escolhaPrincipal = 0

	while (escolhaPrincipal != 6):
		menuPrincipal()
		escolhaPrincipal = int(input('Escolha uma opção: '))

		if (escolhaPrincipal == 1):
			menu1()    

		elif (escolhaPrincipal == 2):
			menu2()

		elif (escolhaPrincipal == 3):
			menu3()

		elif (escolhaPrincipal == 4):
			menu4()

		elif (escolhaPrincipal == 5):
			menu5()

		elif (escolhaPrincipal > 6):
			print("Opção inválida! Tente novamente.")


# if len(sys.argv) != 3:
#     print('%s <ip> <porta>' %sys.argv[0])
#     sys.exit(0)

# ip = sys.argv[1]
# porta = sys.argv[2]

ip = "localhost"
porta = "5000"

mainMenu()