from conexao import conectar, fechar_conexao
import status
import tarefas
import tipos
from datetime import datetime


def menu_habitos(usuario):

    while True:
        print("\n========== Hábitos ==========")
        print("Menu de Hábitos:")
        print("1 - Ver Hábitos")
        print("2 - Cadastrar Hábito")
        print("0 - Voltar")

        opcao = input("Digite qual opção do menu deseja acessar: ")

        if opcao == "1":
            buscarHabitos(usuario)

        elif opcao == "2":
            formCadastrarHabito(usuario)

        # elif opcao == "3":
        #     atualizarHabito()

        elif opcao == "0":
            break

        else:
            print("Opção inválida")


def buscarHabitos(usuario):                        
    conexao = conectar()

    if conexao:                                    
        cursor = conexao.cursor()
        sql = f"""
            SELECT h.id_habito, h.nome_habito, h.descricao_habito, h.numero_dias_consistencia
            FROM habitos h
            WHERE h.id_usuario = {usuario}
        """
        cursor.execute(sql)

        habitos = cursor.fetchall()

        if not habitos:
            print("Você não possui hábitos cadastrados. Cadastre seu primeiro hábito!")
            formCadastrarHabito(usuario)

        else:
            print("\n========== Seus Hábitos ==========")
            for habito in habitos:
                print(
                    f"ID: {habito[0]} | Nome: {habito[1]} | "
                    f"Frequência: {habito[3]}"
                )
                if habito[2]:
                    print(f"   Descrição: {habito[2]}")

        cursor.close()
        fechar_conexao(conexao)


def cadastrarHabito(usuario, nome, descricao):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = """
            INSERT INTO habitos(
                nome_habito,
                descricao_habito,
                id_usuario
            )
            VALUES (%s, %s, %s)
        """
        valores = (nome, descricao, usuario)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

        print("Hábito cadastrado com sucesso!")
        buscarHabitos(usuario)


def formCadastrarHabito(usuario):
    print("\n========== Formulário de Cadastro ==========")
    nome = input("Digite o nome do hábito: ")
    descricao = input("Digite a descrição do hábito (ou Enter para pular): ")
    cadastrarHabito(usuario, nome, descricao)
    