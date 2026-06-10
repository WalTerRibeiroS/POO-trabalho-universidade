class Estoque:

    __proximo_id = 1

    def __init__(self, nome, quantidade_unitaria):

        self.__id = Estoque.__proximo_id
        Estoque.__proximo_id += 1

        self.__nome = nome
        self.__quantidade_unitaria = quantidade_unitaria

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome
    
    def get_quantidade_unitaria(self):
        return self.__quantidade_unitaria
    
    def set_quantidade_unitaria(self, quantidade):
        self.__quantidade_unitaria = quantidade

    def set_nome(self, nome):
        self.__nome = nome

class Piso(Estoque):

    def __init__(self, nome, quantidade_unitaria, comprimento_mm, largura_mm):
        super().__init__(nome, quantidade_unitaria)
        self.comprimento_mm = comprimento_mm
        self.largura_mm = largura_mm

    def area_unitaria_em_metro_quadrado(self):
        return (self.comprimento_mm * self.largura_mm) / 1000000

    def area_total_no_estoque(self):
        return self.area_unitaria_em_metro_quadrado() * self.get_quantidade_unitaria()

    def mostrar(self):
        print(f"Codigo(id): {self.get_id()}")
        print(f"Nome: {self.get_nome()}")
        print(f"Dimensão(Comprimento x Largura): {self.comprimento_mm}mm x {self.largura_mm}mm")
        print(f"Quantidade unitária disponível no estoque: {self.get_quantidade_unitaria()}")
        print(f"Quantidade total em estoque em m²: {self.area_total_no_estoque():.2f}m²")


estoque = []

while True:
    print("\n\n==================== Menu ==============================")
    print("\n1 - Cadastrar um novo piso no estoque")
    print("2 - Procure pisos em estoque")
    print("3 - Listar todos os pisos em estoque")
    print("4 - Atualizar piso em estoque (apenas correção)")
    print("5 - Deletar pisos em estoque")
    print("6 - Registrar SAIDA de piso do estoque")
    print("7 - Registrar ENTRADA de piso do estoque")
    print("8 - Sair do menu")

    opcao = int(input("\nEscolha a opção: "))

    if opcao == 1:

        while True:
            nome = input("\nDigite o nome: ")
            quantidade_unitaria = int(input("Digite a quantidade em unidades: "))
            comprimento_mm = int(input("Digite o comprimento em milímetros: "))
            largura_mm = int(input("Digite a largura em milímetros: "))

            piso = Piso(nome, quantidade_unitaria, comprimento_mm, largura_mm)
            estoque.append(piso)

            print("Produto Cadastrado!")

            vai_continuar = input("\nContinuar cadastrando?(s/n): ")
            if vai_continuar.lower() != "s":
                print("========================================================")
                break

    elif opcao == 2:

        while True:
            busca = int(input("\nColoque o código do piso a ser procurado: "))
            encontrado = False

            for piso in estoque:
                if piso.get_id() == busca:
                    piso.mostrar()
                    encontrado = True
                    break

            if not encontrado:
                print("\nPiso com esse código não pode ser encontrado, tente outro código.")

            vai_continuar = input("\nContinuar procurando piso?(s/n): ")
            if vai_continuar.lower() != "s":
                print("========================================================")
                break

    elif opcao == 3:

        if not estoque:
            print("\nNenhum piso cadastrado no estoque.")
        else:
            print(f"\n{len(estoque)} piso(s) encontrado(s) no estoque:\n")
            for piso in estoque:
                print("--------------------------------------------------------")
                piso.mostrar()
            print("========================================================")

    elif opcao == 4:

        while True:
            busca = int(input("\nColoque o código do piso a ser atualizado: "))
            encontrado = False

            for piso in estoque:
                if piso.get_id() == busca:
                    encontrado = True
                    print("\nPiso encontrado:")
                    piso.mostrar()

                    print("\nO que deseja corrigir?")
                    print("1 - Nome")
                    print("2 - Comprimento")
                    print("3 - Largura")

                    campo = int(input("\nEscolha o campo: "))

                    if campo == 1:
                        novo_nome = input("Novo nome: ")
                        piso.set_nome(novo_nome)
                        print("Nome atualizado!")

                    elif campo == 2:
                        novo_comprimento = int(input("Novo comprimento em milímetros: "))
                        piso.comprimento_mm = novo_comprimento
                        print("Comprimento atualizado!")

                    elif campo == 3:
                        nova_largura = int(input("Nova largura em milímetros: "))
                        piso.largura_mm = nova_largura
                        print("Largura atualizada!")

                    else:
                        print("Campo inválido.")

                    break

            if not encontrado:
                print("\nPiso com esse código não pode ser encontrado, tente outro código.")

            vai_continuar = input("\nContinuar atualizando?(s/n): ")
            if vai_continuar.lower() != "s":
                print("========================================================")
                break

    elif opcao == 5:

        while True:
            busca = int(input("\nColoque o código do piso a ser deletado: "))
            encontrado = False

            for piso in estoque:
                if piso.get_id() == busca:
                    encontrado = True
                    print("\nPiso encontrado:")
                    piso.mostrar()

                    confirmacao = input("\nTem certeza que deseja deletar esse piso?(s/n): ")
                    if confirmacao.lower() == "s":
                        estoque.remove(piso)
                        print("Piso deletado com sucesso!")
                    else:
                        print("Operação cancelada.")
                    break

            if not encontrado:
                print("\nPiso com esse código não pode ser encontrado, tente outro código.")

            vai_continuar = input("\nContinuar deletando?(s/n): ")
            if vai_continuar.lower() != "s":
                print("========================================================")
                break

    elif opcao == 6:

        while True:
            busca = int(input("\nColoque o código do piso para registrar a saída(em unidades): "))
            encontrado = False

            for piso in estoque:
                if piso.get_id() == busca:
                    encontrado = True
                    print(f"\nEstoque atual: {piso.get_quantidade_unitaria()} unidade(s)")

                    quantidade_saida = int(input("Quantidade de saída: "))

                    if quantidade_saida <= piso.get_quantidade_unitaria():
                        piso.set_quantidade_unitaria(piso.get_quantidade_unitaria() - quantidade_saida)
                        print(f"Saída registrada! Novo estoque: {piso.get_quantidade_unitaria()} unidade(s)")
                    else:
                        print(f"Estoque insuficiente. Disponível: {piso.get_quantidade_unitaria()} unidade(s).")
                    break

            if not encontrado:
                print("\nPiso com esse código não pode ser encontrado, tente outro código.")

            vai_continuar = input("\nContinuar registrando saída?(s/n): ")
            if vai_continuar.lower() != "s":
                print("========================================================")
                break

    elif opcao == 7:

        while True:
            busca = int(input("\nColoque o código do piso para registrar a entrada(em unidades): "))
            encontrado = False

            for piso in estoque:
                if piso.get_id() == busca:
                    encontrado = True
                    print(f"\nEstoque atual: {piso.get_quantidade_unitaria()} unidade(s)")

                    quantidade_entrada = int(input("Quantidade de entrada: "))
                    piso.set_quantidade_unitaria(piso.get_quantidade_unitaria() + quantidade_entrada)
                    print(f"Entrada registrada! Novo estoque: {piso.get_quantidade_unitaria()} unidade(s)")
                    break

            if not encontrado:
                print("\nPiso com esse código não pode ser encontrado, tente outro código.")

            vai_continuar = input("\nContinuar registrando entrada?(s/n): ")
            if vai_continuar.lower() != "s":
                print("========================================================")
                break

    elif opcao == 8:
        print("\nSaindo do menu.")
        break

    else:
        print("\nOpção inválida. Escolha uma opção entre 1 e 8.")