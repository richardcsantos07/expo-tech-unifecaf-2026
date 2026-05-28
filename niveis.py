from conexao import conectar, fechar_conexao


def buscarNivel(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"SELECT * FROM niveis WHERE id_usuario = {usuario}"
        cursor.execute(sql)

        nivel = cursor.fetchone()

        cursor.close()
        fechar_conexao(conexao)

        return nivel

def calcularNivel(xp):
    if xp < 100:
        return 1, "Aprediz"
    elif xp < 300:
        return 2, "Genin"
    elif xp < 600:
        return 3, "Chunnin"
    elif xp < 1000:
        return 4, "Jounin"
    elif xp < 1500:
        return 5, "anbu"
    else:
        return 6, "Ninja mestre"

def atualizarNivel(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        sqlXp = f"SELECT xp_total FROM usuarios WHERE id_usuario = {usuario}"
        cursor.execute(sqlXp)
        xpUsuario = cursor.fetchone()[0]

        numeroNivel, nomeNivel = calcularNivel(xpUsuario)

        sqlVerifica = f"SELECT * FROM niveis WHERE id_usuario = {usuario}"
        cursor.execute(sqlVerifica)
        nivelAtual = cursor.fetchone()

        if not nivelAtual:
            sql = f"INSERT INTO niveis(numero_nivel, nome_nivel, id_usuario) VALUES ({numeroNivel}, '{nomeNivel}', {usuario})"
        else:
            sql = f"UPDATE niveis SET numero_nivel = {numeroNivel}, nome_nivel = '{nomeNivel}' WHERE id_usuario = {usuario}"

        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

        return numeroNivel, nomeNivel

def MostrarNivel(usuario):
    nivel = MostrarNivel(usuario)

    if not nivel:
        print("Nivel não encontrado!")
        return

    print("\n========== Nivel ==========")
    print(f"ID: {nivel[0]} | NIVEL: {nivel[1]} | NOME: {nivel[2]}")

def menu_niveis(usuario):
    while True:
        print("\n========== Niveis ==========")
        print("Menu de Niveis:")
        print("1 - Ver meu nivel")
        print("2 - Atualizar nivel")
        print("0 - Voltar")

        opcao = input("Digite qual opção do menu deseja acessar: ")

        if opcao == "1":
            MostrarNivel(usuario)

        elif opcao == "2":
            numeroNivel, nomeNivel = atualizarNivel(usuario)
            print(f"Nivel atualizado! Voce agora e nivel {numeroNivel} - {nomeNivel}")

        elif opcao == "0":
            break

        else:
            print("Opção inválida")