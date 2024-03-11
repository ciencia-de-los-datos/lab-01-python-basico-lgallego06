"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    ruta_archivo='data.csv'
    suma_columna=0
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            valor_columna=int(campos[1])
            suma_columna += valor_columna
    print(suma_columna)
    return suma_columna
#pregunta_01()

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    ruta_archivo='data.csv'
    conteo_letras={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            letra=campos[0][0] 
            conteo_letras[letra] = conteo_letras.get(letra, 0) + 1
    lista_tuplas=sorted(conteo_letras.items())
    print(lista_tuplas)
    return lista_tuplas
#pregunta_02()


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    ruta_archivo='data.csv'
    suma_por_letra={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            letra= campos[0][0]
            valor_columna_2=int(campos[1])
            suma_por_letra[letra]=suma_por_letra.get(letra,0)+valor_columna_2
    lista_tuplas=sorted(suma_por_letra.items())
    print(lista_tuplas)
    return lista_tuplas
#pregunta_03()


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    ruta_archivo='data.csv'
    registro_por_mes={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            mes=campos[2][5:7]
            registro_por_mes[mes]=registro_por_mes.get(mes,0)+1
    lista_tuplas=sorted(registro_por_mes.items())
    print(lista_tuplas)
    return lista_tuplas
#pregunta_04()



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    ruta_archivo='data.csv'
    maximo_minimo_letras={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            letra=campos[0]
            valor_columna_2=int(campos[1])
            if letra not in maximo_minimo_letras:
               maximo_minimo_letras[letra]={'maximo': valor_columna_2,'minimo': valor_columna_2}
            else:
                maximo_minimo_letras[letra]['maximo'] = max(maximo_minimo_letras[letra]['maximo'], valor_columna_2)
                maximo_minimo_letras[letra]['minimo'] = min(maximo_minimo_letras[letra]['minimo'], valor_columna_2)
    lista_maximo_minimo=[(letra, valores['maximo'], valores['minimo']) for letra, valores in maximo_minimo_letras.items()]
    lista_maximo_minimo=sorted(lista_maximo_minimo)
    print(lista_maximo_minimo)
    return lista_maximo_minimo
#pregunta_05()

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    ruta_archivo='data.csv'
    valores_extremos={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            diccionario=campos[4].split(',')
            for item in diccionario:
                clave, valor=item.split(':')
                valor=int(valor)
                if clave not in valores_extremos:
                    valores_extremos[clave]={'minimo':valor,'maximo':valor}
                else:
                    valores_extremos[clave]['minimo']=min(valores_extremos[clave]['minimo'],valor)
                    valores_extremos[clave]['maximo']=max(valores_extremos[clave]['maximo'],valor)
    lista_valores_extremos=[(clave,valores['minimo'],valores['maximo']) for clave, valores in valores_extremos.items()]         
    lista_valores_extremos=sorted(lista_valores_extremos)
    print(lista_valores_extremos)
    return lista_valores_extremos
#pregunta_06()

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    ruta_archivo='data.csv'
    valores_letras={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            valor_columna_2=int(campos[1])
            letra_columna_1=campos[0]
            if valor_columna_2 not in valores_letras:
                valores_letras[valor_columna_2]=[letra_columna_1]
            else: 
                valores_letras[valor_columna_2].append(letra_columna_1)
    lista_valores_letras=[(valor,letras) for valor, letras in valores_letras.items()]
    lista_valores_letras=sorted(lista_valores_letras)
    print(lista_valores_letras)
    return lista_valores_letras
#pregunta_07()

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    ruta_archivo='data.csv'
    valores_letras={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            valor_columna_2=int(campos[1])
            letra_columna_1=campos[0]
            if valor_columna_2 not in valores_letras:
                valores_letras[valor_columna_2]=[letra_columna_1]
            else:
                valores_letras[valor_columna_2].append(letra_columna_1)
    lista_tuplas=[(valor,sorted(set(letras))) for valor,letras in valores_letras.items()]
    lista_tuplas=sorted(lista_tuplas)
    print(lista_tuplas)
    return lista_tuplas
#pregunta_08()



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    ruta_archivo='data.csv'
    conteo_claves={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            columna5=campos[4].split(',')
            for item in columna5:
                clave, _=item.split(':')
                conteo_claves[clave]=conteo_claves.get(clave,0)+1
    conteo_claves = {k: v for k, v in sorted(conteo_claves.items())}
    print(conteo_claves)
    return conteo_claves
#pregunta_09()


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    ruta_archivo='data.csv'
    lista_tuplas=[]
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            letra=campos[0]
            elementos_columna_4=len(campos[3].split(','))
            elementos_columna_5=len(campos[4].split(','))
            lista_tuplas.append((letra,elementos_columna_4,elementos_columna_5))
            print(lista_tuplas)
    return lista_tuplas
#pregunta_10()

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    ruta_archivo='data.csv'
    suma_letra_4={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            letras_4=campos[3].split(',')
            suma_columna_2=int(campos[1])
            for letra in letras_4:
                suma_letra_4[letra]=suma_letra_4.get(letra,0)+suma_columna_2
    suma_letra_4={k:suma_letra_4[k] for k in sorted(suma_letra_4)}
    print(suma_letra_4)
    return suma_letra_4
#pregunta_11()

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    ruta_archivo='data.csv'
    suma_letra={}
    with open(ruta_archivo,'r') as file:
        for line in file:
            campos=line.strip().split('\t')
            letra=campos[0]
            valores_columna_5=campos[4].split(',')
            suma_columna_5=sum(int(valor.split(':')[1]) for valor in valores_columna_5)
            if letra in suma_letra:
                suma_letra[letra]+=suma_columna_5
            else:
                suma_letra[letra]=suma_columna_5
    suma_letra={k:suma_letra[k] for k in sorted(suma_letra)}
    print(suma_letra)
    return suma_letra
#pregunta_12()
