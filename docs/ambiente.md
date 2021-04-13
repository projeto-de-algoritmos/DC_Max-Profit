## Instalação 

**Linguagem**: Python<br>

**Biblioteca**: pip3<br>

O projeto foi criado em um ambiente de desenvolvimento linux utilizando a IDE [VSCode](https://code.visualstudio.com/)

1. Inicialmente, caso não haja uma versão instalada, instale o [python3](https://www.python.org/downloads/)
2. Caso esteja utilizando o VSCode, é interessante instalar as extensões [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) e [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Uso 

Para uso do projeto basta rodar o projeto a partir da pasta do projeto.
  ```bash
  python3 main.py
  ```
Ao utilizar esse metódo, basta seguir as requisições do terminal e registrar as requiridas atividades.
Para realizar o cadastro mais rapidamente, pode ser útil inicializar o programa com um arquivo de texto contendo as tarefas, o modelo do arquivo é mostrado abaixo.
  ```C
  1//Aqui deve ser colocado a periodicidade da entrada 1-mensal 2-semestral 3-anual
  4.5//as 'N' linhas seguintes são os lucros naquele período
  -1
  -2.3
  5
  -1
  4
  -5
  -3.1
  10
  fim//é necessário indicar o fim dos períodos
  2//Aqui se indica a periodicidade da sáida
  ```
Para executar o código com auxílio do arquivo texto basta seguir esse exemplo. O exemplo acima está disponível no repositório como `test2.txt`
  ```bash
  python3 sources/main.py < seuarquivo.txt
  ```
Obs.: No repositório há os arquivos `test1.txt` e `test2.txt` previamente preenchidos como exemplo para teste