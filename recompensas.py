from conexao import conectar, fechar_conexao;

def menu_recompensa(usuario):
    
    while True:
        print("\n========== Hábitos ==========")
        print("Menu de Hábitos:")
        print("1 - Ver Recompensas")
        print("2 - Cadastrar Recompensa")
        print("3 - Reesgatar Recompensa")
        print("0 - Voltar")

        opcao = input("Digite qual opção do menu deseja acessar: ")

        if opcao == "1":
            buscarRecompensas(usuario)

        elif opcao == "2":
            formCadastrarRecompensa(usuario)

        elif opcao == "3":
            recompensa = int(input("Qual a recompensa a ser resgatada: "))
            resgatarRecompensa(usuario, recompensa)

        elif opcao == "0":
            break

        else:
            print("Opção inválida")

def buscarRecompensas(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"SELECT * FROM recompensas WHERE id_usuario = {usuario}"
        cursor.execute(sql)

        recompensas = cursor.fetchall()

        if not recompensas:

            print("Você não possui recompensas cadastradas!")

        else:
            print("\n========== Recompensa ==========")

            for recompensa in recompensas:
                print(f"ID: {recompensa[0]} | NOME: {recompensa[1]} | DESCRICAO: {recompensa[2]} | VALOR: {recompensa[3]} | RESGATADO: {recompensa[4]}")

            cursor.close
            fechar_conexao(conexao)


def cadastrarRecompensa(usuario, nome, descricao, valor):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"INSERT INTO recompensas(nome_recompensa, descricao_recompensa, valor_recompensa, id_usuario) VALUES ('{nome}', '{descricao}', {valor}, {usuario})"
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

        buscarRecompensas(usuario)

def formCadastrarRecompensa(usuario):
    print("\n========== Formulário de Cadastro ==========")
    nome = input("Digite o nome da recompensa: ")
    descricao = input("Digite a descrição da recompensa: ")
    valor = int(input("Digite quanto a recompensa vai custar: "))

    cadastrarRecompensa(usuario, nome, descricao, valor)

def resgatarRecompensa(usuario, recompensa):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sqlConsulta = f"SELECT coins_total FROM usuarios WHERE id_usuario = {usuario}"
        cursor.execute(sqlConsulta)
        coinsUsuario = cursor.fetchone()[0]

        sqlConsulta = f"SELECT valor_recompensa FROM recompensas WHERE id_recompensa = {recompensa}"
        cursor.execute(sqlConsulta)
        coinsRecompensa = cursor.fetchone()[0]

        if coinsRecompensa > coinsUsuario:
            print("Você é pobre e não possui o necessário para resgatar a recompensa")
        else:
            sqlGasto = f"UPDATE usuarios SET coins_total = coins_total - {coinsRecompensa} WHERE id_usuario = {usuario}"
            cursor.execute(sqlGasto)
            conexao.commit()

            sqlResgate = f"UPDATE recompensas SET resgatado = TRUE WHERE id_recompensa = {recompensa}"
            cursor.execute(sqlResgate)
            conexao.commit()

            print("Recompensa resgatada")
            buscarRecompensas(usuario)

            cursor.close()
            fechar_conexao(conexao)  