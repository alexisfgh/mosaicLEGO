
# LEGO Mosaic Maker en Python

Este proyecto es una alternativa al servicio oficial de LEGO Mosaic Maker ([LEGO Mosaic Maker](https://www.lego.com/es-us/product/mosaic-maker-40179)), que permite convertir imágenes en mosaicos estilo LEGO. El programa está escrito en Python y permite una gran flexibilidad, no solo en el número de colores utilizados en el mosaico, sino también en las dimensiones del mismo.

## Descripción

El código en Python toma una imagen JPG cuadrada como entrada y crea un mosaico visual similar al generado por el LEGO Mosaic Maker. A diferencia del servicio oficial de LEGO, que por defecto usa 4 o 5 colores, este programa permite al usuario elegir **n** colores. Además, el código permite modificar las dimensiones del mosaico, siendo 48x48 bloques el valor por defecto (al igual que LEGO Mosaic Maker), pero cualquier tamaño es posible.

### ¿Cómo funciona?

El programa sigue los siguientes pasos para generar el mosaico de LEGO:

1. **Redimensionado de la imagen**: La imagen de entrada (de dimensiones cuadradas) se ajusta a las dimensiones de bloque proporcionadas por el usuario. El tamaño por defecto es de 48x48 bloques.

2. **Saturación y vecindad**: El código utiliza técnicas de procesamiento de imágenes para saturar la imagen y obtener una paleta de colores representativa. Esto se hace con un proceso de clustering, donde se agrupan los colores de la imagen en un número de grupos (colores).

3. **Cálculo de colores**: Usando el algoritmo de **K-Means Clustering**, el programa obtiene el vector de colores (por defecto 5 colores), pero puedes ajustar este parámetro para trabajar con más colores si lo deseas. Los colores seleccionados son ordenados por luminosidad para asegurar que la imagen final tenga coherencia visual.

4. **Generación del mosaico**: Una vez que se tiene la imagen redimensionada y los colores ordenados, se genera la imagen final del mosaico. Además, se crean versiones del mosaico con diferentes combinaciones de bloques LEGO, que son almacenadas en carpetas organizadas por el nombre, fecha y hora.

## Características

- Convierte imágenes JPG cuadradas en mosaicos estilo LEGO.
- Permite elegir el número de colores para el mosaico (5 colores).
- Personaliza la dimensión del mosaico (por defecto 48x48 bloques, pero cualquier dimensión es posible).
- Realiza un procesamiento de la imagen para obtener una paleta de colores mediante técnicas de clustering (K-Means).
- Ordena los colores por luminosidad para garantizar una representación coherente.
- Genera versiones del mosaico y los guarda en carpetas con el nombre de la fecha y hora.

## Requisitos Previos

Este proyecto está diseñado para ser ejecutado en Python 3.x. Antes de usar el programa, asegúrate de tener los siguientes paquetes instalados:

- `matplotlib`
- `numpy`
- `scikit-image`
- `scikit-learn`
- `Pillow`
- `imageio`

Para instalarlos, puedes usar `pip`:

```bash
pip install matplotlib numpy scikit-image scikit-learn pillow imageio
```

## Instalación y Uso

1. Clona este repositorio o descarga el código fuente.
2. Coloca la imagen cuadrada (la imagen siempre debe ser cuadrada) en formato JPG que deseas convertir en mosaico.
3. Configura la dimensión y el número de colores deseados.
3. Ejecuta el script `mosaic.py` desde tu terminal o entorno de desarrollo.

```bash
python mosaic.py
```

### Parámetros Personalizables

El código permite personalizar varios parámetros clave:

- **Imagen de entrada**: Ruta de la imagen JPG cuadrada que se desea convertir en mosaico.
- **Número de colores**: Se puede especificar el número de colores para el mosaico. Por defecto, el programa maneja 4 o 5 colores, pero puedes ajustar este número.
- **Dimensiones del mosaico**: Por defecto, el tamaño es 48x48 bloques de LEGO, pero puedes ajustar las dimensiones a cualquier tamaño que necesites.

## Ejemplo de Uso

Si tienes una imagen llamada `ejemplo.jpg` que deseas convertir en un mosaico de 5 colores y con una dimensión de 32x32 bloques:

1. Ajusta los parámetros en el código o en la función principal.
2. Ejecuta el programa.
3. Los resultados se guardarán en una carpeta organizada por fecha y hora, que incluirá:
	- La imagen redimensionada.
	- El mosaico generado.
	- Versiones del mosaico utilizando bloques de LEGO.

## Resultados Generados

El programa crea los siguientes archivos en una carpeta con el nombre de la fecha y hora actuales:

- Una imagen JPG del mosaico generado.
- Imágenes de los bloques LEGO individuales que conforman el mosaico.
- Archivos adicionales con las distintas versiones del mosaico.

## Ejemplos

Al ejecutar el código con los parámetros 5 colores se generan 9 imágenes diferentes por la densidad de los colores y puede escoger la que mejor se adecue.
<figure>
	<img src="/resultados.png" alt="Resultado 5 colores">
	<figcaption>Resultado por defecto con 5 colores.</figcaption>
</figure>

### Resultado con 5 colores y dimensión de 48x48 bloques
<figure>
	<img src="/Test 20241122 134205/Test_1_1_3.pdf.jpg" alt="5 Colores 48 bloques">
	<figcaption>Test1 con 5 colores y dimensión 48x48.</figcaption>
</figure>

### Resultado con 50 colores y dimensión de 96x96 bloques
<figure>
	<img src="/Test 20241122 134250/Test_1_1.pdf.jpg" alt="50 Colores 96 bloques">
	<figcaption>Test1 con 50 colores y dimensión 96x96.</figcaption>
</figure>



## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).


