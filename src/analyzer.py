from collections import Counter

def validar_calificaciones(calificaciones):
    if not isinstance(calificaciones, list):
        raise TypeError("Debe ser una lista de números")
    for c in calificaciones:
        if not (0 <= c <= 100):
            raise ValueError("Calificación fuera de rango (0-100)")

def promedio(calificaciones):
    validar_calificaciones(calificaciones)
    if not calificaciones:
        return 0.0
    return round(sum(calificaciones) / len(calificaciones), 2)

def mediana(calificaciones):
    validar_calificaciones(calificaciones)
    if not calificaciones:
        return 0.0
    ordenadas = sorted(calificaciones)
    n = len(ordenadas)
    mitad = n // 2
    if n % 2 == 0:
        return round((ordenadas[mitad - 1] + ordenadas[mitad]) / 2, 2)
    return round(ordenadas[mitad], 2)

def moda(calificaciones):
    validar_calificaciones(calificaciones)
    if not calificaciones:
        return []
    conteo = Counter(calificaciones)
    max_frecuencia = max(conteo.values())
    modas = [num for num, frec in conteo.items() if frec == max_frecuencia]
    return sorted(modas)

def aprobados(calificaciones, minimo=60):
    validar_calificaciones(calificaciones)
    return [c for c in calificaciones if c >= minimo]

def reprobados(calificaciones, minimo=60):
    validar_calificaciones(calificaciones)
    return [c for c in calificaciones if c < minimo]

def estadisticas_completas(calificaciones):
    return {
        "promedio": promedio(calificaciones),
        "mediana": mediana(calificaciones),
        "moda": moda(calificaciones),
        "aprobados": aprobados(calificaciones),
        "reprobados": reprobados(calificaciones)
    }
