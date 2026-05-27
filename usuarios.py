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