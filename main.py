import login
import usuarios
import tarefas
import tipos
import status
import conquistas
import usuarios
import recompensas
import habitos
import sessoes_foco
import classes
import niveis



def menu_login():
    while True:
        print("\n========== TaskQuest ==========")
        print("1 - Login")
        print("2 - Cadastre-se")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            
            idUsuario = login.formularioLogin()

            if not idUsuario:
                menu_admin()
            else:
                menu_principal(idUsuario)

        if opcao == "2":
            
            login.formularioCadastro()
            idUsuario = login.formularioLogin()
            menu_principal(idUsuario)
        
        elif opcao == "0":
            
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opcao invalida. Tente novamente.")

def menu_principal(usuario):
    
    while True:
        print("\n========== Home ==========")
        print("Deseja navegar para qual menu?")
        print("1 - Tarefas")
        print("2 - Conquistas")
        print("3 - Recompensas")
        print("4 - Hábitos")
        print("5 - Sessões de Foco")
        print("6 - Perfil")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            
            tarefas.menu_tarefas(usuario)

        elif opcao == "2":

            conquistas.menu_conquistas(usuario)

        elif opcao == "3":

            recompensas.menu_recompensa(usuario)

        elif opcao == "4":

            habitos.menu_habitos(usuario)

        elif opcao == "5":

            sessoes_foco.menu_sessao(usuario)

        elif opcao == "6":

            usuarios.perfil_usuario(usuario)

        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_admin():
    
    while True:
        print("\n========== ADMIN ==========")
        print("Deseja navegar para qual menu?")
        print("1 - Usuarios")
        print("2 - Conquistas")
        print("3 - Niveís")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            
            usuarios.menu_usuarios()

        elif opcao == "2":

            conquistas.menu_conquistas_admin()

        elif opcao == "3":

            niveis.menu_niveis()

        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_login()
