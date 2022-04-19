# Extraer frecuencias de fonemas en un texto
El siguiente script toma la transcripción fonética ancha de un texto en español y extrae información de apariones y frecuencias de sus elementos. La transcripción no debe incluir paravocales, puestos que no están incluidas en el cómputo.

## Referencia/Cómo citar
Casado-Mancebo, Mario (2022). Extraer frecuencias de fonemas en un texto. [Script de Python]. https://github.com/mario-casado-m/frec-fon.

## Dependencias
No se necesita ninguna dependencia extra aparte del propio Python 3.

## Ejecución
Para ejecutar el script, debes incluir en la carpeta del proyecto un archivo llamado ``transcripcion.txt`` con la transcripción fonética ancha del texto. Abre una terminal del sistema en la carpeta del proyecto y ejecuta el comando ``python3 script.py``.

## Resultado
Como resultado de la ejecución aparecerá un archivo llamado ``data.txt`` con la siguiente información:
- __total__: el número total de segmentos en la transcripción
- __consonantes__: dos columnas. La primera, el total de consonantes en la transcripción; la segunda, el porcentaje que representan en el total de segmentos.
- __vocales__: dos columnas. La primera, el total de vocales en la transcripción; la segunda, el porcentaje que representan en el total de segmentos. En esta cuenta solo se incluyen los segmentos a, e, i, o, u.
- un desglose de frecuencias por segmento con tres columnas: la primera, la etiqueta del segmento; la segunda, su frecuencia absoluta en la transcripción; y la tercera, el porcentaje que representa del total.

El archivo ``data.txt`` está en formato tabulado, de modo que se puede visualizar cómodamente en cualquier procesador de hojas de cálculo para operar cómodamente ocn los resultados.
