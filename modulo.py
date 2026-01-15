provincias = ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga", "Sevilla"]

def calcular_iva(precio, iva=21):
    return precio * (iva / 100)

def aplicar_descuento(precio, descuento):
    return precio - (precio * (descuento / 100))

def buscar_provincia(nombre):
    for provincia in provincias:
        if provincia.lower() == nombre.lower():
            return provincia
    return None