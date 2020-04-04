print("Asignaturas Optativas Año 2020")
print("Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower() # Para pasar todo a minusculas
 
if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):

    print("asignatura elegida "+ asignatura)

else:

    print("La asigantura no es valida")