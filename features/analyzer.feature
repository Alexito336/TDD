Feature: Analizador de Calificaciones
  Como desarrollador de software
  Quiero analizar un listado de calificaciones escolares
  Para obtener metricas estadisticas precisas y filtrar alumnos.

  Scenario Outline: Calcular estadisticas basicas y filtros
    Given una lista de calificaciones <lista_entrada>
    When se procesan las estadisticas completas
    Then el promedio debe ser <prom_esp>
    And la mediana debe ser <med_esp>
    And la moda debe ser <moda_esp>
    And la lista de aprobados con minimo sesenta debe ser <aprob_esp>
    And la lista de reprobados con minimo sesenta debe ser <reprob_esp>

    Examples:
      | lista_entrada           | prom_esp | med_esp | moda_esp | aprob_esp     | reprob_esp |
      | []                      | 0.0      | 0.0     | []       | []            | []         |
      | [85]                    | 85.0     | 85.0    | [85]     | [85]          | []         |
      | [70,80,90,100]          | 85.0     | 85.0    | [70,80,90,100] | [70,80,90,100] | []   |
      | [10,20,30]              | 20.0     | 20.0    | [10,20,30] | []          | [10,20,30] |
      | [10,20,20,30,40]        | 24.0     | 20.0    | [20]     | []            | [10,20,20,30,40] |
      | [60]                    | 60.0     | 60.0    | [60]     | [60]          | []         |
      | [80.5,90.25,75.0]       | 81.92    | 80.5    | [75.0,80.5,90.25] | [80.5,90.25,75.0] | [] |

  Scenario Outline: Validar calificaciones fuera de rango permitido
    Given una lista con valores invalidos <lista_invalida>
    When se intenta validar el listado
    Then se debe lanzar una excepcion de valor invalido

    Examples:
      | lista_invalida |
      | [-5,80,90]     |
      | [105,70,60]    |
