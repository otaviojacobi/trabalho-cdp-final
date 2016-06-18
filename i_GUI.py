#!/usr/bin/env python3
from tkinter import *
import tkinter.filedialog as fdialog
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
from functools import partial
from tkinter.filedialog import askopenfilename
import e_bplustree_to_file as bpt
from g_buscas import *


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

    Estacao=Checkbutton(introFrame, variable=VarEst,text="Estacao", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
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

    #buttons
    bt1 = Button(introFrame,command=partial(fazBusca,introFrame,window),relief = RAISED, width=13,font = "Arial 14 bold", text="Fazer Consulta", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')
    bt2 = Button(introFrame,command=load_file, width=13,relief = RAISED, font = "Arial 14 bold", text="Incluir nova DB", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')
    bt3 = Button(introFrame,command=load_bin, relief = RAISED, width=13,font = "Arial 14 bold", text="Carregar .bin", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')

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

#def updateList(lista_de_flags):


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
            saida_FINAL=consulta1(consulta1_s,infos,_1ent1.get(),_1ent2.get(),lista,quantidade=int(amount.get()))
            print(saida_FINAL)
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
            saida_FINAL=consulta2(a,infos,regiao_2.get().lower(),dictionary,quantidade=int(amount.get()))
            print(saida_FINAL)
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
            saida_FINAL=consulta3(a,infos,int(Entrada4.get()),int(Entrada5.get()),quantidade=int(amount.get()))
            print(saida_FINAL)




    except:
        messagebox.showerror("Error!", "Algum errou aconteceu, tente reiniciar !")


    recFrame.mainloop()

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
