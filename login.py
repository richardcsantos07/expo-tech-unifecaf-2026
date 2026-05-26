from conexao import conectar, fechar_conexao;

def loginUsuario(email, senha):
    conexao = conectar()

    if conexao:

        cursor = conexao.cursor()
        sql = f'SELECT u.nome_usuario, u.id_usuario FROM login L INNER JOIN usuarios U ON U.id_usuario = L.id_usuario WHERE email = "{email}" AND senha = "{senha}"'
        cursor.execute(sql)

        usuario = cursor.fetchone()
        
        cursor.close()
        fechar_conexao(conexao)
        
        return usuario
    
def formularioLogin():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = loginUsuario(email, senha)
    
    print(f'Bem vindo! {usuario[0]}')

    return usuario[1]


