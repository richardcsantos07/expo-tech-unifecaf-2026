import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password='root',
    database='dbtaskquest'
)

cursor = conexao.cursor()

def buscaPessoas():
    sql = 'SELECT * FROM tbl_pessoas'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return print(resultado)

def buscaPessoaById(id):
    sql = f'SELECT * FROM tbl_pessoas WHERE id_pessoa = {id}'
    cursor.execute(sql)
    resultado = cursor.fetchone()
    if resultado == None:
        return print("Nenhuma pessoa encontrada com esse id")
    else:
        return print(resultado)


def cadastraPessoa(nome, idade):
  
    sql = f'INSERT INTO tbl_pessoas (nome_pessoa, idade) VALUES ("{nome}", {idade})'
    cursor.execute(sql)
    conexao.commit()
    buscaPessoas()

nome = input("Digite o nome da pessoa que deseja cadastrar: ")
idade = int(input("Digite a idade da pessoa: "))
cadastraPessoa(nome, idade)

def atualizaNomePessoa(id, nome):
    sql = f'UPDATE tbl_pessoas SET nome_pessoa = "{nome}" WHERE id_pessoa = {id}'
    cursor.execute(sql)
    conexao.commit()
    buscaPessoas()

# buscaPessoas()
# id = int(input("Digite o id da pessoa na que deseja atualizar o nome: "))
# nome = input("Digite o novo nome: ")
# atualizaNomePessoa(id, nome)

def deletaPessoa(id):
    sql = f'DELETE FROM tbl_pessoas WHERE id_pessoa = {id}'
    cursor.execute(sql)
    conexao.commit()
    buscaPessoas()

# buscaPessoas()
# id = int(input("Digite o id da pessoa que deseja excluir: "))
# deletaPessoa(id)

# buscaPessoas()

conexao.close()
cursor.close()