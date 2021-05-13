import xmlrpc.server
import sys
import json

def ConsultarBaseLivros():
	try:
		with open("baseDados.json", "r") as json_file:
			dados = json.load(json_file)
	except:
		dados = json.loads('[]')
	return dados

def PersistirBaseLivros(baseLivros):
	with open("baseDados.json", "w") as json_file:
		json.dump(baseLivros, json_file, indent=4)

def CriarLivro(json_input):
	livro = json.loads(json_input)
	baseLivros = ConsultarBaseLivros()
	livro_novo = {}

	livro_novo["codigoLivro"] = 0
	livro_novo["tituloLivro"] = livro["tituloLivro"]
	livro_novo["autorLivro"] = livro["autorLivro"]
	livro_novo["edicaoLivro"] = livro["edicaoLivro"]
	livro_novo["anoPublicacaoLivro"] = livro["anoPublicacaoLivro"]

	ultimoCodigo = 0
	for livro in baseLivros:
		if (livro["codigoLivro"] > ultimoCodigo):
			ultimoCodigo = livro["codigoLivro"]

	livro_novo["codigoLivro"] = ultimoCodigo + 1

	baseLivros.append(livro_novo)
	PersistirBaseLivros(baseLivros)
	return ("Livro inserido com sucesso!")

def ConsultarLivroAutor(json_input):
	livro_consulta = json.loads(json_input)
	baseLivros = ConsultarBaseLivros()
	livrosRetorno = json.loads('[]')

	for livro in baseLivros:
		if (livro["autorLivro"] == livro_consulta["autorLivro"]):
			livrosRetorno.append(livro)

	return json.dumps(livrosRetorno)


def ConsultarLivroTitulo(json_input):
	livro_consulta = json.loads(json_input)
	baseLivros = ConsultarBaseLivros()
	livrosRetorno = json.loads('[]')

	for livro in baseLivros:
		if (livro["tituloLivro"] == livro_consulta["tituloLivro"]):
			livrosRetorno.append(livro)

	return json.dumps(livrosRetorno)


def ConsultarLivroPorAnoEdicao(json_input):
	livro_consulta = json.loads(json_input)
	baseLivros = ConsultarBaseLivros()
	livrosRetorno = json.loads('[]')

	for livro in baseLivros:
		if (livro["edicaoLivro"] == livro_consulta["edicaoLivro"] and livro["anoPublicacaoLivro"] == livro_consulta["anoPublicacaoLivro"]):
			livrosRetorno.append(livro)

	return json.dumps(livrosRetorno)


def RemoverLivro(json_input):
	livro_exclusao = json.loads(json_input)
	baseLivros = ConsultarBaseLivros()

	for livro in baseLivros:
		if (livro["tituloLivro"] == livro_exclusao["tituloLivro"]):
			baseLivros.remove(livro)

	PersistirBaseLivros(baseLivros)
	return "Livro removido com sucesso!"


def AlterarLivro(json_input):
	livro_alteracao = json.loads(json_input)
	baseLivros = ConsultarBaseLivros()

	for livro in baseLivros:
		if (livro["codigoLivro"] == livro_alteracao["codigoLivro"]):
			baseLivros.remove(livro)
			baseLivros.append(livro_alteracao)

	PersistirBaseLivros(baseLivros)
	return "Livro alterado com sucesso!"

if len(sys.argv) != 2:
	print ('%s <porta>' % sys.argv[0]) 
	sys.exit(0)

porta = int(sys.argv[1])

servidor = xmlrpc.server.SimpleXMLRPCServer(("localhost", porta))

servidor.register_function(CriarLivro, "CriarLivro")
servidor.register_function(ConsultarLivroAutor, "ConsultarLivroAutor")
servidor.register_function(ConsultarLivroTitulo, "ConsultarLivroTitulo")
servidor.register_function(ConsultarLivroPorAnoEdicao, "ConsultarLivroPorAnoEdicao")
servidor.register_function(RemoverLivro, "RemoverLivro")
servidor.register_function(AlterarLivro, "AlterarLivro")

servidor.serve_forever()

#------------- TESTE -------------
# livroteste = '{ "codigoLivro": "1", "tituloLivro": "Harry Potter e o prisioneiro de Azkaban", "autorLivro": "Nome de alguem", "edicaoLivro": "Segunda", "anoPublicacaoLivro": 2010 }'
# livroteste = '{"tituloLivro": "RPC99", "autorLivro": "9999", "edicaoLivro": "9999", "anoPublicacaoLivro": 9999}'
# CriarLivro(livroteste)
#------------        -------------