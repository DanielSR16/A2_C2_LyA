from audioop import add
import csv
from queue import PriorityQueue
import string



 
# def filt(word):
#     return unicodedata.normalize('NFKD', word).encode('ascii', errors='ignore').decode('ascii')
mayusculas = list(string.ascii_uppercase)
minusculas = list(string.ascii_lowercase)

listLetra = minusculas + mayusculas
listNumeros = ['1','2','3','4','5','6','7','8','9','0']
with open('datos.csv', newline='') as File:  
    reader = csv.reader(File)
    auxLit = []
    ListaTotalDatos = []
    for row in reader:
        for datos in row:
                auxLit.append(datos)
        ListaTotalDatos.append(auxLit)
        auxLit = []  
 
    ListaTotalDatos[0][19] = 'enteroSuperPequeño'
    ListaTotalDatos[0][20] = 'enteroPequeño'
    ListaTotalDatos[0][29] = 'año'
    ListaTotalDatos[0][30] = 'textoPequeño'
    ListaTotalDatos[0][6] = 'a...z|A...Z'


    ListaTotalDatos[12][19] = 'enteroSuperPequeño'
    ListaTotalDatos[12][20] = 'enteroPequeño'
    ListaTotalDatos[12][29] = 'año'
    ListaTotalDatos[12][30] =  'textoPequeño'
    ListaTotalDatos[7][6] = 'a...z|A...Z'

    print(ListaTotalDatos[0][7])
    # for i in ListaTotalDatos[] 

def metodos_sintantico(valoresBuscar):
    apuntador = 0
    entrada = valoresBuscar
    pila = ['ENTRADAS','$']
    primeroPila = pila[0]
    while(primeroPila != '$'):

        primeroPila = pila[0]
        simboloApuntado = entrada[apuntador]
        encuentra_terminales = primeroPila in ListaTotalDatos[0]
        print('PRIMERO EN LA PILA: ',primeroPila)
        print('APUNTADOR: ',simboloApuntado)
        if primeroPila == 'vacio':
                print('entre a vacio')
                pila.pop(0)
                # apuntador = apuntador + 1
                print('pila depues de vacio = ',pila)
        elif encuentra_terminales == True or primeroPila == '$':

            if primeroPila == 'a...z|A...Z':
                in_listaLetra =  simboloApuntado in listLetra
                if in_listaLetra == True:
                    pila.pop(0)
                    apuntador = apuntador + 1
            elif primeroPila == '0...9':
                in_listaNumeros = simboloApuntado in listNumeros
                if in_listaNumeros == True:
                    pila.pop(0)
                    apuntador = apuntador + 1
         
            elif primeroPila == simboloApuntado:
                pila.pop(0)
                apuntador = apuntador + 1
            else:
                print('ERROR')
                break
        elif encuentra_terminales == False:
            fila = buscarFila(primeroPila)
            columna = buscarColumna(simboloApuntado)
            print('FILA: ',fila)
            print('COLUMNA: ',columna)
            datoAddPila = ListaTotalDatos[fila][columna]
            
            # print(datoAddPila)
            listaAddPila = datoAddPila.split()
            # print(listaAddPila)
            pila.pop(0)
            listaAddPila.extend(pila)
            pila = listaAddPila
            print(pila)
            # regla = 



        
def buscarFila(valor_pila):
    # posicionFila = 0
    for i in range(1,len(ListaTotalDatos)-1):
        # print(i)
        if ListaTotalDatos[i][0] == valor_pila:
            posicionFila = i
    return posicionFila   

def buscarColumna(simboloApuntado:str):
    simboloBuscar = ''
    # print('soy el simbolo',simboloApuntado)
    letra = False
    if(len(simboloApuntado) == 1 and simboloApuntado.isalpha() == True):

        letra = True
    numero = simboloApuntado.isdigit()
    if letra == True:
        simboloBuscar = 'a...z|A...Z'
    elif numero == True:
        simboloBuscar == '0..9'
    else:
         simboloBuscar = simboloApuntado

    for x in range(1,len(ListaTotalDatos[0])-1):
        # print(x)
        # print(ListaTotalDatos[0][x] )
        if ListaTotalDatos[0][x] == simboloBuscar:
            # print('simbolo en columa: ',ListaTotalDatos[0][x])
            # print('simbolo a buscar: ',simboloBuscar)
            posicionColumna = x
    return posicionColumna
        
         


# def string_to_list(string):

#     listAux = []
#     listaTotal = []
#     for i in range(0,len(string)):
#         if string[i]!= ' ' or len(string) != i:
#             listAux.append(string[i])

#         elif string[i] == ' ' or len(string) == i:
#             listaTotal.reverse

    



