#!/usr/bin/env python3
from tkinter import *
import tkinter.filedialog as fdialog
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
from functools import partial
from tkinter.filedialog import askopenfilename
import e_bplustree_to_file as bpt


def MainWindow(window):

    #frame
    introFrame = Frame(window)
    introFrame.pack()

    # create the main logo
    bg = PhotoImage(file="img/inicial.gif")
    inicial = Label(introFrame, image=bg)
    inicial.pack()
    introFrame.option_add("*background", "#BBFFFF"),
    opcao = Label(introFrame, text="Selecione a opção: ", font = "Arial 12 bold")
    dataI = Label(introFrame, text="Data Inicial: ", font = "Arial 12 bold")
    dataF = Label(introFrame, text="Data Final: ", font = "Arial 12 bold")
    estds = Label(introFrame, text="Selecione uma região: ", font = "Arial 12 bold")
    qt = Label(introFrame, text="Quantidade: ", font = "Arial 12 bold")

    #textboxes
    introFrame.option_add("*background", "#FFFFFF"),
    ent1 = Entry(introFrame)
    ent2 = Entry(introFrame)
    qtbo = Entry(introFrame, width='12')

    #buttons
    bt1 = Button(introFrame, relief = RAISED, width=13,font = "Arial 14 bold", text="Fazer Consulta", fg="black", background="Sky blue", activebackground="Sky blue", cursor='hand1')
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
    combobox=ttk.Combobox(introFrame, state='readonly', font = "Arial 12 bold", values=[' ','Precipitação','TempMáxima', 'TempMínima', 'Insolação', 'Umidade Relativa Média', 'Velocidade do Vento Média'])
    combobox['width']= '25'
    combobox2=ttk.Combobox(introFrame, state='readonly', font = "Arial 12 bold",)
    combobox2['values']=['Todos','Sul', 'Sudeste', 'Centro-Oeste', 'Nordeste', 'Norte']
    combobox2['width']= '25'

    #checkboxes
    maior=Checkbutton(introFrame, text="Maior", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')
    menor=Checkbutton(introFrame, text="Menor", font="Arial 12 bold", background= "#E0FFFF", activebackground= "#E0FFFF",activeforeground="#00688B",cursor='hand1')

    opcao.place(x=80, y=150)
    dataI.place(x=338, y=150)
    dataF.place(x=338, y=210)
    ent1.place(x=338, y=175)
    ent2.place(x=338, y=235)
    estds.place(x=520, y=150)
    qt.place(x=770, y=150)
    qtbo.place(x=770, y=175)
    combobox.place(x=80,y=175)
    combobox2.place(x=520, y=175)
    btINMET.place(x=660, y=420)
    bt1.place(x=370, y=570)
    bt2.place(x=370, y=520)
    bt3.place(x=370, y=470)
    maior.place(x=80, y=210)
    menor.place(x=160, y=210)

    introFrame.mainloop()

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
    btReturn = Button(recFrame, text="↩", relief=GROOVE, command=partial(ActionGotoMain, recFrame, window), font="Courier 15 bold", background="PaleTurquoise1", activebackground="PaleTurquoise1")
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

    #global B+TREES!!!!
    infos=[]

    w = Tk()
    w.resizable(0, 0) # prevent resizing
    w.title("INMET - BD Facilitado")
    icon = PhotoImage(file='img/icon.gif')
    w.call('wm', 'iconphoto', w._w, icon)
    w["bg"] = "ghost white"
    w.geometry("941x621+200+200") # (width x height + leftMargin + topMargin) in pixels
    AuxCenterWindow(w)
    MainWindow(w)

    w.mainloop()
