from operations import depositar, sacar, extrato

def main():
    while True:
        print("\n### Bem vindo ao Bem Vindo Bank ###\n")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            valor = float(input("\nQuanto você quer depositar? "))
            depositar(valor)
        elif opcao =="2":
            valor = float(input("\nQuanto você quer sacar? "))
            sacar(valor)        
        elif opcao =="3":
            extrato()
        elif opcao =="4":
            print("Saindo...")
            break
        else:
            print("\nDigite uma opção válida!\nTente novamente.")

if __name__ == "__main__":
    main()             
