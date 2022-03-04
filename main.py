from dataclasses import replace
from hashlib import new
from json import tool
from operator import le
from posixpath import split
import sys
from tokenize import String
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from tabla import *
import string
from sintactico import metodos_sintantico

valor = ''
listaPrimaria = []
mayusculas = list(string.ascii_uppercase)
minusculas = list(string.ascii_lowercase)
letra = minusculas + mayusculas
print(string.ascii_uppercase)
print(string.ascii_lowercase)
encontrados = {
    'guion' : [],
    'dosPuntos' : [],
    'coma': [],
    'parentesis' : [],
    'palabraReservada':[],
    'valor' :[],
    'letra': [],
    'digito' : [],
    'error' : []
    }

tokens = {
    'guion' : ['-'],
    'dosPuntos' : [':'],
    'coma': [','],
    'parentesis' : ['(',')'],

'palabraReservada':['BaseDeDatos','NombreTabla','ListaCampo','LlavePrimaria','noVacio','incrementarse'],
    'valor' : ['entero','enteroSuperPequeño','enteroPequeño',
                         'fecha','fechaHora','hora','textoPequeño','texto','textoMediano','textoLargo','textoLargo','dobleFlotante',
                         'cadenaDefinida','cadena','enteroMediano','enteroGande','enteroDecimal','decimalDoble',
                         'decimal','año'],
    
    'letra': letra,
    'digito' : ['1','2','3','4','5','6','7','8','9','0']
    
}
listaEncontrados = []
auxListaEncontrado = []
encontradosString = []

encontradosValores = []
encontradosvalores_aux = []
encontrados_valores_String = []

class index(QMainWindow):
    def __init__(self,data):
        super().__init__()
        self.data = data
        uic.loadUi("vista3.ui", self)
        self.boton.clicked.connect(self.input_to_List)
        self.tablaW.setColumnWidth(0,1500)
        
       

    def input_to_List(self):
        listaPrimaria.clear()
    
        valor:str = self.input.toPlainText()
        newvaL =  valor.replace('\n','*')
        newvaL = newvaL + '*'
        lineaNombreAux = ''
        for i in newvaL:
            # print(i)
            if i != '*' :
                lineaNombreAux = lineaNombreAux + i
            elif i == '*':
                newNombre = lineaNombreAux.replace(' ','')
                listaPrimaria.append(newNombre)
                lineaNombreAux = ''

        validarTokens()
        self.cargarData()
        self.mostrarError()
        
    def mostrarError(self):
        self.error.setText('')
        stringError = ''
        if(len(encontrados['error'])>0):
            for i in encontrados['error']:
                stringError = stringError + i
            self.error.setText('Error encontrador en: ' + stringError)
        encontrados['error'] = []

    def cargarData(self):
        self.tablaW.setRowCount(len(encontradosString))
        for  i in range(0,len(encontradosString)):
            self.tablaW.setItem(i,0,QtWidgets.QTableWidgetItem(encontradosString[i]))
            
        
      
def validarTokens():
    errorSimbolo = False
    for numLinea in range(0,len(listaPrimaria)):
        # print(listaPrimaria)
        if errorSimbolo ==False:
            
            auxString = ''
            for valores in listaPrimaria[numLinea]:
                # print(valores)
                if valores != ':':
                    auxString = auxString + valores
            
                    if len(listaPrimaria[numLinea]) == len(auxString):
                        print('soy normal xd')
                        palabra = listaPrimaria[numLinea]
                        verificarTokens(palabra)
                        listaPrimaria[numLinea] = []
                elif  valores == ':' :
                    
                    existe_in_list_dosPuntos = ':' in encontrados['dosPuntos']
                    if( existe_in_list_dosPuntos == False):
                   
                        encontrados['dosPuntos'].append(':')

                    palabra = palabrasReservadas(auxString)
                    
                    if(palabra == 'BaseDeDatos'):

                        auxListaEncontrado.append('PalabraReservada')
                        auxListaEncontrado.append('dosPuntos')

                        encontradosvalores_aux.append('BaseDeDatos')
                        encontradosvalores_aux.append(':')
                        dataBD = listaPrimaria[numLinea][len(palabra)+1:len( listaPrimaria[numLinea])]
                        listaPrimaria[numLinea] = dataBD
                       
                   
                        verificarTokens(listaPrimaria[numLinea])
                        listaPrimaria[numLinea] = []

                    elif(palabra == 'NombreTabla'):
                        
                        auxListaEncontrado.append('PalabraReservada')
                        auxListaEncontrado.append('dosPuntos')

                        encontradosvalores_aux.append('NombreTabla')
                        encontradosvalores_aux.append(':')
                        
                        dataNT = listaPrimaria[numLinea][len(palabra)+1:len( listaPrimaria[numLinea])]
                        listaPrimaria[numLinea] = dataNT
                        verificarTokens(listaPrimaria[numLinea])
                        listaPrimaria[numLinea] = []
                        print('soy data tabala',dataNT)

                    elif(palabra == 'ListaCampo'):
                        auxListaEncontrado.append('PalabraReservada')
                        auxListaEncontrado.append('dosPuntos')

                        encontradosvalores_aux.append('ListaCampo')
                        encontradosvalores_aux.append(':')

                        dataLC = listaPrimaria[numLinea][len(palabra)+1:len( listaPrimaria[numLinea])]
                        listaPrimaria[numLinea] = dataLC
                        verificarTokensCampo(listaPrimaria[numLinea])
                        listaPrimaria[numLinea] = []
               
                    elif(palabra == 'LlavePrimaria'):
                        auxListaEncontrado.append('PalabraReservada')
                        auxListaEncontrado.append('dosPuntos')

                        encontradosvalores_aux.append('LlavePrimaria')
                        encontradosvalores_aux.append(':')

                        dataLP = listaPrimaria[numLinea][len(palabra)+1:len( listaPrimaria[numLinea])]
                        listaPrimaria[numLinea] = dataLP
                        verificarTokens(listaPrimaria[numLinea])
                        listaPrimaria[numLinea] = []
                 

                    else:
                        print('SoyNormal')
                        palabra = listaPrimaria[numLinea]
                        verificarTokens(palabra)
                        listaPrimaria[numLinea] = []
            listaAux= []
            listaAux.extend(auxListaEncontrado)
            listaEncontrados.append(listaAux)
            auxListaEncontrado.clear()

        
            # listaAux_valores = []
            # listaAux_valores.extend(encontradosvalores_aux)

            encontradosValores.extend(encontradosvalores_aux)


            # print(encontradosValores)

            

          
            # listaAux_valores.clear()
            encontradosvalores_aux.clear()

            if len(encontrados['error']) > 0:
               errorSimbolo = True
          
    # print('ListaEnocontrados')
    # print(listaEncontrados)
    listasToString()
    print(encontradosValores)
    metodos_sintantico(encontradosValores)

    # print(encontradosString)
    for borrarEncontrado in range(0,len(listaEncontrados)):
        listaEncontrados.pop()      
        encontradosValores.pop()


        



def palabrasReservadas (palabra):
    for reservadas in tokens['palabraReservada']:
        if(palabra == reservadas):
            existe_in_list_reservada = palabra in  encontrados['palabraReservada'] 
            if existe_in_list_reservada == False:
                encontrados['palabraReservada'].append(palabra)


    return palabra
#cadena(10)-noVacio-incrementarse,
def verificarTokens(palabra):
 
    for letra in palabra:
        
        bandera = False
        if letra in tokens['dosPuntos'] :
            auxListaEncontrado.append('DosPuntos')
            encontradosvalores_aux.append(':')
            bandera = True
        elif letra in tokens['coma']:
            auxListaEncontrado.append('coma')
            encontradosvalores_aux.append(',')
            bandera = True
        elif letra in tokens['parentesis']:
            auxListaEncontrado.append('parentesis')
            encontradosvalores_aux.append(letra)
    
            bandera = True
        elif letra in tokens['letra']:
            auxListaEncontrado.append('letra')
            encontradosvalores_aux.append(letra)
           
            bandera = True
        elif letra in tokens['digito']:
            auxListaEncontrado.append('digito')
            encontradosvalores_aux.append(letra)
    
            bandera = True
        elif letra in tokens['guion']:
            auxListaEncontrado.append('guion')
            encontradosvalores_aux.append(letra)
         
            bandera = True
            
        if bandera == False:
            auxListaEncontrado.append('error')
            
            encontrados['error'].append(letra)

        
def verificarTokensCampo(palabra):
    campoAux = ''
    for letra in palabra:
            if letra != '-' and letra != ',' and letra != '(' :
                # print(letra)
                campoAux = campoAux + letra
                # print(campoAux)
                if len(palabra) == len(campoAux):
                 
                    verificarTokens(campoAux)

    
            # print(letra)
            if letra == '-':
                print('raya')
                print(campoAux)
                
                existe_in_list_valor = campoAux in tokens['valor']

                existe_in_list_reservadas = campoAux in tokens['palabraReservada']
                if existe_in_list_valor == True:
                    auxListaEncontrado.append('valor')
                    auxListaEncontrado.append('guion')
                    encontradosvalores_aux.append(campoAux)
                    encontradosvalores_aux.append('-')

                elif existe_in_list_reservadas == True:
                    auxListaEncontrado.append('palabraReservada')
                    auxListaEncontrado.append('guion')
                    encontradosvalores_aux.append(campoAux)
                    encontradosvalores_aux.append('-')
                else:
                    verificarTokens(campoAux)
                    auxListaEncontrado.append('guion')
                    encontradosvalores_aux.append('-')
                campoAux = ''
            elif letra == '(':
                # print('parentesis')
                # print(campoAux)
                existe_in_list_reservadas1 = campoAux in tokens['valor']
               
                if existe_in_list_reservadas1 == True:
                    auxListaEncontrado.append('valor')
                    auxListaEncontrado.append('parentesis')

                    encontradosvalores_aux.append(campoAux)
                    encontradosvalores_aux.append('(')
                    

                else:
                    verificarTokens(campoAux)
                    auxListaEncontrado.append('parentesis')

                    encontradosvalores_aux.append('(')
                campoAux = ''
            
            elif letra == ',':
                print('coma')
                print(campoAux)
                existe_in_list_reservadas2 = campoAux in tokens['palabraReservada']
                existe_in_list_valores2 = campoAux in tokens['valor']
                # print(existe_in_list_reservadas2)
          
                if existe_in_list_reservadas2 == True:
                    auxListaEncontrado.append('palabraReservada')
                    auxListaEncontrado.append('coma')

                    encontradosvalores_aux.append(campoAux)
                    encontradosvalores_aux.append(',')
                elif existe_in_list_valores2 == True:
                    auxListaEncontrado.append('valor')
                    auxListaEncontrado.append('coma')

                    encontradosvalores_aux.append(campoAux)
                    encontradosvalores_aux.append(',')
                else:
                    verificarTokens(campoAux)
                    auxListaEncontrado.append('coma')
                    encontradosvalores_aux.append(',')

                campoAux = ''    
            elif letra == ')':
                    existe_in_list_reservadas1 = campoAux in tokens['valor']
                
                    if existe_in_list_reservadas1 == True:
                        auxListaEncontrado.append('valor')
                        auxListaEncontrado.append('parentesis')

                        encontradosvalores_aux.append(campoAux)
                        encontradosvalores_aux.append(')')
                        

                    else:
                        verificarTokens(campoAux)
                        auxListaEncontrado.append('parentesis')

                      
                    campoAux = ''
        


                        
def listasToString():
    auxEncontradosString = ''
    encontradosString .clear()

    for encontrado in listaEncontrados:
        for datos in encontrado:
            auxEncontradosString = auxEncontradosString + datos + ' '
        encontradosString.append(auxEncontradosString)
        # print(encontradosString)
        auxEncontradosString = ''

    
    # encontrados_valores_String.clear()
    auxEncontrados_valores_String = ''
    print
    # for encontrado_valor in encontradosValores:
    #     for datos_valor in encontrado_valor:
    #         auxEncontrados_valores_String = auxEncontrados_valores_String + datos_valor + ' '
    #     encontrados_valores_String.append(auxEncontrados_valores_String)
    #     print('a')
    #     print(encontrados_valores_String)
    #     auxEncontrados_valores_String = ''




                



        



    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index(['daniel','juan'])
    GUI.show()
    sys.exit(app.exec_())


    