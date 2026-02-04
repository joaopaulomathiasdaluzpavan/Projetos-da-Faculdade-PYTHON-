print("Bem vindo à R.M! ")

def final_value():
    valor_total_locacao()
    global valor_total
    valor_total = (valor + apontamento1_adi + apontamento2_adi + apontamento3_comp)

def valor_total_locacao():
    global valor_contrato
    valor_contrato = 2000

def parcelamento():
    try: 
        global parcela
        parcela = int(input("Gostaria de dividir o valor em quantas parcelas?: "))
        valor_total_locacao()
    
        while True: 
            if 1 <= parcela <=5:
                global valor_parcelado
                global parcela_valor
                parcela_valor = parcela
                valor_parcelado = round((valor_contrato / parcela),2)
                break
            elif parcela > 5 or parcela < 1: 
                print(f"A quantidade de {parcela} parcelas não se encontra no intervalo compreendido!")
                print("Retornando para Parcelamentos!....")
                parcelamento()
    except ValueError: 
        print("\nO valor informado de parcelas não se enquadra no intervalo! Por favor insira o valor novamente! ....")
        parcelamento()

    print(f"Você optou por dividir o valor do contrato em {parcela} vez(es). Desse modo ficará {parcela} parcela(as) de {valor_parcelado}!")

def retorno():
    print("Nós trabalhamos com 3 tipos de locação e valores padrão: ")
    print("* Apartamentos R$ 700,00/ 1 quarto", 
          "\n* Casas R$900,00/ 1 quarto", 
          "\n* Estúdio R$ 1200,00")
    
    global escolha_opcoes_inicio
    global tr3s
    global d0is
    global um
    global valor
    escolha_opcoes_inicio = input("Qual das opções mais lhe(s) agrada(m)?\nInsira aqui: ")

    um = "Apartamentos R$ 700,00/ 1 quarto"
    d0is = "Casas R$900,00/ 1 quarto"
    tr3s = "Estúdio R$ 1200,00"

    if escolha_opcoes_inicio == "1":
      print(f"Você escolheu a opção :{um}")
      valor = 700
    elif escolha_opcoes_inicio == "2":
       print(f"Você escolheu a opção :{d0is}")
       valor = 900
    elif escolha_opcoes_inicio == "3":
       print(f"Você escolheu a opção {tr3s}")
       valor = 1200
    else:
       print("\nEssa opção não se encontra dentro de nossos padrões!")
       print("Escolha uma opção válida!")
       retorno()

def proximo():
    retorno()
    prosseguir = str(input("\nDeseja escolher esta opção?\n Sim (s) | Não (n)")).upper()
    return prosseguir.upper()


while True:
    prosseguir = proximo()
    if prosseguir == "S":
        print("\nVamos prosseguir para o próximo passo...")
        break

    elif prosseguir == "N":
        print("\nVoltando à página anterior!")
        

    else:
        print("\nEsta opção não condiz com as opções! Voltando à página anterior!")


#Auxílio do Gemini
"""while True:
    # ESTA É A LINHA CHAVE: ATUALIZA as variáveis a cada iteração, mesmo após o 'N'
    prosseguir = proximo() 
    
    # 2. Verifica a resposta da confirmação
    if prosseguir == "S":
        print("🎉 Vamos prosseguir para o próximo passo...")
        break  # Sai do loop principal
    
    elif prosseguir == "N":
        print("↩ Voltando à seleção de opções...")
        # O loop recomeça automaticamente, chamando proximo() novamente.
#print(f"Você escolheu a opção {escolha}")"""
# O problema era que eu tentava obter o valor da variável prosseguir antes de insirir algo dentro da mesma. 
# O problema era que eu colocava o prosseguir == proximo() fora do while True, além de usar while normal para criar a escolha

print("\nO valor do contrato é de R$ 2000,00. Podendo ser dividido em até 5 vezes!")
parcelamento()
def apontamento1():
    print("\nSe você quiser optar por alugar um apartamento com dois quartos será acrescentado R$ 250,00 na mensalidade")
    while True:
        if escolha_opcoes_inicio == "1":
            escolha_apont1 = input("Deseja fazer essa escolha? \nSim (s) | Não (n): ").upper()
            if escolha_apont1 == "S":
                print("\nSerá acrescentado + R$ 250,00 na mensalidade, mediante à escolha feita!")
                valor_total_locacao()
                global apontamento1_adi
                apontamento1_adi = 250
                break
            elif escolha_apont1 == "N":
                print("\nO valor ainda continua inalterado!")
                apontamento1_adi = 0
                break
            else:
                print("\nA escolha não se encaixa nas opções!")
                apontamento1()
                break
        elif escolha_opcoes_inicio == "2":
            print(f"Como você optou por {d0is}, você não tem acesso a esse apontamento!")
            apontamento1_adi = 0
            break

        elif escolha_opcoes_inicio == "3":
            print(f"Como você optou por {tr3s}, você não tem acesso a esse apontamento!")
            apontamento1_adi = 0
            break

        else:
            print("Essa opção não se enquadra nas demais opções!")
            apontamento1()
            break

        
    
apontamento1()

def apontamento2():
    print("\nPara incluir a vaga de garagem tanto para casas quanto para apartamentos o valor acrescentado é de R$ 300,00")
    
    while True:
        if escolha_opcoes_inicio == "1" or escolha_opcoes_inicio == "2":
            escolha_apont2 = input("Deseja fazer essa escolha? Sim (s) | Não (n): ").upper()
            if escolha_apont2 == "S":
                print("\nSerá acrescentado + R$ 300,00 na mensalidade, mediante à escolha feita!")
                valor_total_locacao()
                global apontamento2_adi
                apontamento2_adi = 300
                print(apontamento2_adi)
                break
            elif escolha_apont2 == "N": 
                print("O valor ainda continua inalterado!")
                valor_total_locacao()
                apontamento2_adi = 0
                print(valor_contrato)
                break
            else:
                print("A escolha não se encaixa nas opções!")
                apontamento2()
        elif escolha_opcoes_inicio == "3":
            print(f"Você escolheu a opção {tr3s}, portanto não tem acesso a esse apontamento!")
            apontamento2_adi = 0
            break
        else:
            print("A escolha não se encaixa nas opções!")
            apontamento2()
            break
    
apontamento2()

def apontamento3():
    print("\nNo caso do Estúdio pode ser adicionado vagas de estacionamento no valor de R$ 250,00 com 2 (duas) vagas, podendo acrescentar mais vagas no valor de R$ 60,00 cada!")
    while True:
        if escolha_opcoes_inicio == "3":
            escolha_apont3 = input("Deseja fazer essa escolha? Sim (s) | não (n): ").upper()
            if escolha_apont3 == "S":
                print("\n\nSerá acrescentado + R$ 250,00 na mensalidade, mediante à escolha feita!")
                valor_total_locacao()
                global apontamento3_adi
                apontamento3_adi = 250
                vagas_adicionais_opcs = input("Você deseja inserir alguma vaga além dessas duas vagas? Sim (s) | Não (n)").upper()
                if vagas_adicionais_opcs == "S": 
                    qtde_vagas = int(input("\nInsira aqui quantas vagas você quer que sejam adicionadas: "))
                    global apontamento3_1_adi
                    apontamento3_1_adi = 60
                    print(qtde_vagas * apontamento3_1_adi)
                    global apontamento3_comp
                    apontamento3_comp = (apontamento3_adi + (qtde_vagas)*apontamento3_1_adi)
                    break
                elif vagas_adicionais_opcs == "N":
                    print("Você optou por não adicionar mais vagas adicionais!")
                    apontamento3_comp = (apontamento3_adi)
                    break
                else:
                    print("Essa opção não condiz com o sistema!")
                    apontamento3()
                    break
                
            elif escolha_apont3 == "N": 
                print("O valor continua inalterado!")
                apontamento3_comp = 0
                break

            else:
                print("A escolha não se encaixa nas opções!")
                apontamento3()
                break
        elif escolha_opcoes_inicio == "2": 
            print(f"Como você escolheu a opção {d0is} você não poderá atribuir a esse apontamento!")
            apontamento3_comp = 0
            break
        elif escolha_opcoes_inicio == "1":
            print(f"Como você escolheu a opção {um} você não poderá atribuir a esse apontamento!")
            apontamento3_comp = 0
            break 
apontamento3()

def apontamento4():
    print("\nNós disponibilizamos um desconto de 5% no valor do aluguel de apartamentos para pessoas que não possuem crianças!")
    while True: 
        if escolha_opcoes_inicio == "1": 
            cond_crianca = input("Você possui crianças? Sim (s) | Não (n): ").upper()
            if cond_crianca == "N": 
                print("Você tem acesso ao desconto de 5% do valor do aluguel!")
                final_value()
                global apontamento4_adi
                apontamento4_adi = valor_total - (valor_total/100)*5
                #print(f"\nO valor obtido da negociação foi de R$ {apontamento4_adi}")
                break
            elif cond_crianca == "S":
                print("Você não tem acesso ao desconto de 5% do valor do alguel!")
                final_value()
                apontamento4_adi = valor_total
                #print(f"\nO valor obtido da negociação foi de R$ {apontamento4_adi}")
                break
            else: 
                print("Essa condição não está dentro das condições!")
                break
        elif escolha_opcoes_inicio == "2": 
            final_value()
            apontamento4_adi = valor_total
            print(f"Você não possui acesso ao desconto! Mediante que você escolheu a opção {d0is}.")
            print(f"\nO valor obtido da negociação foi de R$ {apontamento4_adi}")
            break

        elif escolha_opcoes_inicio == "3":
            final_value()
            apontamento4_adi = valor_total
            print(f"Você não possui acesso ao desconto! Mediante que você escolheu a opção {tr3s}.")
            print(f"\nO valor obtido da negociação foi de R$ {apontamento4_adi}")
            break
apontamento4()

for mes in range(1,13):
    mensalidade = apontamento4_adi
    parc_mes = 0.00
    if mes <= parcela:
        mensalidade += valor_parcelado
        parc_mes = valor_parcelado
        global valor_totalitario
        valor_totalitario =+ mensalidade

    print(f"Mês {mes:02d}: R$ {apontamento4_adi:.2f} (Aluguel) + R$ {parc_mes:.2f} (Contrato) = Valor Mensal: R${mensalidade:.2f}")
