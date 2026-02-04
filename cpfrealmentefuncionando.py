cpf = str(input('Digite um CPF para ver se é válido ou não:'))
if len(cpf) == 11:
 print('\nPrimeira etapa da validação concluída')

 cpf1 = int(cpf[0])
 cpf2 = int(cpf[1])
 cpf3 = int(cpf[2])
 cpf4 = int(cpf[3])
 cpf5 = int(cpf[4])
 cpf6 = int(cpf[5])
 cpf7 = int(cpf[6])
 cpf8 = int(cpf[7])
 cpf9 = int(cpf[8])
 cpf10 = int(cpf[-2])
 cpf11 = int(cpf[-1])
 
 valid2 = (cpf1 * 10) + (cpf2 * 9) + (cpf3 * 8) + (cpf4 * 7) + (cpf5 * 6) + (cpf6 * 5) + (cpf7 * 4) + (cpf8 * 3) + (cpf9 * 2)
 valid2_1 = (valid2 * 10) % 11 
 pen_dig = valid2_1
 print(pen_dig)
 if pen_dig == 10:
     pen_dig = 0

 if pen_dig == cpf10:
   print('A segunda etapa da verificação do CPF está Válida')
 else:
   print('A segunda etapa da verificação do CPF está Inválida')
   
 valid3 = ((cpf1 * 11) + (cpf2 * 10) + (cpf3 * 9) + (cpf4 * 8) + (cpf5 * 7) + (cpf6 * 6) + (cpf7 * 5) + (cpf8 * 4) + (cpf9 * 3) + ((pen_dig) * 2))
 valid3_1 = (valid3 * 10) % 11
 ult_dig = valid3_1
 print(ult_dig)
 if ult_dig == 10:
     ult_dig = 0
     pen_dig == cpf10 and ult_dig == cpf11
     print('A terceira etapa do CPF está válida!')
     print(cpf1,cpf2,cpf3,'.',cpf4,cpf5,cpf6,'.',cpf7,cpf8,cpf9,'-',pen_dig,ult_dig)

 
 elif cpf10 == pen_dig and cpf11 == ult_dig:
     print('A terceira etapa do CPF está válida!')
     print(cpf1,cpf2,cpf3,'.',cpf4,cpf5,cpf6,'.',cpf7,cpf8,cpf9,'-',pen_dig,ult_dig)
 else:
     print('\nA terceira etapa da verificação do CPF está Inválida')
     print('\nO cpf digitado:', cpf,'está incorreto!')
  
elif len(cpf) < 11 or len(cpf) > 11:
   print('\nA primeira etapa da validação do CPF está Inválida')
