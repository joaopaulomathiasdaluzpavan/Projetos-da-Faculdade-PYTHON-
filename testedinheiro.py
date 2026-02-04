c = 'add'
cont = 0
while c == 'add':
    valor_merc = float(input('\nInsira aqui o preço do produto adquirido: '))
    valor_cli = float(input('\nInsira aqui o valor que você possui: '))
    troco = round((valor_cli - valor_merc),2)
    cobra = (valor_merc - valor_cli)
    div5 = troco//5
    r_div5 = round((troco % 5),2)
    
    if troco >= 2 and troco < 5:
        div2 = troco // 2
        r_div2 = round((troco % 2),2)
    else:
        div2 = r_div5 // 2
        r_div2 = round((r_div5 % 2),2)
        
    if troco >= 1 and troco < 2:    
        div1 = troco // 1
        r_div1 = round((troco % 1),2)
    else:
        div1 = r_div2 // 1
        r_div1 = round((r_div2 % 1),2)
        
    if troco >= 0.50 and troco < 1:
        divo_5 = troco // 0.50
        r_div0_5 = round((troco % 0.50),2)
    else: 
        divo_5 = r_div1 // 0.50
        r_div0_5 = round((r_div1 % 0.50),2)
        
    if troco >= 0.25 and troco < 0.50:
        divo_25 = troco / 0.25
        r_div0_25 = round((troco % 0.25),2)
    else: 
        divo_25 = r_div0_5 / 0.25
        r_div0_25 = round((r_div0_5 % 0.25),2)
        
    if troco >= 0.10 and troco < 0.25:
        divo_1o = troco / 0.10
        r_div0_10 = round((troco % 0.10),2)
    else:
        divo_1o = r_div0_25 / 0.10
        r_div0_10 = round((r_div0_25 % 0.10),2)
        
    if troco >= 0.05 and troco < 0.10:
        divo_o5 = troco // 0.05
        r_div0_05 = round((troco % 0.05),2)
    else: 
        divo_o5 = r_div0_10 // 0.05
        r_div0_05 = round((r_div0_10 % 0.05),2)
        
    if troco >= 0.01 and troco < 0.05:
        divo_o1 = round((troco //0.01),2)
    else:
        divo_o1 = round((r_div0_05 / 0.01),2)
        
    if valor_merc < valor_cli:
        print('\nO valor do produto é de R${:.2f}, e o valor que a pessoa possui é de R${:.2f}'.format(valor_merc,valor_cli))
        print('\nO valor a ser devolvido é de R$ {:.2f}.'.format(troco))
        print('\nO número de moedas de R$ 0.01 é de',int(round((divo_o1),2)),'moeda(s).')
        print('\nO número de moedas de R$ 0.05 é de',int(round((divo_o5),2)),'moeda(s).')
        print('\nO número de moedas de R$ 0.10 é de',int(round((divo_1o),2)),'moeda(s).')
        print('\nO número de moedas de R$ 0.25 é de',int(round((divo_25),2)),'moeda(s).')
        print('\nO número de moedas de R$ 0.50 é de',int(round((divo_5),2)),'moeda(s).')
        print('\nO número de moedas de R$ 1.00 é de',int(round((div1),2)),'moeda(s).')
        print('\nO número de notas de R$ 2.00 é de',int(round((div2),2)),'nota(s).')
        print('\nO número de notas de R$ 5.00 é de',int(round((div5),2)),'nota(s).')
      
        #print(divo_o1)
        #print(r_div0_05)
        
    elif valor_merc == valor_cli:
        print('\nNão há troco!')
        
    else:
        print('\nO valor que está faltando é de R$',round(cobra,2))
    cont = cont + 1
    c = str(input('\nDigite <add> para continuar a compra: '))
print('\nO número de produtos comprados é de',cont,'produto(s).')