import e_bplustree_to_file as bpt
import pickle


def consulta1(valorordem, lista_bplus, valorlow, valorhigh, listaflags,reversal=0,quantidade=10):
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

    arvdata=lista_bplus[6]
    resultadobruto = arvdata.getRange(valorlow, valorhigh, 1)
    listaordenada = []
    if valorordem > 1:
        for res in resultadobruto:
            truevalor = valorordem - 1
            aux = res.split('$')[1].split(',')
            aux[truevalor] = aux[truevalor].split('.', 1)
            aux[truevalor][0] = aux[truevalor][0].zfill(3)
            if len(aux[truevalor]) == 2:
                aux[truevalor] = aux[truevalor][0] + '.' + aux[truevalor][1]
            else:
                aux[truevalor] = aux[truevalor][0]
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
            for numero in range(8):
                truenumber = numero
                if numero > 1:
                    truenumber -= 1
                if listaflags[numero] == 1 and numero != 1:
                    umasaida.append(parametros[truenumber])
                    #print(umasaida)
            if('' not in umasaida):
                listasaida.append(umasaida)
        if reversal!=0:
            listasaida.reverse()

        for elemento in listasaida:
            var_aux_=elemento[0].split('/')
            year,month,day =var_aux_[0],var_aux_[1],var_aux_[2]
            elemento[0]='/'.join([day,month,year])

        if quantidade != 4242:
            return listasaida[0:quantidade]
        else:
            return listasaida[0:]


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
            for numero in range(8):
                truenumber = numero
                if numero > 1:
                    truenumber -= 1
                if listaflags[numero] == 1 and numero != 1:
                    umasaida.append(parametros[truenumber])
                if('' not in umasaida):
                    listasaida.append(umasaida)

        if reversal!=0:
            listasaida.reverse()

        for elemento in listasaida:
            var_aux_=elemento[0].split('/')
            year,month,day =var_aux_[0],var_aux_[1],var_aux_[2]
            elemento[0]='/'.join([day,month,year])

        if quantidade != 4242:
            return listasaida[0:quantidade]
        else:
            return listasaida[0:]

def consulta2(pesquisa, lista_bplus, regiao,dictionary, quantidade=10, reversal=0):
    if regiao!='todas':
        resultadobruto=lista_bplus[pesquisa].keys()
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

    else:
        resultadobruto=lista_bplus[pesquisa].keys()
        saida=[]
        if reversal==0:
            for num in range(quantidade):
                saida.append(resultadobruto[-1-num])
        if reversal==1:
            for num in range(quantidade):
                dsaida.append(resultadobruto[num])

    listafinal = []
    for resultado in saida:
        listaaux=[]
        newresult = resultado.split('$')
        listaaux.append(newresult[1][5:])
        listaaux.append(newresult[1][0:5])
        listaaux.append(newresult[0])
        listafinal.append(listaaux)
    #print(listafinal)
    return listafinal

def consulta3(pesquisa, lista_bplus, valorlow, valorhigh,quantidade=10,reversal=0):
    resultadobruto = lista_bplus[pesquisa].getRange(valorlow, valorhigh, 0)
    #print(resultadobruto)
    listafinal = []
    for resultado in resultadobruto:
        listaaux = []
        newresult = resultado.split('$')
        listaaux.append(newresult[1][5:])
        listaaux.append(newresult[1][0:5])
        listaaux.append(newresult[0])

        listafinal.append(listaaux)
    #return listafinal
    if reversal==1:
        if quantidade != 4242:
            return listafinal[0:quantidade]
        else:
            return listafinal[0:]
    elif reversal==0:
        if quantidade != 4242:
            return listafinal[-quantidade-1:-1]
        else:
            return listafinal[0:]


#chuva, tempM, tempm, sol, umidade, vento, data = bpt.insere_from_file('d_dados_clr.csv')
#bpluses=[chuva, tempM, tempm, sol, umidade, vento, data]

#k=consulta1(2,bpluses,'01/06/2015','12/11/2015',[1,1,1,0,0,0,0,0])
#print(k)
# i=0
# for element in k:
#     i=i+1
#     print(element)
# print(i)
