from conexao import conectar, fechar_conexao;

def buscarStatus(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"SELECT * FROM status WHERE id_usuario = {usuario}"
        cursor.execute(sql)

        status = cursor.fetchall()

        if not status:
            descricao = ''
            print("Você não possui status cadastrados. Cadastre seu primeiro status!")
            cadastrarStatus(usuario, descricao)
        else:
            print("\n========== Status ==========")
            for statu in status:
                print(f"ID: {statu[0]} | Descrição: {statu[1]}")

            cursor.close
            fechar_conexao(conexao)
    

def cadastrarStatus(usuario, descricao):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"INSERT INTO status(descricao_status, id_usuario) VALUES ('{descricao}', {usuario})"
        cursor.execute(sql)
        conexao.commit()

        buscarStatus(usuario)

    