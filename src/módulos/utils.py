# crypto_tracker/módulos/utils.py

def validar_numero_positivo(valor, nombre_variable):
    """
    Valida que el valor sea un número positivo.

    Args:
        valor (str): El valor a validar.
        nombre_variable (str): El nombre de la variable para mensajes de error.

    Returns:
        float: El valor convertido a float si es válido.

    Raises:
        ValueError: Si el valor no es un número válido o es negativo.
    """
    try:
        valor = float(valor)
        if valor >= 0:
            return valor
        else:
            raise ValueError(f"{nombre_variable} debe ser un número positivo.")
    except ValueError:
        raise ValueError(f"{nombre_variable} debe ser un número válido.")

def formatear_dinero(cantidad):
    """
    Formatea una cantidad de dinero con dos decimales.

    Args:
        cantidad (float): La cantidad de dinero.

    Returns:
        str: La cantidad de dinero formateada.
    """
    return f"${cantidad:.2f}"

def generar_nombre_unico(prefijo, sufijo):
    """
    Genera un nombre único concatenando un prefijo y un sufijo.

    Args:
        prefijo (str): El prefijo del nombre.
        sufijo (str): El sufijo del nombre.

    Returns:
        str: El nombre único generado.
    """
    return f"{prefijo}_{sufijo}"

# Puedes agregar más funciones útiles según las necesidades de tu aplicación.
