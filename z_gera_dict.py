import pickle

fopen = open('b_estacoes.txt','r')

brasil={}
brasil['sul']=[]
brasil['sudeste']=[]
brasil['centrooeste']=[]
brasil['nordeste']=[]
brasil['norte']=[]

sul=['RS', 'PR', 'SC']
sudeste=['SP', 'RJ', 'MG', 'ES']
centrooeste=['GO', 'MS', 'MT','DF']
nordeste=['SE','RN','PI','PE','PB','MA','CE','BA','AL']
norte=['AC','AM','AP','PA','RO','RR','TO']


for line in fopen:
    estacao=line.split('-')[0].strip(' ')
    estado=line.split(' ')[-1].strip('\n').strip(' ')
    if estado in sul:
        brasil['sul'].append(estacao)
    elif estado in sudeste:
        brasil['sudeste'].append(estacao)
    elif estado in centrooeste:
        brasil['centrooeste'].append(estacao)
    elif estado in nordeste:
        brasil['nordeste'].append(estacao)
    elif estado in norte:
        brasil['norte'].append(estacao)

afile=open('estacoes.dic','wb')
pickle.dump(brasil,afile)
