from conectar import ligar
from criar_db import Cliente 
from criar_db import Vendedor

def menu_cliente(id_cliente):
    usuario = Cliente(id_cliente)

    while True:
        print("\n === MENU CLIENTE ===")
        print("[1] Cadastrar")
        print("[2] Login")
        print("[3] Compras")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            #lógica de cadastro
            print("Ok")
        elif opcao == "2":
            #logica de login
            print("ok")
        elif opcao == "3":
            #logica de compras
            print("ok") 
        else:
            print("Opção inválida")    

def menu_vendedor(id_vendedor):
    vendedor = Vendedor(id_vendedor)

    while True:
        print("\n === MENU VENDEDOR ===")
        print("[1] Login")
        print("[2] Consulta")
        print("[3] Adicionar produto")

        opcao = input("Esculha uma opção:")
        if opcao == "1":
            #logica de login
            print("ok")
        elif opcao == "2":
            #logica de consulta
            print("Ok")
        elif opcao == "3":
            #logica de adicionar produto
            print("ok")
        else:
            print("Opção inválida")   

def menu_gerente(id_vendedor):
    gerente = Vendedor(id_vendedor)
    
    while True:
        print("\n=== MENU GERENTE ===")
        print("[1] Buscar")
        print("[2] Apagar")
        print("[3] Editar")

        opcao = input("Esculha uma opção:")
        if opcao == "1":
            #logica de busca
            print("ok")
        elif opcao == "2":
            #logica de apagar
            print("Ok")
        elif opcao == "3":
            #logica de editar
            print("ok")
        else:
            print("Opção inválida")  

def menu_adm(id_vendedor):
    adm = Vendedor(id_vendedor)

    while True:
        print("\n === MENU ADMINISTRADOR ===")
        print("[1] Buscar")
        print("[2] Apagar")
        print("[3] Editar")             
        print("[4] Adicionar")             
        print("[5] Consultar")  

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            #logica buscar
            print("ok")           
        elif opcao == "2":
            #logica apagar 
            print("ok")          
        elif opcao == "3":
            #logica editar
            print("ok")
        elif opcao == "4":
            #logica adicionar
            print("ok")
        elif opcao == "5":
            #logica consultar
            print("ok")
        else:         
            print("Opção inválida")

def main():
    while True:
        print("\n=== MENU ===")
        print("[1] Cliente")
        print("[2] Vendedor")
        print("[3] Gerente")
        print("[4] Administrador")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_cliente()
        elif opcao == "2":           
            menu_vendedor()
        elif opcao == "3":           
            menu_gerente()
        elif opcao == "4":           
            menu_adm()
        else:
            print("Opção inválida")           
        
