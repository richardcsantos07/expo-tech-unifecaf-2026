import login
import usuarios
import tarefas
import tipos
import status


def menu_principal():
    while True:
        print("\n========== TaskQuest ==========")
        print("1 - Login")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            login.loginUsuario(email, senha)
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
