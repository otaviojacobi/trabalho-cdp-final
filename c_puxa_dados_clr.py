#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import os

pt1="http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt.php?&mRelEstacao="
datai='01/01/2015'
dataf='31/12/2015'
pt2="&btnProcesso=serie&mRelDtInicio=" + datai + "&mRelDtFim="+ dataf + "&mAtributos=,,1,1,,,,,,1,1,,,,1,1,"

arquivo=open('estacoes.txt')

estados={}

for line in arquivo:
    line=line.split('-')
    try:
        estados[line[-1].strip('\n ')].append([line[0].strip(' '), line[1].strip(' ')])
    except KeyError:
        estados[line[-1].strip('\n ')]=[[line[0].strip(' '), line[1].strip(' ')]]

inicial="http://www.inmet.gov.br/projetos/rede/pesquisa/gera_serie_txt.php?&mRelEstacao=83364&btnProcesso=serie&mRelDtInicio=21/12/2014&mRelDtFim=21/12/2015&mAtributos=,,,,,,,,,,1,,,,,,"
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get(inicial)
login = driver.find_element_by_name("mCod")
login.clear()
login.send_keys('leivascmpa@hotmail.com')
senha = driver.find_element_by_name("mSenha")
senha.clear()
senha.send_keys('g1qkjc7q')
botao=driver.find_element_by_name("btnProcesso").click()

fopen = open('dados.csv', 'w')
fopen.write('Estacao;Data;Hora;Precipitacao;TempMaxima;TempMinima;Insolacao;Umidade Relativa Media;Velocidade do Vento Media;\n'.replace(';', ',').encode('utf8'))
for estado in estados.keys():
    lista_de_links=[]
    for cidades in estados[estado]:
        lista_de_links.append(pt1 + str(cidades[0]) + pt2)
    for link in lista_de_links:
        driver.get(link)
        texto=driver.find_element_by_xpath("html").text
        if texto[0]!='N':
            texto=texto.split('\n')

            texto = '\n'.join(texto[17:])
            fopen.write(texto.replace(';',',').encode('utf8'))

            fopen.write('\n')
    fopen.write('\n')

fopen.close()
driver.close()

fopen=open('dados.csv', 'r')
clear=open('dados_clr.csv', 'w')
clear.write('Estacao,Data,Precipitacao,TempMaxima,TempMinima,Insolacao,Umidade Relativa Media,Velocidade do Vento Media,\n')
lista_de_elementos=[]
for line in fopen:
    lista_de_elementos.append(line)

for i in range(len(lista_de_elementos)-1):
    if 'E' not in lista_de_elementos[i]:
        al = lista_de_elementos[i].split(',')
        bl = lista_de_elementos[i+1].split(',')

        if al[0]==bl[0] and al[1]==bl[1]:
            saida=al[0:2] + [bl[3]] + [al[4]] +[bl[5]] + al[6:-1]
            clear.write(','.join(saida)+'\n')

clear.close()
fopen.close()
os.remove('dados.csv')
