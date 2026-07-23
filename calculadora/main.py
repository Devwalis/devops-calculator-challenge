def somar(numero1, numero2):
	return numero1 + numero2


while True:
	print("-" * 30)
	print("               CALCULADORA FAP"
	print("=" * 30)
	print("1 - Soma")
	print("0 - Sair")
	
	opcao = input("\nEscolha uma opção: ")
	
	
	if opcao == "1":
		numero1 = float(input("Digite o primeiro número: "))
		numero2 = float(input("Digite o segundo  número: "))
		
		resultado = somar(numero, numero2)
	
		print(f"\nResultado: {resultado}")


	elif opcao == "0":
		print("\nEncerrando a calculadora...")
	
	else:
		print("\nOpção inválida!")

	continuar = input("\nDeseja realizar outra operação? (S/N):   ".upper()


	if continuar != "S":
		print("\nObrigado por utilizar a calculadora")
		break

