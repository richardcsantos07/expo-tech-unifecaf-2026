from conexao import conectar, fechar_conexao;
import status
import tipos
from datetime import datetime

def menu_tarefas(usuario):
    
    while True:
        print("\n========== Tarefas ==========")
        print("Menu de Tarefas:")
        print("1 - Ver Tarefas")
        print("2 - Cadastrar Tarefas")
        print("3 - Atualizar Tarefa")
        print("4 - Concluir Tarefa")
        print("5 - Excluir Tarefa")
        print("0 - Voltar")

        opcao = input("Digite qual opção do menu deseja acessar: ")

        if opcao == "1":
            
            buscarTarefas(usuario)

        elif opcao == "2":

            cadastrarTarefa(usuario)

        elif opcao == "3":

            atualizarTarefa()

        elif opcao == "4":

            concluirTarefa()

        elif opcao == "5":

            excluirTarefa()

        elif opcao == "0":

            break

        else:
            print("Opção inválida")


def buscarTarefas(usuario):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f""" SELECT t.id_tarefa, t.nome_tarefa, t.data_fim, t.xp_recompensa, t.concluida, ti.descricao_tipo, s.descricao_status 
        FROM tarefas t
        INNER JOIN tipos ti ON ti.id_tipo = t.id_tipo
        INNER JOIN status s ON s.id_status = t.id_status 
        WHERE t.id_usuario = {usuario}
               """
        cursor.execute(sql)

        tipos = cursor.fetchall()

        if not tipos:

            print("Você não possui tarefas cadastradas. Cadastre seu primeira tarefa!")
            formCadastrarTarefa(usuario)

        else:
            print("\n========== Tarefas ==========")
            for tipo in tipos:
                print(f"ID: {tipo[0]} | Descrição: {tipo[1]}")

            cursor.close
            fechar_conexao(conexao)

def cadastrarTarefa(usuario, nome, descricao, dataInicio, dataFim, xp, coins, tipo, estado):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = """
INSERT INTO tarefas(
    nome_tarefa,
    descricao_tarefa,
    data_inicio,
    data_fim,
    xp_recompensa,
    coins_recompensa,
    id_tipo,
    id_status,
    id_usuario
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
        valores = (
            nome,
            descricao,
            dataInicio,
            dataFim,
            xp,
            coins,
            tipo,
            estado,
            usuario
        )

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

        buscarTarefas(usuario)

def formCadastrarTarefa(usuario):
    print("\n========== Formulário de Cadastro ==========")
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    dataInicio = input("Digite a data de inicio: ")
    dataIConvertida = datetime.strptime(dataInicio, "%Y-%m-%d").date()
    dataFim = input("Digite a data de fim: ")
    dataFConvertida = datetime.strptime(dataFim, "%Y-%m-%d").date()
    xp = int(input("Digite o xp de recompensa: "))
    coins = int(input("Digite a recompensa em coins: "))
    tipos.buscarTipos(usuario)
    tipo = int(input("Escolha o tipo da tarefa: "))
    status.buscarStatus(usuario)
    estado = int(input("Escolha o status da tarefa: "))

    cadastrarTarefa(nome, descricao, dataIConvertida, dataFConvertida, xp, coins, tipo, estado, usuario)


    

def atualizarTarefa():

    return

def concluirTarefa():

    return

def excluirTarefa():

    return
    



    