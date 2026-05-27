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

            formCadastrarTarefa(usuario)

        elif opcao == "3":

            formAtualizarTarefa(usuario)

        elif opcao == "4":

            concluirTarefa()

        elif opcao == "5":

            formExcluirTarefa(usuario)

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

        tarefas = cursor.fetchall()

        if not tarefas:

            print("Você não possui tarefas cadastradas. Cadastre seu primeira tarefa!")
            formCadastrarTarefa(usuario)

        else:
            print("\n========== Tarefas ==========")
            for tarefa in tarefas:
                print(f"ID: {tarefa[0]} | NOME: {tarefa[1]} | DATA_FIM: {tarefa[2]} | XP: {tarefa[3]} | DONE: {tarefa[4]} | TIPO: {tarefa[5]} | STATUS: {tarefa[6]}")

            cursor.close
            fechar_conexao(conexao)

def buscarTarefa(tarefa):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f""" SELECT t.id_tarefa, t.nome_tarefa, t.data_fim, t.xp_recompensa, t.concluida, ti.descricao_tipo, s.descricao_status 
        FROM tarefas t
        INNER JOIN tipos ti ON ti.id_tipo = t.id_tipo
        INNER JOIN status s ON s.id_status = t.id_status 
        WHERE t.id_tarefa = {tarefa}
               """
        cursor.execute(sql)

        tarefas = cursor.fetchone()

        if not tarefas:

            print("Tarefa não encontrada!")

        else:
            print("\n========== Tarefa ==========")
            
            print(f"ID: {tarefas[0]} | NOME: {tarefas[1]} | DATA_FIM: {tarefas[2]} | XP: {tarefas[3]} | DONE: {tarefas[4]} | TIPO: {tarefas[5]} | STATUS: {tarefas[6]}")

            cursor.close
            fechar_conexao(conexao)

def cadastrarTarefa(nome, descricao, dataInicio, dataFim, xp, coins, tipo, estado, usuario):
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


    

def atualizarTarefa(usuario, tarefa, status):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"UPDATE tarefas SET id_status = {status} WHERE id_tarefa = {tarefa}"
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

        buscarTarefa(tarefa)

def formAtualizarTarefa(usuario):
    print("\n========== Formulário de Atualização ==========")
    tarefa = int(input("Escolha a tarefa que deseja atualizar: "))
    status.buscarStatus(usuario)
    estado = int(input("Escolha o status da tarefa: "))

    atualizarTarefa(usuario, tarefa, estado)

    

def concluirTarefa():

    return

def excluirTarefa(usuario, tarefa):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"DELETE FROM tarefas WHERE id_tarefa = {tarefa}"
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

        buscarTarefas(usuario)

def formExcluirTarefa(usuario):
    print("\n========== Formulário de Exclusão ==========")
    tarefa = int(input("Escolha a tarefa que deseja excluir: "))

    excluirTarefa(usuario, tarefa)
    



    