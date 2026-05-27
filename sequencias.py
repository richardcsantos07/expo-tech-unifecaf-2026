from conexao import conectar, fechar_conexao;

def cadastrarSequencia(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"INSERT INTO sequencias (numero_sequencia, id_usuario) VALUES (1, {usuario})"
        cursor.execute(sql)
        conexao.commit()

        cursor.close
        fechar_conexao(conexao)

def atualizarSequencia(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"UPDATE sequencias SET numero_sequencia = numero_sequencia + 1 WHERE id_usuario = {usuario}"
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

def buscarSequencia(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"SELECT numero_sequencia FROM sequencias WHERE id_usuario = {usuario}"
        cursor.execute(sql)
        
        sequencia = cursor.fetchone()

        return sequencia