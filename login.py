from conexao import conectar, fechar_conexao;
from datetime import datetime;
import sequencias

def loginUsuario(email, senha):
    conexao = conectar()

    if conexao:

        cursor = conexao.cursor()
        sql = f'SELECT u.nome_usuario, u.id_usuario FROM login L INNER JOIN usuarios U ON U.id_usuario = L.id_usuario WHERE email = "{email}" AND senha = "{senha}"'
        cursor.execute(sql)

        usuario = cursor.fetchone()

        sequencia = sequencias.buscarSequencia(usuario[1])

        if not sequencia:
            sequencias.cadastrarSequencia(usuario[1])
        else:
            sequencias.atualizarSequencia(usuario[1])
        
        cursor.close()
        fechar_conexao(conexao)
        
        return usuario
    
def formularioLogin():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    if email == "admin@admin.com" and senha == "admin123":
        return None
    else:
        usuario = loginUsuario(email, senha)
    

    return usuario[1]

def cadastroUsuario(nome, email, senha, dataNasc, telefone):
    conexao = conectar()


    if conexao:
        cursor = conexao.cursor()
        sql = f"INSERT INTO usuarios(nome_usuario, data_nasc, telefone) VALUES ('{nome}', '{dataNasc}', '{telefone}')"
        cursor.execute(sql)
        conexao.commit()

        sqlUsuario = f"SELECT * FROM usuarios ORDER BY id_usuario DESC LIMIT 1"
        cursor.execute(sqlUsuario)
        usuario = cursor.fetchone()

        sql = f"INSERT INTO login(email, senha, id_usuario) VALUES ('{email}', '{senha}', '{usuario[0]}')"
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

        return usuario[0]




def formularioCadastro():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu telefone: ")
    dataNasc = input("Digite sua data de nascimento: ")
    dataConvertida = datetime.strptime(dataNasc, "%Y-%m-%d").date()
    senha = input("Digite sua senha: ")

    
    usuario = cadastroUsuario(nome, email, senha, dataConvertida, telefone)
   
    return usuario
    

def validarTelefone(telefone):
    if not re.match(r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', telefone):
        print("Telefone inválido! Use o formato: (11) 99999-9999")
        return False
    return True
