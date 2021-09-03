MAX = "999999999"
DNI = 0
LAB = 1
LOTE = 2
DOSIS = 3

def leer_linea(archivo):
    linea = archivo.readline().rstrip('\n')
    if linea:
        registro = linea.split(',')
    else:
        registro = [MAX, MAX, MAX, MAX]
    
    return registro


def escribir_archivo(archivo, dni, lab, lote, nro_dosis):
    archivo.write(str(dni)+', '+str(lab)+', '+str(lote)+', '+str(nro_dosis)+'\n')

    
def actualizar_dic(dic, lab, nro_dosis):
    if lab in dic:
        dic[lab] += 1
    else:
        dic[lab] = 1            
    
    return dic


def corte(vacunados_1, vacunados_2, vacunados_totales):
    
    vac_1 = leer_linea(vacunados_1)
    vac_2 = leer_linea(vacunados_2)
    
    labos_1_dosis = {}
    labos_2_dosis = {}
    cont_vac_1 = 0
    cont_vac_2 = 0
    
    while vac_1[DNI] != MAX or vac_2[DNI] != MAX:
        
        men = min(vac_1[DNI], vac_2[DNI])
        
        while int(vac_1[DNI]) == int(vac_2[DNI]) and (int(vac_1[DNI]) != MAX or int(vac_2[DNI]) != MAX):
            if int(vac_1[DOSIS]) == 1:
                escribir_archivo(vacunados_totales, vac_1[DNI], vac_1[LAB], vac_1[LOTE], vac_1[DOSIS])
                labos_1_dosis = actualizar_dic(labos_1_dosis, vac_1[LAB], vac_1[DOSIS])
                escribir_archivo(vacunados_totales, vac_2[DNI], vac_2[LAB], vac_2[LOTE], vac_2[DOSIS])
                labos_2_dosis = actualizar_dic(labos_2_dosis, vac_2[LAB], vac_2[DOSIS])
            else:
                escribir_archivo(vacunados_totales, vac_2[DNI], vac_2[LAB], vac_2[LOTE], vac_2[DOSIS])
                labos_1_dosis = actualizar_dic(labos_1_dosis, vac_2[LAB], vac_2[DOSIS])
                escribir_archivo(vacunados_totales, vac_1[DNI], vac_1[LAB], vac_1[LOTE], vac_1[DOSIS])
                labos_2_dosis = actualizar_dic(labos_2_dosis, vac_1[LAB], vac_1[DOSIS])
                
            cont_vac_1 += 1
            cont_vac_2 += 1
            vac_1 = leer_linea(vacunados_1)
            vac_2 = leer_linea(vacunados_2)
            
        
        while men == vac_1[DNI]:
            escribir_archivo(vacunados_totales, vac_1[DNI], vac_1[LAB], vac_1[LOTE], vac_1[DOSIS])
            if int(vac_1[DOSIS]) == 1:
                labos_1_dosis = actualizar_dic(labos_1_dosis, vac_1[LAB], vac_1[DOSIS])
                cont_vac_1 += 1
            else:
                labos_2_dosis = actualizar_dic(labos_2_dosis, vac_1[LAB], vac_1[DOSIS])
                cont_vac_2 += 1
                    
            vac_1 = leer_linea(vacunados_1)
                
        
        while men == vac_2[DNI]:
            escribir_archivo(vacunados_totales, vac_2[DNI], vac_2[LAB], vac_2[LOTE], vac_2[DOSIS])
            if int(vac_2[DOSIS]) == 1:
                labos_1_dosis = actualizar_dic(labos_1_dosis, vac_2[LAB], vac_2[DOSIS])
                cont_vac_1 += 1
            else:
                labos_2_dosis = actualizar_dic(labos_2_dosis, vac_2[LAB], vac_2[DOSIS])
                cont_vac_2 += 1
                    
            vac_2 = leer_linea(vacunados_2)
                
    return labos_1_dosis, labos_2_dosis, cont_vac_1, cont_vac_2


def diccionario_lista_ordenada(dic):
    lista = list(dic.items())
    lista.sort(key = lambda x:x[1], reverse = True)
    
    return lista

def imprimir(lista, cont_vac_1, nro_vacuna):
    print("Los resultados de la", nro_vacuna, "vacuna:")
    for element in lista:
        porcentaje = element[1] / cont_vac_1
        print("El laboratorio", element[0], "tiene un porcentaje de:", str(porcentaje *100), "%")
        
    
def main(vacunas_1, vacunas_2, vacunas_total):
    vac_1 = open(vacunas_1)
    vac_2 = open(vacunas_2)
    vac_total = open(vacunas_total, 'w')
    lab_1, lab_2, cont_1, cont_2 = corte(vac_1, vac_2, vac_total)
    lab_1_ordenado = diccionario_lista_ordenada(lab_1)
    lab_2_ordenado = diccionario_lista_ordenada(lab_2)
    imprimir(lab_1_ordenado, cont_1, "primer")
    print("------------")
    imprimir(lab_2_ordenado, cont_2, "segunda")
    vac_1.close()
    vac_2.close()
    vac_total.close()
        

main("./vacunas_1.txt", "./vacunas_2.txt", "./vacunas_totales.txt")
                
                
                
