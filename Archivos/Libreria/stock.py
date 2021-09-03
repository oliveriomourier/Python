MAX = 99999999999999
ISBN = 0
TITULO = 1
DIA = 1
STOCK = 2
VENTAS = 2
PRECIO = 3

def leer_archivo(archivo):
    linea = archivo.readline().rstrip('\n')
    if linea:
        registro = linea.split(',')
    else: 
        registro = [MAX, MAX, MAX]
    
    return registro

def leer_stock(archivo):
    linea = archivo.readline().rstrip('\n')
    if linea:
        registro = linea.split(',')
    else: 
        registro = [MAX, MAX, MAX, MAX]
    
    return registro

def escribir_archivo(archivo, isbn, titulo, stock, precio):
    archivo.write(str(isbn)+', '+str(titulo)+', '+str(stock)+', '+str(precio)+'\n')
    
def diccionario_libros(dic, isbn, ventas):
    tipo = ''
    if isbn[10:12] == '01':
        tipo = 'tapa dura'
    elif isbn[10:12] == '02':
        tipo = "tapa blanda"
    else:
        tipo = "edicion bolsillo"
        
    if tipo in dic:
        dic[tipo] += int(ventas)
    else:
        dic[tipo] = int(ventas)
        
    return dic

def diccionario_recaudacion(dic, dia, recaudacion):
    if dia in dic:
        dic[dia] += int(recaudacion)
    else:
        dic[dia] = int(recaudacion)
        
    return dic

def corte(arch1, arch2, arch3, stock, stock_act):
    a1 = leer_archivo(arch1)
    a2 = leer_archivo(arch2)
    a3 = leer_archivo(arch3)
    estock = leer_stock(stock)
    
    dic_recaudacion = {}
    dic_ventas_libros = {}
    
    while int(a1[ISBN]) != MAX or int(a2[ISBN]) != MAX or int(a3[ISBN]) != MAX:
        men = min(int(a1[ISBN]), int(a2[ISBN]), int(a3[ISBN]))
        
        while int(estock[ISBN]) < men:
            escribir_archivo(stock_act, estock[ISBN], estock[TITULO], estock[STOCK], estock[PRECIO])
            estock = leer_stock(stock)
            
        stock_actual = int(estock[STOCK])
        precio = int(estock[PRECIO])
        
        if men == int(a1[ISBN]):
            while men == int(a1[ISBN]):
                recaudacion = int(a1[VENTAS]) * precio
                stock_actual -= int(a1[VENTAS])
                dic_recaudacion = diccionario_recaudacion(dic_recaudacion, a1[DIA], recaudacion)
                dic_ventas_libros = diccionario_libros(dic_ventas_libros, a1[ISBN], a1[VENTAS])
                a1 = leer_archivo(arch1)
                
        if men == int(a2[ISBN]):
            while men == int(a2[ISBN]):
                recaudacion = int(a2[VENTAS]) * precio
                stock_actual -= int(a2[VENTAS])
                dic_recaudacion = diccionario_recaudacion(dic_recaudacion, a2[DIA], recaudacion)
                dic_ventas_libros = diccionario_libros(dic_ventas_libros, a2[ISBN], a2[VENTAS])
                a2 = leer_archivo(arch2)
                
        if men == int(a3[ISBN]):
            while men == int(a3[ISBN]):
                recaudacion = int(a3[VENTAS]) * precio
                stock_actual -= int(a3[VENTAS])
                dic_recaudacion = diccionario_recaudacion(dic_recaudacion, a3[DIA], recaudacion)
                dic_ventas_libros = diccionario_libros(dic_ventas_libros, a3[ISBN], a3[VENTAS])
                a3 = leer_archivo(arch3)
                
       
        escribir_archivo(stock_act, estock[ISBN], estock[TITULO], stock_actual, precio)
        estock = leer_stock(stock)
        
    return dic_recaudacion, dic_ventas_libros


def ordenar_lista(diccionario):
    lista = list(diccionario.items())
    lista.sort(key = lambda x:x[1], reverse = True)
    
    for elemento in lista:
        print(elemento[0], elemento[1])
        
    
def imprimir_recaudacion(dic):
    total = 0
    lista = list(dic.items())
    lista.sort(key = lambda x:x[1], reverse = True)
    for elemento in lista:
        print("dia", elemento[0], "se recaudó:", elemento[1])
        total += elemento[1]
        
    print("----------------")
    print("El total de la recaudacion fue:", total)
        
def main(a1, a2, a3, stock, stock_new):
    ar1 = open(a1)
    ar2 = open(a2)
    ar3 = open(a3)
    estock = open(stock)
    estock_new = open(stock_new, 'w')
    dic_recaudacion, dic_ventas_libros = corte(ar1,ar2, ar3, estock, estock_new)
    imprimir_recaudacion(dic_recaudacion)
    print("----------------")
    ordenar_lista(dic_ventas_libros)
    ar1.close()
    ar2.close()
    ar3.close()
    estock.close()
    estock_new.close()
    
    
main("./v1.txt","./v2.txt", "./v3.txt", "./stock.txt", "./stock_actualizado.txt")
        