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
        self.__comprimento_mm = comprimento_mm
        self.__largura_mm = largura_mm

    def get_comprimento(self):
        return self.__comprimento_mm

    def set_comprimento(self, comprimento):
        self.__comprimento_mm = comprimento

    def get_largura(self):
        return self.__largura_mm

    def set_largura(self, largura):
        self.__largura_mm = largura

    def area_unitaria_em_metro_quadrado(self):
        return (self.__comprimento_mm * self.__largura_mm) / 1000000

    def area_total_no_estoque(self):
        return self.area_unitaria_em_metro_quadrado() * self.get_quantidade_unitaria()

    def mostrar(self):
        print(f"Codigo(id): {self.get_id()}")
        print(f"Nome: {self.get_nome()}")
        print(f"Dimensão(Comprimento x Largura): {self.__comprimento_mm}mm x {self.__largura_mm}mm")
        print(f"Quantidade unitária disponível no estoque: {self.get_quantidade_unitaria()}")
        print(f"Quantidade total em estoque em m²: {self.area_total_no_estoque():.2f}m²")

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def acessar_menu_de_estoque(self, estoque):
        while True:

            print(f"\n==================== Menu ({self.nome}) ==============================")

            if not isinstance(self, Operador):# --- é usado isinstance para mostrar as opcoes 1 - 5 apenas se N for o operador 
                print("1 - Cadastrar um novo piso no estoque")
                print("2 - Procure pisos em estoque")
                print("3 - Listar todos os pisos em estoque")
                print("4 - Atualizar piso em estoque (apenas correção)")
                print("5 - Deletar pisos em estoque")
                
            print("6 - Registrar SAIDA de piso do estoque") # --- qualquer um ve
            print("7 - Registrar ENTRADA de piso do estoque")
            print("8 - Sair do menu")

            opcao = input_int("\nEscolha a opção: ")

            # --- mesmo q o operador digite 1 - 5 no menu vai ser bloqueado
            # --- pq o python reconhece q é uma instancia de operador
            if isinstance(self, Operador) and opcao in [1, 2, 3, 4, 5]:
                print("\nAcesso negado! Seu cargo não tem permissão para esta ação.")
                continue

            if opcao == 1: # --- cadastrar ---------
                while True:
                    nome = input("\nDigite o nome: ")
                    quantidade_unitaria = input_int("Digite a quantidade em unidades: ")
                    comprimento_mm = input_int("Digite o comprimento em milímetros: ")
                    largura_mm = input_int("Digite a largura em milímetros: ")

                    piso = Piso(nome, quantidade_unitaria, comprimento_mm, largura_mm)
                    estoque.append(piso)
                    print("Produto Cadastrado!")

                    if not continuar_na_operacao("\nContinuar cadastrando?(s/n): "):
                        break

            elif opcao == 2: # --- procurar ---------
                while True:
                    piso = buscar_piso(estoque, "\nColoque o código do piso a ser procurado: ")
                    if piso:
                        piso.mostrar()

                    if not continuar_na_operacao("\nContinuar procurando piso?(s/n): "):
                        break

            elif opcao == 3: # --- listar ---------
                if not estoque:
                    print("\nNenhum piso cadastrado no estoque.")
                else:
                    print(f"\n{len(estoque)} piso(s) encontrado(s) no estoque:\n")
                    for piso in estoque:
                        print("--------------------------------------------------------")
                        piso.mostrar()
                    print("========================================================")

            elif opcao == 4: # --- atualizar ---------
                while True:
                    piso = buscar_piso(estoque, "\nColoque o código do piso a ser atualizado: ")
                    if piso:
                        print("\nPiso encontrado:")
                        piso.mostrar()

                        print("\nO que deseja corrigir?")
                        print("1 - Nome")
                        print("2 - Comprimento")
                        print("3 - Largura")
                        campo = input_int("\nEscolha o campo: ")

                        if campo == 1:
                            piso.set_nome(input("Novo nome: "))
                            print("Nome atualizado!")
                        elif campo == 2:
                            piso.set_comprimento(input_int("Novo comprimento em milímetros: "))
                            print("Comprimento atualizado!")
                        elif campo == 3:
                            piso.set_largura(input_int("Nova largura em milímetros: "))
                            print("Largura atualizada!")
                        else:
                            print("Campo inválido.")

                    if not continuar_na_operacao("\nContinuar atualizando?(s/n): "):
                        break

            elif opcao == 5: # --- deletar ---------
                while True:
                    piso = buscar_piso(estoque, "\nColoque o código do piso a ser deletado: ")
                    if piso:
                        print("\nPiso encontrado:")
                        piso.mostrar()

                        confirmacao = input("\nTem certeza que deseja deletar esse piso?(s/n): ")
                        if confirmacao.lower() == "s":
                            estoque.remove(piso)
                            print("Piso deletado com sucesso!")
                        else:
                            print("Operação cancelada.")

                    if not continuar_na_operacao("\nContinuar deletando?(s/n): "):
                        break

            elif opcao == 6: # --- saida do estoque ---------
                while True:
                    piso = buscar_piso(estoque, "\nColoque o código do piso para registrar a saída(em unidades): ")
                    if piso:
                        print(f"\nEstoque atual: {piso.get_quantidade_unitaria()} unidade(s)")
                        quantidade_saida = input_int("Quantidade de saída: ")

                        if quantidade_saida <= piso.get_quantidade_unitaria():
                            piso.set_quantidade_unitaria(piso.get_quantidade_unitaria() - quantidade_saida)
                            print(f"Saída registrada! Novo estoque: {piso.get_quantidade_unitaria()} unidade(s)")
                        else:
                            print(f"Estoque insuficiente. Disponível: {piso.get_quantidade_unitaria()} unidade(s).")

                    if not continuar_na_operacao("\nContinuar registrando saída?(s/n): "):
                        break

            elif opcao == 7: # --- entrada no estoque ---------
                while True:
                    piso = buscar_piso(estoque, "\nColoque o código do piso para registrar a entrada(em unidades): ")
                    if piso:
                        print(f"\nEstoque atual: {piso.get_quantidade_unitaria()} unidade(s)")
                        quantidade_entrada = input_int("Quantidade de entrada: ")
                        
                        piso.set_quantidade_unitaria(piso.get_quantidade_unitaria() + quantidade_entrada)
                        print(f"Entrada registrada! Novo estoque: {piso.get_quantidade_unitaria()} unidade(s)")

                    if not continuar_na_operacao("\nContinuar registrando entrada?(s/n): "):
                        break

            elif opcao == 8:  # --- sair do programa ---------
                print("\nSaindo do menu.")
                break

            else:
                print("\nOpção inválida. Escolha uma opção entre 1 e 8.")

class Administrador(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

class Operador(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)


# --- Funções Auxiliares para o programa 

def input_int(mensagem): # --- assegura que em inputs q pede numero vai receber numero
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

def buscar_piso(estoque, mensagem_id): # --- funcao q busca o piso ou por nome ou id
    print("\nComo deseja buscar?")
    print("1 - Por Código (ID)")
    print("2 - Por Nome")
    tipo_busca = input_int("\nEscolha a opção: ")

    if tipo_busca == 1:
        busca_id = input_int(mensagem_id)
        for piso in estoque:
            if piso.get_id() == busca_id:
                return piso

    elif tipo_busca == 2:
        busca_nome = input("\nDigite o nome do piso: ").strip().lower()
        for piso in estoque:
            if busca_nome in piso.get_nome().lower():
                return piso

    else:
        print("\nOpção de busca inválida.")

    print("\nPiso não foi encontrado.")
    return None

def continuar_na_operacao(mensagem):
    vai_continuar = input(mensagem)
    if vai_continuar.lower() != "s":
        print("========================================================")
        return False
    return True

# --- Criacao manual dos objetos para rodar o programa

estoque = []

""" admin1 = Administrador("Joao (admin)")
admin1.acessar_menu_de_estoque(estoque) """

operador1 = Operador("walter (operador)")
operador1.acessar_menu_de_estoque(estoque)
