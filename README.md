# Calculadora Bitwise - Proyecto 1
**Autor:** Jhonny Tintaya  
**Materia:** Estructuras de Datos I (INF220)

## Descripción
Aplicación con interfaz gráfica (Tkinter) desarrollada bajo el patrón **MVC** que permite realizar operaciones lógicas a nivel de bits sobre números enteros.

## Funcionalidades
- **Operaciones Binarias:** AND, OR, XOR (requieren dos números).
- **Operaciones Unarias:** NOT (requiere un número).
- **Desplazamientos:** Left Shift (<<) y Right Shift (>>) indicando la cantidad de bits.
- **Salida Dual:** Los resultados se muestran en formato Decimal y Binario.

## Arquitectura (Patrón MVC)
1. **Modelo (`bit_processor.py`):** Contiene la lógica matemática pura.
2. **Vista (`calculator_view.py`):** Define la interfaz gráfica con Tkinter.
3. **Controlador (`calculator_controller.py`):** Coordina la comunicación entre el modelo y la vista.

## Cómo Ejecutar
1. Tener instalado Python 3.11+.
2. Ejecutar el comando: `python main.py`