# Documentación de Diseño

## Visión General

CryptoTracker es una aplicación diseñada para realizar un seguimiento de las criptomonedas y ayudar a los usuarios a gestionar sus carteras de inversiones. La aplicación proporciona una interfaz simple para agregar y visualizar información sobre diferentes criptomonedas y el valor total de la cartera.

## Arquitectura

La aplicación sigue una arquitectura modular que facilita la extensión y mantenimiento del código. La estructura del paquete Python se organiza de la siguiente manera:

- **`crypto_tracker/`:** El punto de entrada de la aplicación y archivo principal `main.py`.
- **`crypto_tracker/modules/`:** Contiene módulos específicos para manejar monedas y carteras.
- **`crypto_tracker/utils.py`:** Módulo de utilidades con funciones auxiliares.

## Funcionalidades Principales

1. **Seguimiento de Criptomonedas:** Los usuarios pueden agregar nuevas criptomonedas con información detallada, incluyendo nombre, símbolo y precio actual.

2. **Gestión de Cartera:** Permite a los usuarios gestionar sus carteras, agregar o eliminar criptomonedas, y ver el valor total de la cartera en tiempo real.

3. **Interfaz de Usuario Intuitiva:** La interfaz de usuario se centra en la simplicidad y la facilidad de uso para atraer tanto a usuarios novatos como a expertos en criptomonedas.

4. **Persistencia de Datos:** La aplicación utiliza un enfoque simple de almacenamiento en memoria, pero está diseñada para admitir futuras expansiones, como la integración de bases de datos.

## Dependencias

Las dependencias del proyecto se encuentran en el archivo `requirements.txt`. Asegúrate de tener estas dependencias instaladas antes de ejecutar la aplicación.

```bash
pip install -r requirements.txt
Ejecución
Para ejecutar la aplicación, utiliza el siguiente comando:

bash
Copy code
python src/crypto_tracker/main.py
Pruebas Automatizadas
Se han implementado pruebas automatizadas utilizando el marco de pruebas pytest. Estas pruebas se encuentran en el directorio tests/.

Para ejecutar las pruebas, utiliza el siguiente comando:

bash
Copy code
pytest
Contribuciones
¡Agradecemos las contribuciones! Si deseas contribuir al desarrollo de CryptoTracker, sigue las directrices de contribución.

Problemas Conocidos
La aplicación actualmente no maneja las tasas de cambio ni consideraciones fiscales. Estos aspectos están planeados para futuras versiones.
Mejoras Futuras
Integración con servicios de tasas de cambio en tiempo real.
Funcionalidades avanzadas de análisis de cartera.
Historial de Cambios
Consulta el archivo CHANGELOG.md para conocer las actualizaciones y cambios realizados en cada versión.
