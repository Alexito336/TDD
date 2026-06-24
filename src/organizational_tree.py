class EmpleadoNodo:
    def __init__(self, nombre, puesto, email=None):
        self.nombre = nombre
        self.puesto = puesto
        self.email = email
        self.subordinados = []

    def agregar_subordinado(self, nodo_empleado):
        self.subordinados.append(nodo_empleado)

class EmpresaArbol:
    def __init__(self, raiz: EmpleadoNodo):
        self.raiz = raiz

    def mostrar_estructura(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        indentacion = "    " * nivel
        prefijo = "└── " if nivel > 0 else ""
        email_str = f" ({nodo.email})" if nodo.email else " [⚠️ SIN EMAIL]"
        print(f"{indentacion}{prefijo}{nodo.nombre} - {nodo.puesto}{email_str}")
        for sub in nodo.subordinados:
            self.mostrar_estructura(sub, nivel + 1)

    def buscar_empleado(self, nombre, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo.nombre.lower() == nombre.lower():
            return nodo
        for sub in nodo.subordinados:
            resultado = self.buscar_empleado(nombre, sub)
            if resultado:
                return resultado
        return None

    def contar_total(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        total = 1
        for sub in nodo.subordinados:
            total += self.contar_total(sub)
        return total

    def calcular_profundidad(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if not nodo.subordinados:
            return 1
        return 1 + max(self.calcular_profundidad(sub) for sub in nodo.subordinados)

    def buscar_sin_email(self, nodo=None, acumulados=None):
        if acumulados is None:
            acumulados = []
        if nodo is None:
            nodo = self.raiz
        if nodo.email is None:
            acumulados.append((nodo.nombre, nodo.puesto))
        for sub in nodo.subordinados:
            self.buscar_sin_email(sub, acumulados)
        return acumulados

def inicializar_empresa():
    ceo = EmpleadoNodo("Alejandro Silva", "Director General", "alex.silva@empresa.com")
    empresa = EmpresaArbol(ceo)
    g1 = EmpleadoNodo("Carlos Mendoza", "Gerente de TI", "carlos.m@empresa.com")
    g2 = EmpleadoNodo("Beatriz Ramos", "Gerente de Operaciones")
    g3 = EmpleadoNodo("Diana Perez", "Gerente de Recursos Humanos", "diana.p@empresa.com")
    ceo.agregar_subordinado(g1)
    ceo.agregar_subordinado(g2)
    ceo.agregar_subordinado(g3)
    conteo_empleado = 1
    for i, gerente in enumerate([g1, g2, g3], start=1):
        for j in range(1, 3):
            sup = EmpleadoNodo(f"Supervisor {i}.{j}", f"Supervisor Area {i}", f"sup_{i}{j}@empresa.com")
            gerente.agregar_subordinado(sup)
            for k in range(1, 3):
                email_emp = f"emp{conteo_empleado}@empresa.com" if conteo_empleado != 5 else None
                emp = EmpleadoNodo(f"Empleado {conteo_empleado}", "Operativo", email_emp)
                sup.agregar_subordinado(emp)
                conteo_empleado += 1
    return empresa

if __name__ == "__main__":
    mi_empresa = inicializar_empresa()
    print("=========================================================")
    print("             ORGANIZATIONAL TREE EXPLORER                ")
    print("=========================================================\n")
    print("--- ESTRUCTURA ORGANIZACIONAL COMPLETA ---")
    mi_empresa.mostrar_estructura()
    print("-" * 57)
    total = mi_empresa.contar_total()
    profundidad = mi_empresa.calcular_profundidad()
    sin_correo = mi_empresa.buscar_sin_email()
    num_areas = len(mi_empresa.raiz.subordinados)
    promedio_por_area = round((total - 1) / num_areas, 2)
    print(f"\n--- ESTADÍSTICAS GENERALES ---")
    print(f"• Total de empleados registrados : {total}")
    print(f"• Profundidad máxima del árbol   : {profundidad} niveles")
    print(f"• Promedio de personal por área  : {promedio_por_area}")
    print(f"\n--- ALERTAS DE DATOS PENDIENTES ---")
    print(f"Empleados sin correo electrónico registrado ({len(sin_correo)}):")
    for nombre, puesto in sin_correo:
        print(f"  ⚠️ {nombre} [{puesto}]")
    print(f"\n--- PRUEBA DE BÚSQUEDA ---")
    busqueda = "Empleado 5"
    resultado = mi_empresa.buscar_empleado(busqueda)
    if resultado:
        email_res = resultado.email if resultado.email else "No registrado"
        print(f"✅ Localizado: {resultado.nombre} | Puesto: {resultado.puesto} | Email: {email_res}")
    print("=========================================================")
