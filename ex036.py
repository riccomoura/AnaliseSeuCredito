import math
import random
from time import sleep
#Loading sistêmico e orientações ao usuário
print('========== PYTHON BANK DO BRASIL / EST. 2021 ============')
print('\nSeja bem vindo(a) ao Python Bank!')
sleep(3)
print('\nAqui você poderá consultar as condições oferecidas para análise do seu crédito imobiliário.')
sleep(4)
print('\nIMPORTANTE: As informações devem ser digitadas sem pontuações (".", ",", "!", "...").')
sleep(4)
print('\nOs números não devem conter separadores. Ex.: para R$300.000,00 digite "300000".')
sleep(4)
print('\nInicializando terminal...')
sleep(2)
print('\n========== ANÁLISE DE CRÉDITO PERSONALIZADA ============')
sleep(3)
print('\nOlá! Seja bem-vindo(a) a análise de crédito do Python Bank SEM JUROS. ')
sleep(5)

nome = str(input('Por favor, digite seu primeiro nome: '))
vc = float(input('Digite o valor do imóvel de interesse: R$'))
salario = float(input('Digite sua renda mensal comprovada: R$'))
prazoano = int(input('Escolha o prazo desejado (em anos): '))
sleep(3)
prazomensal = prazoano * 12
valorparcela = vc / prazomensal

if valorparcela < salario * 0.30 and vc <= 500000:
    print('\nFinanciamento aprovado, Sr(a) {}. O valor de R${:.2f} ao longo de {} prestações mensais, sem juros e sem entrada, está de acordo com nossa política de segurança.'.format(nome, valorparcela, prazomensal))
    sleep(3)
    print('Seu score é muito bom, parabéns!')
elif valorparcela >= salario * 0.30 and vc <= 500000:
    print('\nSr(a). {}, infelizmente o financiamento foi REPROVADO.\n Consulte a instituição bancária através do telefone 0800-553-8988 para mais informações ou pedido de revisão. '.format(nome))
    sleep(3)
    print('\nRazão: o valor de R${:.2f} é superior a 30% da sua renda.'.format(valorparcela))
    sleep(3)
    print('\nNão desista da Python Bank, entendemos que cada caso é um caso.\nNos dispomos a discutir novas condições em busca de solução para você. :-)')

else:
    sleep(1)
    print('Sr(a). {}, o crédito máximo disponibilizado para financiamento sem juros e sem entrada é de R$500.000,00.'.format(nome))