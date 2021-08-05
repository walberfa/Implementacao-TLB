# Este script roda o main.py e seta os parâmetros, configurados para encontrar um falso positivo.
#import csv
import simulador
import random
from simulador import executaSimulador

#Declaração dos parâmetros fixos
total_cache = 8
arquivo_acesso = "controle.txt"
debug = 0

def quantidade_linhas_arquivo():
    a = open(arquivo_acesso, 'r')
    contador  = 0
    for linha in a:
        contador += 1
    #print(contador)
    return contador

#salva o resultado na variável senão acaba chamando a função a cada ciclo do for
linhas = quantidade_linhas_arquivo()


# Seta os parâmetros
# Quando for testar, copia e cola alterando o tipo de código para cada tipo de falha
# Seta no range do for a quantidade de vezes que vai rodar para cada teste

for i in range(0,1):

    codigo = "NENHUM"
    endereco_falha = 20 #random.randint(0, linhas)
    linha_tlb_falha = 2 #random.randint(1,7)
    bit_falho = 31 #random.randint(0, 31)
    tipo_falhas_inseridas = "FALHA_DUPLA"

    # chama o simulador.py, executa e contabiliza o retorno
    
    simulador.executaSimulador(total_cache, arquivo_acesso, debug, codigo, endereco_falha, linha_tlb_falha, bit_falho, tipo_falhas_inseridas)
    print("iteração:",i+1)
    print("codigo: nenhum")
    print("falha dupla")
    print('-' * 5)
