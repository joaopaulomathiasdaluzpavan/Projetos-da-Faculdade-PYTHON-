c = 'v'
cont = 0
cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0

while c == 'v':
    candidatos = int(input('\nDigite 1 para votar em Eymael.\nDigite 2 para votar em Levy Fidelix.\nDigite 3 para votar em Cabo Daciolo.\nDigite 4 para votar nulo.\nDigire 5 para votar em branco.\n:'))
    if candidatos == 1:
        cont_1 = (cont_1 + 1)
        cont = (cont + 1)
    elif candidatos == 2:
        cont_2 = (cont_2 + 1)
        cont = (cont + 1)
    elif candidatos == 3:
        cont_3 = (cont_3 + 1)
        cont = (cont + 1)
    elif candidatos == 4:
        cont_4 = (cont_4 + 1)
        cont = (cont + 1)
    elif candidatos == 5:
        cont_5 = (cont_5 + 1)
        cont = (cont + 1)
    c = str(input('\nDigite <v> para armazenar os votos da eleicão:'))
print('\nO número de votos do candidato Eymael é de',cont_1,'votos')
per_1 = round((cont_1 * 100)/cont,2)
print('A porcentagem dos votos de Eymael é de',per_1,'%')
print('\nO número de votos do candidato Levy Fidelix é de',cont_2,'votos')
per_2 = round((cont_2 * 100)/cont,2)
print('A porcentagem dos votos de Levy Fidelix é de',per_2,'%')
print('\nO número de votos do candidato Cabo Daciolo é de',cont_3,'votos')
per_3 = round((cont_3 * 100)/cont,2)
print('A porcentagem dos votos de Cabo Daciolo é de',per_3,'%')
print('\nO número de votos nulos é de',cont_4,'votos')
per_4 = round((cont_4 * 100)/cont,2)
print('A porcentagem dos votos nulos é de',per_4,'%')
print('\nO número de votos brancos é de',cont_5,'votos')
per_5 = round((cont_5 * 100)/cont,2)
print('A porcentagem dos votos brancos é de',per_5,'%')
print('\nO total de eleitores foram de',cont,'eleitores')