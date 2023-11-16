import mysql.connector


conexao = mysql.connector.connect(
   host='localhost',
   user='root',
   password='98787589',
   database='academia',
)
cursor = conexao.cursor()
Nome = input("DIGITE O NOME DO ALUNO: ")
cpf = input ("DIGITE O CPF DO ALUNO: ")
endereco = input ("DIGITE O ENDEREÇO: ")
telefone = input ("DIGITE O TELEFONE: ")
comando = f'INSERT INTO alunos (Nome,cpf,endereço,telefone) VALUES ("{Nome}","{cpf}","{endereco}","{telefone}") '
cursor.execute(comando)
conexao.commit()

