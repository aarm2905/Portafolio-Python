# Índice de Discriminación y Dificultad

El índice de discriminación y el índice de dificultad son dos métricas importantes en la evaluación de ítems en pruebas educativas y psicológicas. Aquí te explico cómo calcular ambos índices y te proporcionaré ejemplos de código en Python.

## Índice de Dificultad

El índice de dificultad mide la proporción de estudiantes que respondieron correctamente a un ítem. Se calcula como:

\[ \text{Índice de Dificultad} = \frac{\text{Número de respuestas correctas}}{\text{Número total de respuestas}} \]

Un valor más alto indica que el ítem es más fácil.

## Índice de Discriminación

El índice de discriminación mide cuán bien un ítem diferencia entre estudiantes con alto rendimiento y bajo rendimiento. Una manera común de calcularlo es usando el método del punto biserial:

\[ D = \frac{X_{\text{alto}} - X_{\text{bajo}}}{SD} \]

Donde:

- \( X_{\text{alto}} \) es la media de las puntuaciones de los estudiantes en el grupo superior (generalmente el 27% superior).
- \( X_{\text{bajo}} \) es la media de las puntuaciones de los estudiantes en el grupo inferior (generalmente el 27% inferior).
- \( SD \) es la desviación estándar de las puntuaciones totales del ítem.