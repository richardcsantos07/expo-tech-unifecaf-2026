from conexao import conectar, fechar_conexao;

def buscarTipos(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"SELECT * FROM tipos WHERE id_usuario = {usuario}"
        cursor.execute(sql)

        tipos = cursor.fetchall()

        if not tipos:
            descricao = ''
            print("Você não possui tipos cadastrados. Cadastre seu primeiro tipo!")
            cadastrarTipos(usuario, descricao)
        else:
            print("\n========== Tipos ==========")
            for tipo in tipos:
                print(f"ID: {tipo[0]} | Descrição: {tipo[1]}")

            cursor.close
            fechar_conexao(conexao)
    

def cadastrarTipos(usuario, descricao):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"INSERT INTO tipos(descricao_tipo, id_usuario) VALUES ('{descricao}', {usuario})"
        cursor.execute(sql)
        conexao.commit()

        buscarTipos(usuario)

    