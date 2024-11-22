#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 13:13:26 2024

@author: Alexis Godinez
"""


# Tamaño de la matrix 48x48

# 0 Rojo
# 1 Verde
# 2 Azul

import matplotlib.pyplot as plt
import numpy as np
from skimage import io, exposure, transform, img_as_ubyte
from sklearn.cluster import KMeans
from PIL import Image
import datetime
import os
import imageio



def create_mosaic(img_rgb,n,m,name):
	
	# Crea ruta para guardar imágenes
	fecha_actual = datetime.datetime.now()
	dateAndTime = fecha_actual.strftime('%Y%m%d %H%M%S')
	ruta = './' + name + ' ' + dateAndTime
	ruta_img = ruta + '/bloques'
	ruta_pdf = ruta + '/pdf'
	os.mkdir(ruta)
	os.mkdir(ruta_img)
	os.mkdir(ruta_pdf)
	

	def loop_img(img2Lego,n,name):
		lego_color_yellow = np.array([[0, 0, 0],
								[86, 86, 86],
								[150, 150, 150],
								[242, 202, 70],
								[242, 202, 70]])
		
		lego_color_without_yellow = np.array([[0, 0, 0],
								[86, 86, 86],
								[150, 150, 150],
								[150, 150, 150],
								[255, 255, 255]])
		
		lego_color_all = np.array([[0, 0, 0],
								[86, 86, 86],
								[150, 150, 150],
								[242, 202,  70],
								[255, 255, 255]])
		
		if n == 5:
			c = sustituir_colors(img2Lego,lego_color_yellow)
			plt.imshow(c)
			plt.savefig(ruta_pdf + "/" + name + "1_1.pdf")
			create_portrait(c, name + "1_1.pdf")

			
			c = sustituir_colors(img2Lego,lego_color_without_yellow)
			plt.imshow(c)
			plt.savefig(ruta_pdf + "/" + name + "1_2.pdf")
			create_portrait(c, name + "1_2.pdf")

			
			c = sustituir_colors(img2Lego,lego_color_all)
			plt.imshow(c)
			plt.savefig(ruta_pdf + "/" + name + "1_3.pdf")
			create_portrait(c, name + "1_3.pdf")
		else:
			plt.imshow(img2Lego)
			plt.savefig(ruta_pdf + "/" + name + "1_3.pdf")
			create_portrait(img2Lego, name + "1.pdf")

	def create_portrait(img_resized, name):

		unique_colors = np.unique(img_resized.reshape(-1, img_rgb.shape[2]), axis=0)
		
		colores_ordenados = sorted(unique_colors, key=calcular_luminosidad)
		
		for i in range(0,len(colores_ordenados)):
			#print(i)
			bloque_lego(unique_colors[i],str(i))
			
		# Cargar la imagen
		img = Image.open(ruta_img + "/0.jpg")
		
		# Obtener las dimensiones de la imagen
		img_width, img_height = img.size
			
		# Definir el tamaño del tapiz
		rows, cols = len(img_resized), len(img_resized)
		tapiz_width = img_width * cols
		tapiz_height = img_height * rows
		
		# Crear una imagen nueva con el tamaño del tapiz
		tapiz = Image.new('RGB', (tapiz_width, tapiz_height))
		
		
		for x in range(0, len(img_resized)):
			for y in range(0, len(img_resized)):
				for i in range(0, len(colores_ordenados)):
					if (img_resized[x][y] == colores_ordenados[i]).all():
						# Cargar la imagen
						img = Image.open(ruta_img + '/' + str(i) + ".jpg")
						
						# Calcular la posición de la imagen en el tapiz
						j = x * img_width
						i = y * img_height
						# Pegar la imagen en la posición calculada
						tapiz.paste(img, (i, j))
		
		# Guardar el tapiz resultante
		tapiz.save(ruta + "/" + name + ".jpg")

	# Sustiuir colores 
	def sustituir_colors(img_paleta, lego_color):
		
		unique_colors = np.unique(img_paleta.reshape(-1, img_rgb.shape[2]), axis=0)
		
		c = img_paleta.copy()
		
		colores_ordenados = sorted(unique_colors, key=calcular_luminosidad)
		
		for x in range(0, len(img_paleta)):
			for y in range(0, len(img_paleta)):
				for i in range(0, len(colores_ordenados)):
					if (img_paleta[x][y] == colores_ordenados[i]).all():
						c[x][y] = lego_color[i]
						
		return c

	# Reduce colores a n colores
	def paleta(imagen,num_colors):
		# Convertir la imagen en un arreglo de píxeles (Nx3 donde N es el número de píxeles)
		pixels = imagen.reshape((-1, 3))
		
		# Kmeans
		kmeans = KMeans(n_clusters=num_colors, random_state=42).fit(pixels)
		palette = kmeans.cluster_centers_  # Paleta de colores (arreglo de 16x3)
		labels = kmeans.labels_  # Etiquetas de cada píxel (mapa de índices)

		# Reemplazar cada píxel con el color de la paleta correspondiente
		indexed_pixels = palette[labels].reshape(imagen.shape)

		# Convertir el arreglo de nuevo en una imagen y desnormalizar (de [0,1] a [0,255])
		# Convertir a uint8 para guardar como imagen
		indexed_pixels_ubyte = img_as_ubyte(indexed_pixels)
		#image_indexed = Image.fromarray(indexed_pixels_ubyte)

		# Guardar la imagen resultante
		#image_indexed.save(ruta + '/img_indexed_kmeans.jpg')

		# Opcional: Mostrar la imagen resultante
		#image_indexed.show()
		
		return indexed_pixels_ubyte


	# Calcula la luminosidad de un colore RGB para poder ordenarlos
	def calcular_luminosidad(color):
		r, g, b = color
		return 0.2126 * r + 0.7152 * g + 0.0722 * b


	def bloque_lego(new_color,name):
		lego_white = io.imread("bloques/blanco.jpg")
		lego_black = io.imread("bloques/negro.jpg")
		#plt.imshow(lego_black)
		
		luminosidad = calcular_luminosidad(new_color)
		#print(luminosidad)
		
		if luminosidad < 10:
			# Eliminar el canal alfa (si existe)
			if lego_black.shape[-1] == 4:
				lego_black = lego_black[:, :, :3]  # Mantener solo los tres primeros canales (RGB)


			# Guardar la imagen como JPG
			imageio.imwrite(ruta_img+'/'+name+'.jpg', lego_black, format='jpg')
			
			return lego_black
		else:
			# Verificar si la imagen tiene 4 canales (RGBA) y ajustar el nuevo color
			if lego_white.shape[-1] == 4:
				new_color = np.append(new_color,255)  # Verde con opacidad completa
			
			# Crear una nueva imagen con el color deseado, asegurando que sea del tipo uint8
			imagen_coloreada = np.ones_like(lego_white, dtype=np.uint8) * new_color
			
			# Para evitar la advertencia, puedes modificar ligeramente el brillo usando la luminosidad de la imagen original
			luminosidad = np.mean(lego_white, axis=-1, keepdims=True) / 255.0
			imagen_coloreada = (imagen_coloreada * luminosidad).astype(np.uint8)
			
			# Si la imagen original es RGBA, convertir a RGB antes de guardar como JPG
			if lego_white.shape[-1] == 4:
				imagen_coloreada = imagen_coloreada[:, :, :3]
			
			# Guardar la nueva imagen como JPG
			io.imsave(ruta_img+'/'+name+'.jpg', imagen_coloreada)
			
			#plt.imshow(imagen_coloreada)
		
			return imagen_coloreada


	# Escalar imagen
	img_resized = transform.resize(img_rgb, (m, m))
	
	# Aumentar el contraste
	img_contrast = exposure.equalize_hist(img_rgb)
	
	#  Imagen alto contraste escalada
	img_contrast_resized = exposure.equalize_hist(img_resized)
	
	# Imagen escalada alto contrastes \
	img_resized_contrast = transform.resize(img_contrast, (m, m))
	
	a1 = paleta(img_resized,n)
	a2 = paleta(img_contrast_resized,n)
	a3 = paleta(img_resized_contrast,n)
	
	loop_img(a1,n,name+'_1_')
	loop_img(a2,n,name+'_2_')
	loop_img(a3,n,name+'_3_')

if __name__ == "__main__":

	#Prueba 1
	# Valores por defecto
	num_colores = 5
	dimension_img = 48
	#dim_img = 192

	#num_col = 1000
	#dim_img = 300

	# Leer imagen
	img_rgb = io.imread("Test1.jpg")

	create_mosaic(img_rgb,num_colores,dimension_img,'Test')

