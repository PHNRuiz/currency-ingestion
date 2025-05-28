Projeto de Ingestão de Dados de Câmbio (Script Procedural)

Este projeto consiste em um script Python (etlProcedural.py) que implementa um pipeline ETL (Extract, Transform, Load) simples para buscar dados de taxas de câmbio (Real e Euro) da API freecurrencyapi.com e salvá-los em um banco de dados PostgreSQL.

Funcionalidades:
  
  Extração: Busca as cotações mais recentes da API freecurrencyapi.com.
  
  Transformação: Extrai os valores do Real (BRL) e Euro (EUR) da resposta da API e os prepara para o banco de dados, adicionando um timestamp.
  
  Carregamento: Salva os dados processados em uma tabela currency em um banco de dados PostgreSQL usando SQLAlchemy.

Configuração Segura: Utiliza um arquivo .env para carregar credenciais (chave da API e URL do banco de dados) de forma segura, sem expô-las no código.

Estrutura:

  O código está contido principalmente no arquivo etlProcedural.py e utiliza as seguintes bibliotecas principais:
  
    requests: Para fazer chamadas HTTP à API.
    
    python-dotenv: Para carregar variáveis de ambiente do arquivo .env.
    
    SQLAlchemy: Para interagir com o banco de dados PostgreSQL (ORM).
    
    psycopg2: Driver PostgreSQL para SQLAlchemy (geralmente instalado como dependência do SQLAlchemy para PostgreSQL).

Configuração:

  Clone o repositório (se aplicável) ou tenha o arquivo etlProcedural.py em um diretório.
  
  Crie e ative um ambiente virtual (recomendado):
  
python -m venv venv

source venv/bin/activate  Linux/macOS

venv\Scripts\activate     Windows

Instale as dependências: Crie um arquivo requirements.txt com o seguinte conteúdo:

  requests, python-dotenv, SQLAlchemy, psycopg2-binary

E instale-as:

pip install -r requirements.txt

Crie o arquivo .env: 

No mesmo diretório do etlProcedural.py, crie um arquivo chamado .env e adicione suas credenciais:

  dotenv
  
  CURRENCY_API_KEY="sua_chave_api_aqui"
  
  DATABASE_KEY="postgresql://usuario:senha@host:porta/nome_banco"

Substitua sua_chave_api_aqui pela sua chave da API freecurrencyapi.com.

Substitua os detalhes da conexão PostgreSQL (usuario, senha, host, porta, nome_banco) pelos seus.

Como Executar:

Após configurar o ambiente e o arquivo .env, execute o script diretamente:

python etlProcedural.py

O script irá:

  Carregar as variáveis de ambiente.

  Configurar a conexão com o banco de dados e criar a tabela currency se ela não existir.

  Chamar a função extract() para buscar os dados da API.

  Chamar a função transform() para processar os dados.

  Chamar a função saveSQL() para salvar os dados no banco.

  Logs básicos serão impressos no console indicando o progresso.
