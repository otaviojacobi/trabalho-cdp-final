import e_bplustree_to_file as bpt
import pickle


def consulta1(valorordem, arvdata, valorlow, valorhigh, listaflags, reversal=0):
    ''' As variáveis de parâmetro (estacao ~ vento) são todas booleanas
    tipoconsulta é 1 (procura na data) ou 0 (procura em qualquer outra)
    valorordem é qual o valor é usado para ordenamento na busca de range para datas:
    0 : num de estacao
    1 : data (nunca será no tipo 1)
    2 : precipitacao
    3 : TempMaxima
    4 : TempMinima
    5 : Insolacao
    6 : Umidade Relativa Media
    7 : Velocidade do Vento Media''
    '''
    resultadobruto = arvdata.getRange(valorlow, valorhigh, 1)
    listaordenada = []
    if valorordem > 1:
        for res in resultadobruto:
            truevalor = valorordem - 1
            aux = res.split('$')[1].split(',')
            saida = aux[truevalor] +'!' + res
            listaordenada.append(saida)
        #print("1:", listaordenada)
        listaordenada.sort()
        listaordenada.reverse()
        #print("pos sort", listaordenada)
        listasaida = []
        for entrada in listaordenada:
            aux = entrada.split('!')[1].split('$')
            dataentrada = aux[0]
            parametros = aux[1].split(',')
            umasaida = []
            if listaflags[1] == 1:
                umasaida.append(dataentrada)
            for numero in range(0, 7):
                truenumber = numero
                if numero > 1:
                    truenumber -= 1
                if listaflags[numero] == 1 and numero != 1:
                    umasaida.append(parametros[truenumber])
                    #print(umasaida)
            if(umasaida[2]!=''):
                listasaida.append(umasaida)
        if reversal!=0:
            listasaida.reverse()
        return listasaida

    if valorordem == 0:
        listaordenada = resultadobruto
        listasaida = []
        for entrada in listaordenada:
            aux = entrada.split('$')
            dataentrada = aux[0]
            parametros = aux[1].split(',')
            umasaida = []
            if listaflags[1] == 1:
                umasaida.append(dataentrada)
            for numero in range(7):
                truenumber = numero
                if numero > 1:
                    truenumber -= 1
                if listaflags[numero] == 1 and numero != 1:
                    umasaida.append(parametros[truenumber])
                if(umasaida[2]!=''):
                    listasaida.append(umasaida)

        if reversal!=0:
            listasaida.reverse()
        return listasaida

def consulta2(pesquisa, lista_bplus, regiao,dictionary, quantidade, reversal=0):
    resultadobruto=lista_bplus[pesquisa].getRange(0,999)
    total=[]
    for elemento in resultadobruto:
        if elemento.split('$')[-1][0:5] in dictionary[regiao]:
            total.append(elemento)
    saida=[]
    if reversal==0:
        for num in range(quantidade):
            saida.append(total[-1-num])
    if reversal==1:
        for num in range(quantidade):
            saida.append(total[num])

    print(saida)

def consulta(tipoconsulta, valorordem, lista_bplus, valorlow, valorhigh, listaflags,dictionary,regiao,reversal=0):
    if tipoconsulta==1:
        return consulta1(valorordem, lista_bplus[6], valorlow, valorhigh, listaflags, reversal)
    elif tipoconsulta==2:
        consulta2(valordem,lista_bplus,regiao,dictionary)

chuva, tempM, tempm, sol, umidade, vento, data = bpt.insere_from_file('d_dados_clr.csv')
bpluses=[chuva, tempM, tempm, sol, umidade, vento, data]

dictionary=pickle.load(open('estacoes.dic','rb'))
consulta2(4,bpluses,'sul',dictionary,10,1)
