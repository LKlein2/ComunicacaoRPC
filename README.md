Trabalho de comunicação cliente/servidor através de RPC.
Desenvolvido em conjunto com os colegas do curso de ciência da computação na universidade de caxias do sul.

Métodos de entrada esperados:

[
  {
    {
      "tituloLivro": "Harry Potter e o prisioneiro de Azkaban",
      "autorLivro": "Nome de alguem",
      "edicaoLivro": "Segunda",
      "anoPublicacaoLivro": 2010
    }
  },
  {
    {
      "autorLivro": "Nome de alguem"
    }
  },
  {
    {
      "tituloLivro": "Harry Potter e o prisioneiro de Azkaban"
    }
  },
  {
    {
      "edicaoLivro": "Segunda",
      "anoPublicacaoLivro": 2010
    }
  },
  {
    {
      "tituloLivro": "Harry Potter e o prisioneiro de Azkaban"
    }
  },
  {
    {
      "codigoLivro": "1",
      "tituloLivro": "Harry Potter e o prisioneiro de Azkaban",
      "autorLivro": "Nome de alguem",
      "edicaoLivro": "Segunda",
      "anoPublicacaoLivro": 2010
    }
  }
]

Execução no server: server_tcp.py {Porta}

Execução no client: client_tcp.py {IP server} {Porta server}
