from conexao import conectar, fechar_conexao;

def menu_conquistas(usuario):

    return

def menu_conquistas_admin():

        while True:
        
            print("\n========== Conquistas ==========")
            print("1 - Ver Conquistas")
            print("2 - Cadastrar Conquista")
            print("3 - Atualizar Conquista")
            print("4 - Excluir Conquista")
            print("0 - Voltar")

            opcao = input("Digite qual opção do menu deseja acessar: ")

            if opcao == "1":
                
                buscarConquistas()

            elif opcao == "2":

                formCadastrarConquista()

            elif opcao == "3":

                formAtualizarConquista()

            elif opcao == "4":

                formExcluirConquista()

            elif opcao == "0":

                break

            else:
                print("Opção inválida")
    
def buscarConquistas():
    
    return

def cadastrarConquista(nome, descricao, tabela, valor):
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()
        sql = f"INSERT INTO conquistas(nome_conquista, descricao_conquista, tabela, valor_requerido) VALUES ('{nome}', '{descricao}', '{tabela}', {valor})"
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        fechar_conexao(conexao)

        buscarConquistas()

def formCadastrarConquista():

    cadastrarConquista()

def atualizarConquista(conquista):

    return

def formAtualizarConquista():

    atualizarConquista(conquista)

def excluirConquista(conquista):

    return

def formExcluirConquista():

    excluirConquista(conquista)