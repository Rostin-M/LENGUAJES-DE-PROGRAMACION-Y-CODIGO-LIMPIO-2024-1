## LENGUAJES DE PROGRAMACIÓN Y CÓDIGO LIMPIO 2024-1

### POR:
Rostin Santiago Alzate Montoya y
Miguel Ayala Parra

### ¿Qué es y para qué es?
Este programa calcula la hipoteca inversa en tres casos o modalidades:

- Hipoteca Inversa Temporal
- Hipoteca Inversa Vitalicia
- Hipoteca Inversa Única

### ¿Cómo hacerlo funcionar?
#### Prerrequisitos:
- Python debe estar instalado en tu sistema.

#### Ejecución:
1. Abre una terminal.
2. Navega hasta la carpeta donde se encuentra guardado el proyecto.
3. Ejecuta el programa usando el siguiente comando:
    ```
    python main.py
    ```

### ¿Cómo está hecho?
Este proyecto sigue una arquitectura modular y limpia. Aquí está la estructura del proyecto:

- Carpeta `src`: Contiene el código fuente de la lógica de la aplicación. 
    - Carpeta `console`
        - `__init__.py`: Archivo para que Python reconozca esta carpeta como un módulo.
        - `Menu.py`: Proporciona el menú de la aplicación.
    - Carpeta `logic`
        - `__init__.py`: Archivo para que Python reconozca esta carpeta como un módulo.
        - `Calculations.py`: Contiene las funciones para calcular la hipoteca inversa en diferentes modalidades y algunas verificaciones para ello.
        - `Exceptions.py`: Define las excepciones personalizadas utilizadas en el programa.

- Carpeta `test`: Contiene las pruebas unitarias para el código.
    - `__init__.py`: Archivo para que Python reconozca esta carpeta como un módulo.
    - `Test_Module.py`: Archivo que contiene las pruebas unitarias para el código en `logic`.

### Pruebas
Para ejecutar las pruebas unitarias, desde la carpeta raíz del proyecto, utiliza el siguiente comando en la terminal:

```
python -m unittest discover Test -p '*Test*.py'
```

Con estos pasos, podrás ejecutar y probar la funcionalidad del programa.

#Tener en cuenta que la "Tasa de interés deseada" debe ser mayor o igual a 0.007974
