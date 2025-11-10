from conectar import ligar
from criar_db import Cliente 
from criar_db import Vendedor
import mysql.connector
from config import HOST, USUARIO, SENHA

def conectar():
    try:
        con = mysql.connector.connect(
            host=HOST,
            user=USUARIO,
            password=SENHA,
            database="ecommerce_oculos_db"
        )
        return con
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco: {err}")
        return None

def exibir_total_gasto_por_cliente(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM vw_total_gasto_por_cliente")
    resultados = cursor.fetchall()
    print("\n TOTAL GASTO POR CLIENTE")
    print("-" * 45)
    for nome, total in resultados:
        print(f"{nome:<25} | R$ {total:.2f}")
    cursor.close()

def exibir_total_vendido_por_vendedor(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM vw_total_vendido_por_vendedor")
    resultados = cursor.fetchall()
    print("\n TOTAL VENDIDO POR VENDEDOR")
    print("-" * 45)
    for nome, total in resultados:
        print(f"{nome:<25} | R$ {total:.2f}")
    cursor.close()

def exibir_produtos_mais_vendidos(con):
    cursor = con.cursor()
    cursor.execute("SELECT * FROM vw_produtos_mais_vendidos")
    resultados = cursor.fetchall()
    print("\n PRODUTOS MAIS VENDIDOS")
    print("-" * 45)
    for nome, qtd in resultados:
        print(f"{nome:<25} | Quantidade vendida: {int(qtd)}")
    cursor.close()

def consultar_views():
    """Submenu para exibir as views."""
    con = conectar()
    if not con:
        print("Erro ao conectar no banco de dados.")
        return

    while True:
        print("\n=== CONSULTAS (VIEWS) ===")
        print("[1] Total gasto por cliente")
        print("[2] Total vendido por vendedor")
        print("[3] Produtos mais vendidos")
        print("[0] Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_total_gasto_por_cliente(con)
        elif opcao == "2":
            exibir_total_vendido_por_vendedor(con)
        elif opcao == "3":
            exibir_produtos_mais_vendidos(con)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
    con.close()

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
        print("[1] Login")      
        print("[2] Buscar")
        print("[3] Apagar")
        print("[4] Editar")             
        print("[5] Adicionar")             
        print("[6] Consultar")  

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            #logica do login
            print("ok")
        elif opcao == "2":
            #logica buscar
            print("ok")           
        elif opcao == "3":
            #logica apagar 
            print("ok")          
        elif opcao == "4":
            #logica editar
            print("ok")
        elif opcao == "5":
            #logica adicionar
            print("ok")
        elif opcao == "6":
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
        
