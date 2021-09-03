MAX = "NBS999999999"
def lecheria(cordoba, santa_fe, entre_rios, stock):
    lote_Cor, gusto_Cor, cal_Cor, peso_Cor = lote_gusto_kcal_peso(cordoba)
    lote_SF, gusto_SF, cal_SF, peso_SF = lote_gusto_kcal_peso(santa_fe)
    lote_ER, gusto_ER, cal_ER, peso_ER = lote_gusto_kcal_peso(entre_rios)
    
    total_cordoba = 0
    total_SF = 0
    total_ER = 0
    
    produccion = {}
    
    while lote_Cor != MAX or lote_SF != MAX or lote_ER != MAX:
        men = min(lote_Cor, lote_SF, lote_ER)
        
        while lote_Cor == men and lote_Cor != MAX:
            total_cordoba += float(peso_Cor)
            if float(peso_Cor) >= 90:
                escribir_stock(lote_Cor, gusto_Cor, cal_Cor, peso_Cor, stock)
            produccion = diccionario_produccion(gusto_Cor, cal_Cor, produccion)
            lote_Cor, gusto_Cor, cal_Cor, peso_Cor = lote_gusto_kcal_peso(cordoba)
            
        while lote_SF == men and lote_SF != MAX:
            total_SF += float(peso_SF)
            if float(peso_SF) >= 90:
                escribir_stock(lote_SF, gusto_SF, cal_SF, peso_SF, stock)
            produccion = diccionario_produccion(gusto_SF, cal_SF, produccion)
            lote_SF, gusto_SF, cal_SF, peso_SF = lote_gusto_kcal_peso(santa_fe)
            
        while lote_ER == men and lote_ER != MAX:
            total_ER += float(peso_ER)
            if float(peso_ER) >= 90:
                escribir_stock(lote_ER, gusto_ER, cal_ER, peso_ER, stock)
            produccion = diccionario_produccion(gusto_ER, cal_ER, produccion)
            lote_ER, gusto_ER, cal_ER, peso_ER = lote_gusto_kcal_peso(entre_rios)
            
    print('\n',"Peso producido en Cordoba:", total_cordoba,'\n',
          "Peso producido en Entre Rios:", total_ER,'\n', 
          "Peso producido en Santa Fe:", total_SF)
    
    return produccion
            
        
def lote_gusto_kcal_peso(archivo):
    linea = archivo.readline().rstrip('\n')
    registro = []
    if linea == '':
        registro = [MAX, 0, 0, 0]
    else: registro = linea.split(',')
    return registro

def escribir_stock(lote, gusto, cal, peso, archivo):
    archivo.write(lote +','+ gusto + ',' + cal + ','+ peso+'\n')
    
def diccionario_produccion(gusto, calorias, diccionario):
    clave = gusto +' '+calorias
    if clave in diccionario:
        diccionario[clave] += 1
    else:
        diccionario[clave] = 1
        
    return diccionario

def diccionario_lista_ord(diccionario):
    lista = list(diccionario.items())
    lista.sort(key = lambda x:x[1], reverse = True)
    return lista

def escribir_produccion(lista, archivo):
    for producto in lista:
        archivo.write(str(producto[0])+','+str(producto[1])+'\n')
    return archivo
    

def main(cordoba, entre_rios, santa_fe, stock, produccion):
    cor = open(cordoba)
    er = open(entre_rios)
    sf = open(santa_fe)
    stock = open(stock, 'w')
    prd = open(produccion, 'w')
    dic_prod = lecheria(cor, sf, er, stock)
    lista_prod = diccionario_lista_ord(dic_prod)   
    escribir_produccion(lista_prod, prd)
    cor.close()
    er.close()
    sf.close()
    stock.close()
    prd.close()
    
    
main(".\CB.csv", ".\ER.csv", ".\SF.csv", ".\STOCK.csv", ".\PRODUCCION.csv")
    
    