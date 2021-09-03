MAX = "99999999999999"
FECHA = 0
ISBN = 1
SUCURSAL = 1
VENTAS = 2

def leer_archivo(archivo):
    linea = archivo.readline().rstrip('\n')
    if linea:
        registro = linea.split(',')
    else:
        registro = [MAX, MAX]
        
    return registro
                
   
def actualizar_diccionario(dic, isbn):
    if isbn in dic:
        dic[isbn] += 1
    else:
        dic[isbn] = 1
        
    return dic

def escribir_archivo(archivo, fecha, sucursal, total_ventas):
    archivo.write(str(fecha)+', '+str(sucursal)+', '+str(total_ventas)+'\n')
    
def primer_corte(avell, lom, temp, stock):
    avellaneda = leer_archivo(avell)
    lomas = leer_archivo(lom)
    temperley = leer_archivo(temp)
        
    dic_vtas = {}
    
    while avellaneda[FECHA] != MAX or lomas[FECHA] != MAX or temperley[FECHA] != MAX:
        men = min(avellaneda[FECHA], lomas[FECHA], temperley[FECHA])
        
        if men == avellaneda[FECHA]:
            ventas_dia = 0
            while avellaneda[FECHA] == men:
                ventas_dia += 1
                dic_vtas = actualizar_diccionario(dic_vtas, avellaneda[ISBN])
                avellaneda = leer_archivo(avell)
            escribir_archivo(stock, men, "avellaneda", ventas_dia)
            
        if men == lomas[FECHA]:
            ventas_dia = 0
            while lomas[FECHA] == men:
                ventas_dia += 1
                dic_vtas = actualizar_diccionario(dic_vtas, lomas[ISBN])
                lomas = leer_archivo(lom)
            escribir_archivo(stock, men, "lomas", ventas_dia)
            
        if men == temperley[FECHA]:
            ventas_dia = 0
            while temperley[FECHA] == men:
                ventas_dia += 1
                dic_vtas = actualizar_diccionario(dic_vtas, temperley[ISBN])
                temperley = leer_archivo(temp)
            escribir_archivo(stock, men, "temperley", ventas_dia)
                
    return dic_vtas


def segundo_corte(estock):
    stock = leer_archivo(estock)
    ventas_totales = 0
    
    while stock[FECHA] != MAX:
        print("En el dia:",stock[FECHA])
        fecha =  stock[FECHA]
        subtotal_ventas = 0
        while fecha == stock[FECHA] and stock[FECHA] != MAX:
            print("La sucursal", stock[SUCURSAL], "vendio", stock[VENTAS])
            subtotal_ventas += int(stock[VENTAS])
            stock = leer_archivo(estock)
        print("Se recaudo un total de:", str(subtotal_ventas))
        ventas_totales += subtotal_ventas
    
    print("En total se recaudó", str(ventas_totales))
          
    
    
def imprimir(dic):
    lista = list(dic.items())
    lista.sort(key = lambda x:x[1], reverse = True)
    
    for element in lista:
        print("El producto", element[0], "vendio", element[1], "productos")
    


def main(arch1, arch2, arch3, estock):
    a1 = open(arch1)
    a2 = open(arch2)
    a3 = open(arch3)
    stock = open(estock, 'w')
    dic_vts = primer_corte(a1, a2, a3, stock)
    stock.close()
    stock = open(estock)
    segundo_corte(stock)
    print("-------------")
    imprimir(dic_vts)
    a1.close()
    a2.close()
    a3.close()
    stock.close()
          
main("./avell.txt", "./lomas.txt", "./temp.txt", "./VENTAS.txt")
            