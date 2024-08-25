from models.TablaSimplex import TablaSimplex
from copy import deepcopy

def fillBasic(basic:list[int]) -> list[int]:
    result: list[int] = []
    for b in range(len(basic)):
        result.append(len(basic) + b -1)
    return result

def fillObjetivo(objetivo: list[float] , length: int) -> list[float]:
    result: list[float] = []
    for i in range(length):
        if i<len(objetivo):
            result.append(-objetivo[i])
        else:
            result.append(0)
    return result


def solve_metodo_simplex(tabla:TablaSimplex) -> list[TablaSimplex]:
    newTabla: TablaSimplex = TablaSimplex(matriz = tabla.matriz, objetivo = fillObjetivo(tabla.objetivo,len(tabla.matriz[0])), basic= fillBasic(tabla.basic) , restricciones= tabla.restricciones)
    result: list[TablaSimplex] = [deepcopy(newTabla)]
    solucion: bool = False
    objetivo = newTabla.model_copy().objetivo
    basic = newTabla.model_copy().basic
    restricciones = newTabla.model_copy().restricciones
    print(f"Tabla inicial: {newTabla}")
    print(30*"-")
    while not solucion:
        min_objetivo= min(objetivo)
        min_row = objetivo.index(min_objetivo)
        matriz = deepcopy(result[-1]).matriz
        min_col = 0
        min_division = 10**8
        for i in range(len(matriz)):
            if(matriz[i][min_row] != 0 and min_division > restricciones[i] / matriz[i][min_row]):
                min_division = restricciones[i]/matriz[i][min_row]
                min_col = i
        print(f"Las coordenadas del pivote: col:{min_col}, row:{min_row}")
        pivot = matriz[min_col][min_row]
        print(f"Pivote {pivot}")
        for i in range(len(matriz[min_col])):
            matriz[min_col][i] /= pivot
        restricciones[min_col] /= pivot
        print(f"Columna pivote {matriz[min_col]}")
        for j in range(len(matriz[0])):
                    objetivo[j] -= (objetivo[min_row] * matriz[min_col][j])
        for i in range(len(matriz)):
            
            if i == min_col:
                continue
            col_pivot = matriz[i][min_row]
            for j in range(len(matriz[i])):
                matriz[i][j] -= (col_pivot * matriz[min_col][j])
            restricciones[i] -= (col_pivot * restricciones[min_col])
        basic[min_col] = min_row
        result.append(TablaSimplex(
            matriz= matriz.copy(),
            basic= basic.copy(),
            restricciones= restricciones.copy(),
            objetivo = objetivo.copy(),
        ))
        solucion = len(list(filter(lambda x: (x<0),objetivo))) == 0
        print(30*"-")
    return result

