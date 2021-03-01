from decorator import consulta_frontera

@consulta_frontera
def consulta_pais(pais = None):
    return "Ese país no está en Suramérica!"

print(consulta_pais("col"))