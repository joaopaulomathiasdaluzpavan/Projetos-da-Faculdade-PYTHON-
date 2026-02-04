c = 'add'
cont = 0
while c == 'add':
    valor_merc = float(input('\nInsira aqui o preço do produto adquirido: '))
    valor_cli = float(input('\nInsira aqui o valor que você possui: '))
    troco = round((valor_cli - valor_merc),2)
    cobra = (valor_merc - valor_cli)
    div2oo = troco//200
    r_div200 = round((troco % 200),2)
    if troco >= 100 and troco < 200:
        div1oo = troco//100
        r_div100 = round((troco % 100),2)
    else:
        div1oo = r_div200//100
        r_div100 = round((r_div200 % 100),2)
    
    if troco >= 50 and troco < 100:
        div5o = troco//50
        r_div50 = round((troco % 50),2)
    else:
        div5o = r_div100//50
        r_div50 = round((r_div100 % 50),2)
    
    if troco >= 20 and troco < 50:
        div2o = troco//20
        r_div20 = round((troco % 20),2)
    else:
        div2o = r_div50//20
        r_div20 = round((r_div50 % 20),2)
    
    if troco >= 10 and troco < 20:
        div1o = troco//10
        r_div10 = round((troco % 10),2)
    else:
        div1o = r_div20//10
        r_div10 = round((r_div20 % 10),2)
        
    if troco >= 5 and troco < 10:
        div5 = troco//5
        r_div5 = round((troco % 5),2)
    else: 
        div5 = r_div10 // 5
        r_div5 = round((r_div10 % 5),2)
    
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
        print('\nO valor do produto é de R${:.2f}, e o valor que a pessoa possui é de R$ {:.2f}'.format(valor_merc,valor_cli))
        print('\nO valor a ser devolvido é de R$ {:.2f}.'.format(troco))
        print('\nO número de moedas de R$ 0.01 é de',int(round((divo_o1),2)),'moeda(s).')
        print('\nO número de moedas de R$ 0.05 é de',int(round((divo_o5),2)),'moeda(s).')
        print('\nO número de moedas de R$ 0.10 é de',int(round((divo_1o),2)),'moeda(s).')
        print('\nO número de moedas de R$ 0.25 é de',int(round((divo_25),2)),'moeda(s).')
        print('\nO número de moedas de R$ 0.50 é de',int(round((divo_5),2)),'moeda(s).')
        print('\nO número de moedas de R$ 1.00 é de',int(round((div1),2)),'moeda(s).')
        print('\nO número de notas de R$ 2.00 é de',int(round((div2),2)),'nota(s).')
        print('\nO número de notas de R$ 5.00 é de',int(round((div5),2)),'nota(s).')
        print('\nO número de notas de R$ 10.00 é de',int(round((div1o),2)),'nota(s).')
        print('\nO número de notas de R$ 20.00 é de',int(round((div2o),2)),'nota(s).')
        print('\nO número de notas de R$ 50.00 é de',int(round((div5o),2)),'nota(s).')
        print('\nO número de notas de R$ 100.00 é de',int(round((div1oo),2)),'nota(s).')
        print('\nO número de notas de R$ 200.00 é de',int(round((div2oo),2)),'nota(s).')
        
        
        
        #print(divo_o1)
        #print(r_div0_05)
        #print(div1o)
        
    elif valor_merc == valor_cli:
        print('\nNão há troco!')
        
    else:
        print('\nO valor que está faltando é de R$',round(cobra,2))
    cont = cont + 1
    c = str(input('\nDigite <add> para continuar a compra: '))
print('\nO número de produtos comprados é de',cont,'produto(s).')