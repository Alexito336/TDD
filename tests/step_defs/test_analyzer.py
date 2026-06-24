import pytest
import json
from pathlib import Path
from pytest_bdd import scenarios, given, when, then, parsers
from src import analyzer

BASE_DIR = Path(__file__).resolve().parent.parent.parent
FEATURE_FILE = BASE_DIR / "features" / "analyzer.feature"

scenarios(str(FEATURE_FILE))

@pytest.fixture
def contexto():
    return {}

@given(parsers.parse('una lista de calificaciones {lista_entrada}'), target_fixture='contexto_lista')
def una_lista_de_calificaciones(lista_entrada):
    return {"lista": json.loads(lista_entrada)}

@when('se procesan las estadisticas completas')
def se_procesan_las_estadisticas(contexto_lista):
    lista = contexto_lista["lista"]
    contexto_lista["res_promed"] = analyzer.promedio(lista)
    contexto_lista["res_median"] = analyzer.mediana(lista)
    contexto_lista["res_moda"] = analyzer.moda(lista)
    contexto_lista["res_aprob"] = analyzer.aprobados(lista, minimo=60)
    contexto_lista["res_reprob"] = analyzer.reprobados(lista, minimo=60)

@then(parsers.parse('el promedio debe ser {prom_esp}'))
def el_promedio_debe_ser(contexto_lista, prom_esp):
    assert contexto_lista["res_promed"] == float(prom_esp)

@then(parsers.parse('la mediana debe ser {med_esp}'))
def la_mediana_debe_ser(contexto_lista, med_esp):
    assert contexto_lista["res_median"] == float(med_esp)

@then(parsers.parse('la moda debe ser {moda_esp}'))
def la_moda_debe_ser(contexto_lista, moda_esp):
    assert contexto_lista["res_moda"] == json.loads(moda_esp)

@then(parsers.parse('la lista de aprobados con minimo sesenta debe ser {aprob_esp}'))
def la_lista_de_aprobados(contexto_lista, aprob_esp):
    assert contexto_lista["res_aprob"] == json.loads(aprob_esp)

@then(parsers.parse('la lista de reprobados con minimo sesenta debe ser {reprob_esp}'))
def la_lista_de_reprobados(contexto_lista, reprob_esp):
    assert contexto_lista["res_reprob"] == json.loads(reprob_esp)

@given(parsers.parse('una lista con valores invalidos {lista_invalida}'), target_fixture='contexto_invalido')
def una_lista_con_valores_invalidos(lista_invalida):
    return {"lista": json.loads(lista_invalida)}

@when('se intenta validar el listado')
def se_intenta_validar(contexto_invalido):
    try:
        analyzer.validar_calificaciones(contexto_invalido["lista"])
        contexto_invalido["error"] = None
    except ValueError as e:
        contexto_invalido["error"] = e

@then('se debe lanzar una excepcion de valor invalido')
def excepcion_de_valor_invalido(contexto_invalido):
    assert contexto_invalido["error"] is not None
    assert isinstance(contexto_invalido["error"], ValueError)
