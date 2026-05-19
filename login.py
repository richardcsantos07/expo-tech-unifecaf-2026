from conexao import conectar, fechar_conexao;

def loginUsuario(email, senha):
    conexao = conectar()

    if conexao:

        cursor = conexao.cursor()
        sql = f'SELECT u.nome_usuario FROM login L INNER JOIN usuarios U ON U.id_usuario = L.id_usuario WHERE email = "{email}" AND senha = "{senha}"'
        cursor.execute(sql)

        usuario = cursor.fetchone()

        return print(f'Bem vindo! {usuario[0]}')
