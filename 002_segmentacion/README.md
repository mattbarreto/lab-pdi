# Prácticas Guiadas de Segmentación y Operaciones Básicas

**Laboratorio de Tecnologías de la Imagen Digital — IFTS N.º 24**  
Prof. Matías Barreto · Ciclo lectivo 2026

---

## Qué vas a hacer acá

Un recorrido de 8 prácticas guiadas paso a paso para dominar la manipulación de imágenes digitales con OpenCV, el trabajo en espacios de color (RGB y HSV), el muestreo y cuantización, y la segmentación por color aplicada sobre imágenes reales y propias.

---

## Cuadernos de la unidad

| # | Cuaderno | Foco principal |
|---|---|---|
| 01 | `01_entorno_y_librerias.ipynb` | Comparación de representación entre OpenCV, Matplotlib, PIL y scikit-image |
| 02 | `02_imagenes_color_y_canales.ipynb` | Descomposición en canales, conversión a escala de grises y espacio HSV |
| 03 | `03_operaciones_basicas_opencv.ipynb` | Geometría: recorte matricial (ROI), redimensionado e interpolaciones |
| 04 | `04_muestreo_y_cuantizacion.ipynb` | Resolución espacial (submuestreo) y resolución radiométrica (reducción de bits) |
| 05 | `05_practica_guiada.ipynb` | Integración: pipeline de lectura, mejora, segmentación y conteo de regiones |
| 06 | `06_segmentacion_color.ipynb` | Segmentación por color con máscaras booleanas y operaciones bitwise en HSV |
| 07 | `07_imagenes_propias.ipynb` | Preprocesamiento, normalización y análisis de una imagen capturada por vos |
| 08 | `08_actividad_integradora.ipynb` | Desafío final integrador: diseño autónomo de segmentación por color |

---

## Entorno e instalación

Desde esta carpeta:

```bash
uv venv --python 3.12
```

Activá el entorno:
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
* **macOS / Linux:** `source .venv/bin/activate`

Instalá las dependencias:
```bash
uv pip install -r requirements.txt
```

Abrí la carpeta en **Visual Studio Code**, abrí el cuaderno correspondiente y seleccioná el kernel `.venv/`.
