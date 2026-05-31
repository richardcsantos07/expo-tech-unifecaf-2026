from conexao import conectar, fechar_conexao;

def perfil_usuario(usuario):
    conexao = conectar()

    if conexao: 
        cursor = conexao.cursor()
        sql = f"SELECT * FROM usuarios WHERE id_usuario = {usuario}"
        cursor.execute(sql)

        usuario = cursor.fetchone()

        print("\n========== Perfil ==========")
        print(f"Olá {usuario[1]}")
        print(f"DATA NASCIMENTO: {usuario[2]}")
        print(f"TELEFONE: {usuario[3]}")
        print(f"XP: {usuario[5]}")
        print(f"COINS: {usuario[6]}")

def menu_usuarios():
    conexao = conectar()


    if conexao:
        cursor = conexao.cursor()
        sql = """SELECT u.id_usuario, u.nome_usuario, u.data_nasc, u.telefone, l.email 
                 FROM usuarios u
                 INNER JOIN login l ON l.id_usuario = u.id_usuario
        """
        cursor.execute(sql)

        usuarios = cursor.fetchall()

        cursor.close()
        fechar_conexao(conexao)

        print("\n========== Usuarios ==========")
        for usuario in usuarios:
            print(f"ID: {usuario[0]} | NOME: {usuario[1]} |DATA DE NASCIMENTO: {usuario[2]} | TEL: {usuario[3]} | EMAIL: {usuario[4]}")