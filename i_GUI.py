#!/usr/bin/env python3
from tkinter import *
import tkinter.filedialog as fdialog
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
from functools import partial
from tkinter.filedialog import askopenfilename
import e_bplustree_to_file as bpt
from g_buscas import *
from tabulate import tabulate
import tkinter.scrolledtext as tkst


def MainWindow(window):

    global lista_cb
    global radio_box

    #frame
    introFrame = Frame(window)
    introFrame.pack()

    # create the main logo
    bg = PhotoImage(file="img/inicial2.gif")
    inicial = Label(introFrame, image=bg)
    inicial.pack()

    #labels
    introFrame.option_add("*background", "#BBFFFF")

    dataI = Label(introFrame, text="Data Inicial: ", font = "Arial 12 bold")
    dataF = Label(introFrame, text="Data Final: ", font = "Arial 12 bold")
    opcao = Label(introFrame, text="Selecione a opção: ", font = "Arial 12 bold")
    estds = Label(introFrame, text="Selecione uma região: ", font = "Arial 12 bold")
    #qt1 = Label(introFrame, text="Quantidade: ", font = "Arial 12 bold")
    qt2 = Label(introFrame, text="Quantidade: ", font = "Arial 12 bold")
    opcao2 = Label(introFrame, text="Selecione a opção: ", font = "Arial 12 bold")
    minimo = Label(introFrame, text="Minimo: ", font = "Arial 12 bold")
    maximo = Label(introFrame, text="Maximo: ", font = "Arial 12 bold")

    #checkboxes
    # maior=Checkbutton(introFrame, text="Maior", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    # menor=Checkbutton(introFrame, text="Menor", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')

    Estacao=Checkbutton(introFrame, variable=VarEst,text="Estação", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    Estacao.select()
    Data=Checkbutton(introFrame ,variable=VarData,text="Data", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    Data.select()
    Chuva=Checkbutton(introFrame, variable=VarChuva,text="Chuva", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    TempM=Checkbutton(introFrame, variable=VarTempM,text="Temp. M.", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    Tempm=Checkbutton(introFrame, variable=VarTempm,text="Temp. m.", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    Sol=Checkbutton(introFrame, variable=VarSol,text="Insolação", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    Umidade=Checkbutton(introFrame ,variable=VarUmi,text="Umidade", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    Vento=Checkbutton(introFrame, variable=VarVento,text="Vento", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')



    #textboxes
    introFrame.option_add("*background", "#FFFFFF"),
    ent1 = Entry(introFrame,textvariable=_1ent1)
    ent2 = Entry(introFrame,textvariable=_1ent2)
    #ent3 = Entry(introFrame)
    ent4 = Entry(introFrame,textvariable=amount)
    ent5 = Entry(introFrame,textvariable=Entrada4)
    ent6 = Entry(introFrame,textvariable=Entrada5)

    #qtbo = Entry(introFrame, width='12')


    #radioboxes
    var=IntVar()
    consulta1=Radiobutton(introFrame,variable=var,value=1, command=partial(fazConsulta,1) ,text="Consulta 1",font = "Arial 12 bold",background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    consulta2=Radiobutton(introFrame,variable=var,value=2, command=partial(fazConsulta,2),text="Consulta 2",font = "Arial 12 bold",background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    consulta3=Radiobutton(introFrame,variable=var,value=3, command=partial(fazConsulta,3),text="Consulta 3",font = "Arial 12 bold",background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')

    nvar=IntVar()
    consulta11=Radiobutton(introFrame,variable=nvar,value=4,state=DISABLED ,cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")
    consulta12=Radiobutton(introFrame,variable=nvar,value=1, command=partial(fazFirst,4),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")
    consulta13=Radiobutton(introFrame,variable=nvar,value=6, command=partial(fazFirst,5),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")
    consulta14=Radiobutton(introFrame,variable=nvar,value=7, command=partial(fazFirst,6),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")
    consulta15=Radiobutton(introFrame,variable=nvar,value=8, command=partial(fazFirst,7),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")
    consulta16=Radiobutton(introFrame,variable=nvar,value=9, command=partial(fazFirst,8),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")
    consulta17=Radiobutton(introFrame,variable=nvar,value=10, command=partial(fazFirst,9),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")
    consulta18=Radiobutton(introFrame,variable=nvar,value=11, command=partial(fazFirst,10),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")

    biggest=Radiobutton(introFrame,text='Maior',variable=MAIOR,value=12, command=partial(mudaMENOR,12),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")
    menorest=Radiobutton(introFrame,text='Menor',variable=MAIOR,value=13, command=partial(mudaMENOR,13),cursor='hand1',height=1,background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B")

    #buttons
    bt1 = Button(introFrame,command=partial(fazBusca,introFrame,window),relief = RAISED, width=13,font = "Arial 14 bold", text="Fazer Consulta", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')
    bt2 = Button(introFrame,command=load_file, width=13,relief = RAISED, font = "Arial 14 bold", text="Incluir nova DB", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')
    bt3 = Button(introFrame,command=load_bin, relief = RAISED, width=13,font = "Arial 14 bold", text="Carregar .bin", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')
    bt4 = Button(introFrame,command=ABOUT_US, relief = RAISED,font = "Arial 14 bold", text="?", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')


    img = PhotoImage(file="img/inmet.gif")
    btINMET = Button(introFrame, relief=RIDGE, cursor='hand1')
    btINMET.image = img
    btINMET.configure(image=img)
    btINMET['command']=partial(InfoInMet, introFrame, window)

    #comboboxes
    introFrame.option_add("*background", "#E0FFFF"),
    introFrame.option_add("*foreground", "#00688B"),

    combobox=ttk.Combobox(introFrame,textvariable=consulta_2,state='readonly', font = "Arial 12 bold", values=[' ','Precipitação','TempMáxima', 'TempMínima', 'Insolação', 'Umidade Relativa Média', 'Velocidade do Vento Média'])
    combobox['width']= '25'

    combobox2=ttk.Combobox(introFrame,textvariable=regiao_2,state='readonly', font = "Arial 12 bold",)
    combobox2['values']=['Todas','Sul', 'Sudeste', 'CentroOeste', 'Nordeste', 'Norte']
    combobox2['width']= '25'

    combobox3=ttk.Combobox(introFrame,textvariable=consulta_3 ,state='readonly', font = "Arial 12 bold", values=[' ','Precipitação','TempMáxima', 'TempMínima', 'Insolação', 'Umidade Relativa Média', 'Velocidade do Vento Média'])
    combobox3['width']= '25'


    #labels
    dataI.place(x=50, y=400)
    dataF.place(x=50, y=470)
    opcao.place(x=345, y=140)
    estds.place(x=345, y=220)
    #qt1.place(x=50, y=540)
    qt2.place(x=395, y=390)
    opcao2.place(x=650,y=140)
    minimo.place(x=650,y=220)
    maximo.place(x=650,y=300)


    #radioboxes
    consulta1.place(x=90, y=40)
    consulta2.place(x=400, y=40)
    consulta3.place(x=730, y=40)
    consulta11.place(x=80, y=100)
    consulta12.place(x=80, y=130)
    consulta13.place(x=80, y=160)
    consulta14.place(x=80, y=190)
    consulta15.place(x=80, y=220)
    consulta16.place(x=80, y=250)
    consulta17.place(x=80, y=280)
    consulta18.place(x=80, y=310)
    biggest.place(x=365,y=360)
    menorest.place(x=450,y=360)


    #textboxes
    ent1.place(x=50, y=430)
    ent2.place(x=50, y=500)
    #ent3.place(x=50, y=570)
    ent4.place(x=365,y=420)
    ent5.place(x=650,y=250)
    ent6.place(x=650,y=330)

    #comboboxes
    combobox.place(x=345,y=175)
    combobox2.place(x=345, y=250)
    combobox3.place(x=650, y=175)

    #buttons
    btINMET.place(x=660, y=420)
    bt1.place(x=370, y=470)
    bt2.place(x=370, y=570)
    bt3.place(x=370, y=520)
    bt4.place(x=880,y=20)

    #checkboxes
    #maior.place(x=80, y=210)
    #menor.place(x=160, y=210)
    Estacao.place(x=110, y=100)
    Data.place(x=110, y=130)
    Chuva.place(x=110, y=160)
    TempM.place(x=110, y=190)
    Tempm.place(x=110, y=220)
    Sol.place(x=110, y=250)
    Umidade.place(x=110, y=280)
    Vento.place(x=110, y=310)


    introFrame.mainloop()

def mudaMENOR(valor):
    global MENOR
    if valor==12:
        MENOR=0
    elif valor==13:
        MENOR=1

def fazBusca(frame,window):

    # destroy previous window
    frame.destroy()

    # make a new frame for the widgets
    recFrame = Frame(window)
    recFrame.pack(fill=BOTH)

    # make a new frame for the image
    recImage = Frame(recFrame)
    recImage.pack(fill=BOTH)

    # create widget and assign image to it
    img = PhotoImage(file="img/inicial.gif")   # convert the Image object into a TkPhoto object
    backgroundImage = Label(recImage, image=img)    # put it in the display window
    backgroundImage.pack()

    btReturn = Button(recImage, command=partial(ActionGotoMain, recFrame, window), text="↩",relief = RAISED, font = "Arial 14 bold", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')
    btReturn.place(x=55, y=39)

    try:
        global saida_FINAL

        lista=[VarEst.get(), VarData.get(), VarChuva.get(),VarTempM.get(), VarTempm.get(), VarSol.get(),VarUmi.get(),VarVento.get()]

        if radio_box==1:
            saida_FINAL=consulta1(consulta1_s,infos,_1ent1.get(),_1ent2.get(),lista,quantidade=int(amount.get()),reversal=MENOR)
        elif radio_box==2:
            if consulta_2.get()=='Precipitação':
                a=0
            elif consulta_2.get()=='TempMáxima':
                a=1
            elif consulta_2.get()=='TempMínima':
                a=2
            elif consulta_2.get()=='Insolação':
                a=3
            elif consulta_2.get()=='Umidade Relativa Média':
                a=4
            elif consulta_2.get()=='Velocidade do Vento Média':
                a=5
            saida_FINAL=consulta2(a,infos,regiao_2.get().lower(),dictionary,quantidade=int(amount.get()),reversal=MENOR)
        elif radio_box==3:
            if consulta_3.get()=='Precipitação':
                a=0
            elif consulta_3.get()=='TempMáxima':
                a=1
            elif consulta_3.get()=='TempMínima':
                a=2
            elif consulta_3.get()=='Insolação':
                a=3
            elif consulta_3.get()=='Umidade Relativa Média':
                a=4
            elif consulta_3.get()=='Velocidade do Vento Média':
                a=5
            saida_FINAL=consulta3(a,infos,int(Entrada4.get()),int(Entrada5.get()),quantidade=int(amount.get()),reversal=MENOR)
    except:
        messagebox.showerror("Error!", "Algum errou aconteceu, tente reiniciar !")
        pass


    TABELAO=fazString(saida_FINAL)

    # create the text area frame that will be called by other functions to show the result
    recTextArea = Frame(recFrame)
    recTextArea.place(x=70, y=95, height=490, width=824)

    saida =  tkst.ScrolledText(recTextArea,undo=TRUE,width=115,height=32)
    saida.insert(INSERT,TABELAO)
    saida.place(x=0,y=0)
    #sada['state']=DISABLED


    recFrame.mainloop()


def ABOUT_US():
    msg="UFRGS-Informática\nArthur Medeiros - 261587 \nFelipe Leivas - 000000\nOtavio Jacobi - 261569\nVersão 1.0.0 - 06/2016"
    messagebox.showinfo("About Us!",msg)


def fazString(lista_de_string):
    if radio_box==2 or radio_box==3:
        lis_final=[]
        for lista in lista_de_string:
            finzao= [dictionary[lista[1]],lista[0],str(float(lista[2]))]
            lis_final.append(finzao)


        if radio_box==2:
            k=consulta_2.get()
        elif radio_box==3:
            k=consulta_3.get()

        parameters =['CIDADE', 'DIA',k]

        TABELA_BONITA=tabulate(lis_final,headers=parameters,tablefmt="simple")

    elif radio_box==1:
        k=achaK()
        lis_final=[]
        for lista in lista_de_string:
            finzao=[dictionary[lista[1]],lista[0]]
            for element in lista[2:]:
                element=str(float(element))
                finzao.append(element)
            lis_final.append(finzao)

        TABELA_BONITA=tabulate(lis_final,headers=k,tablefmt="simple")


    return TABELA_BONITA


def achaK():
    lista=[VarEst.get(), VarData.get(), VarChuva.get(),VarTempM.get(), VarTempm.get(), VarSol.get(),VarUmi.get(),VarVento.get()]
    saida=[]
    if lista[0]==1:
        saida.append('Estação')
    if lista[1]==1:
        saida.append('Data')
    if lista[2]==1:
        saida.append('Chuva')
    if lista[3]==1:
        saida.append('TempMáxima')
    if lista[4]==1:
        saida.append('TempMínima')
    if lista[5]==1:
        saida.append('Insolação')
    if lista[6]==1:
        saida.append('Umidade')
    if lista[7]==1:
        saida.append('Vento')

    return saida

def fazFirst(var):
    global consulta1_s

    if var==3:
        consulta1_s=0
    if var==4:
        consulta1_s=1
    if var==5:
        consulta1_s=2
    if var==6:
        consulta1_s=3
    if var==7:
        consulta1_s=4
    if var==8:
        consulta1_s=5
    if var==9:
        consulta1_s=6
    if var==10:
        consulta1_s=7


def fazConsulta(var):
    global radio_box
    if var==1:
        radio_box=1
        #print('1')
    elif var==2:
        radio_box=2
        #print('2')
    elif var==3:
        radio_box=3
        #print('3')

def InfoInMet(frame, window):
    # destroy previous window
    frame.destroy()

    # make a new frame for the widgets
    recFrame = Frame(window)
    recFrame.pack(fill=BOTH)

    # make a new frame for the image
    recImage = Frame(recFrame)
    recImage.pack(fill=BOTH)

    # create widget and assign image to it
    img = PhotoImage(file="img/inicial.gif")   # convert the Image object into a TkPhoto object
    backgroundImage = Label(recImage, image=img)    # put it in the display window
    backgroundImage.pack()

    #the return button
    btReturn = Button(recFrame, command=partial(ActionGotoMain, recFrame, window), text="↩",relief = RAISED, font = "Arial 14 bold", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')
    #btReturn = Button(recFrame,, relief=GROOVE, , font="Courier 15 bold", background="PaleTurquoise1", activebackground="PaleTurquoise1")
    btReturn.place(x=55, y=39)


    # create the text area frame that will be called by other functions to show the result
    recTextArea = Frame(recFrame)
    recTextArea.place(x=70, y=95, height=450, width=824)

    texto=tkst.ScrolledText(recTextArea,height=23,width=89,font = "Arial 12 bold", fg="LightBlue4", background="Sky blue")

    mon_str='''
    O Instituto Nacional de Meteorologia do Brasil (INMET) é um órgão federal da administração direta do Ministério da Agricultura, Pecuária e Abastecimento (MAPA), criado em 1909 com a missão de prover informações meteorológicas através de monitoramento, análise e previsão do tempo e clima, concorrendo com processos de pesquisa aplicada para prover informações adequadas em situações diversas, como no caso de desastres naturais como inundações e secas extremas que afetam, limitam ou interferem nas atividades cotidianas da sociedade brasileira.\n
    No INMET, há uma seção própria para a recepção e tratamento destas imagens de satélites. Então, os meteorologistas mapeiam e analisam estas informações e, só depois de feitas todas estas análises (cartas de superfície, modelos numéricos, imagens de satélites, etc) tem-se maior segurança em elaborar a previsão do tempo para todo o Brasil.
    Quem utiliza estas informações sobre o tempo?
    São inúmeras as pessoas, físicas ou jurídicas, que delas se utilizam, por exemplo:
    a) Agricultura: garantia de uma boa colheita;
    b) Marinha: proteção aos seus marinheiros, navios e passageiros;
    c) Aeronáutica: proteção e segurança de seus pilotos, aeronaves e passageiros;
    d) Pescadores: condições favoráveis à pesca;
    e) Turismo: garantia de um passeio e/ou viagem feliz e tranqüila.
    Observação Meteorológica:
    Uma observação meteorológica consiste na medição, registro ou determinação de todos os elementos que, em seu conjunto, representam as condições meteorológicas num dado momento e em determinado lugar, utilizando instrumentos adequados e valendo-se da vista. Estas observações realizadas de maneira sistemática, uniforme, ininterrupta e em horas estabelecidas, permitem conhecer as características e variações dos elementos atmosféricos, os quais constituem os dados básicos para confecção de cartas de previsão do tempo, para conhecimento do clima, para a investigação de leis gerais que regem os fenômenos meteorológicos, etc. As observações devem ser feitas, invariavelmente, nas horas indicadas e sua execução terá lugar no menor tempo possível.
    É de capital importância prestar atenção a estas duas indicações porque o descuido das mesmas dará lugar, pela constante variação dos elementos, à obtenção de dados que, por serem tomados a distintas horas, não podem ser comparáveis. A definição acima, por si mesma, exclui qualquer possibilidade de informação com caráter de previsão de condições futuras do tempo por parte do observador. Com isso, deve ficar claro que o observador, ao preparar uma observação meteorológica, deverá se retringir a informar as condições de tempo reinantes no momento da observação. Não lhe é facultado informar o tempo que ocorrerá em momento futuro, mesmo que sua experiência e conhecimento profissionais lhe permita prever mudanças importantes no tempo.
    Finalidade e Importância:
    Nos serviços meteorológicos, estas observações têm a finalidade, entre outras, de informar aos meteorologistas nos centros de previsão, a situação e as mudanças de tempo que estão ocorrendo nas diferentes estações meteorológicas; obter dados unitários para fins de estatísticas meteorológicas e climatológicas; fazer observações meteorológicas para cooperação com outros serviços de meteorologia e difusão internacional. Só pelas finalidades acima, notamos a importância de se fazer às observações com o máximo de precisão e de honestidade.
    A Meteorologia básica, como o próprio nome sugere, nos fornece uma visão mais simples dos fenômenos atmosféricos que ocorrem em nosso dia a dia. Baseados em observações, os elementos meteorológicos mais importantes do ar, a velocidade e direção do vento, tipo e quantidade de nuvens, podemos ter uma boa noção de como o tempo está se comportando num determinado instante e lugar.
    As leis físicas aplicadas à atmosfera podem explicar o "estado" dela. Mas o estado ou o tempo é o resultado, desses elementos e outros mais com a influência dos fatores astronômicos e fatores geográficos, podem estar distribuídos em um número infinito de padrões no espaço e no tempo e em constante modificação.
    A meteorologia engloba tanto tempo como clima, enquanto os elementos da meteorologia devem necessariamente estar incorporados na climatologia para torná-la significativa e científica. O tempo e o clima podem, juntos, ser considerados como conseqüência e demonstração da ação dos processos complexos na atmosfera, nos oceanos e na Terra.
    A Meteorologia no seu sentido mais amplo, é uma ciência extremamente vasta e complexa, pois a atmosfera é muito extensa, variável e sede de um grande número de fenômenos.
    '''


    texto.insert(INSERT,mon_str)

    texto.place(x=2,y=2)

    #this is only necessary in the Windows platform, and it makes images persistent
    recFrame.mainloop()


def ActionGotoMain(frame, window):
    frame.destroy()
    MainWindow(window)


def load_file():
    try:
        _chuva, _tempM, _tempm, _sol, _umidade, _vento, _data = bpt.insere_from_file(askopenfilename(title='Selecione o arquivo'))
        bpt.save_parameters(_chuva, _tempM, _tempm, _sol, _umidade, _vento, _data)
        messagebox.showinfo("Inserido", "Nova Database Inserida com Exito !")
    except:
        messagebox.showerror("Error!", "Database nao foi inserida com Exito!")


def load_bin():
    try:
        global infos
        _chuva, _tempM, _tempm, _sol, _umidade, _vento, _data = bpt.load_stuff(askopenfilename(title='Selecione o arquivo'))
        infos = [_chuva, _tempM, _tempm, _sol, _umidade, _vento, _data]
        messagebox.showinfo("Criado", "Database Carregada com Exito !")
    except:
        messagebox.showerror("Error!", "Database nao foi carregada com Exito!")


def AuxCenterWindow(window):
    """
    Centers the window

    Keyword arguments:
        window = Tk
    """

    window.update_idletasks()
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))


if __name__ == '__main__':

    w = Tk()
    #global B+TREES!!!!
    infos=[]
    #gloval escolhe consulta
    radio_box=0
    amount=StringVar()
    saida_FINAL=[]
    #global consulta1
    consulta1_s=0
    lista_cb=[]
    MAIOR=IntVar()
    MENOR=IntVar()

    VarEst= IntVar()
    VarData= IntVar()
    VarChuva= IntVar()
    VarTempM= IntVar()
    VarTempm= IntVar()
    VarSol= IntVar()
    VarUmi= IntVar()
    VarVento= IntVar()
    _1ent1=StringVar()
    _1ent2=StringVar()

    #global consulta2
    regiao_2=StringVar()
    consulta_2=StringVar()

    #global consulta3
    consulta_3=StringVar()
    Entrada4=StringVar()
    Entrada5=StringVar()

    #global dict
    dictionary=pickle.load(open('estacoes.dic','rb'))

    w.resizable(0, 0) # prevent resizing
    w.title("INMET - BD Facilitado")
    icon = PhotoImage(file='img/icon.gif')
    w.call('wm', 'iconphoto', w._w, icon)
    w["bg"] = "ghost white"
    w.geometry("941x621+200+200") # (width x height + leftMargin + topMargin) in pixels
    AuxCenterWindow(w)
    MainWindow(w)

    w.mainloop()
