# Nivel 2 — OpenCV fundamental

**Laboratorio de Tecnologías de la Imagen Digital — IFTS24**
Matías Barreto, 2026

El procesamiento clásico de imágenes: operaciones sobre cada píxel, sobre sus vecinos y sobre las formas. Este nivel responde cómo mejorar, limpiar y segmentar una imagen, y cómo medir lo que se segmentó.

> **Estado: en preparación.** La tabla describe la secuencia planificada y el material existente que se va a reescribir para cada cuaderno.

---

## Contenido planificado

| Cuaderno | Tema | Funciones principales | Material de base |
|---|---|---|---|
| `001_contraste` | Brillo y contraste lineal, ecualización global, por canal y sobre V, CLAHE | `convertScaleAbs`, `equalizeHist`, `createCLAHE` | taller `cv2/01` §6-7 y `cv2/03`; `001_intro/archivo/002/007` parte 4 |
| `002_color` | Segmentación por color con rangos y máscaras | `inRange`, `bitwise_and`, `bitwise_or`, `bitwise_not` | taller `cv2/01` §8-11; `001_intro/archivo/002/006` y `008` |
| `003_geometria` | Rotación en cualquier ángulo, transformaciones afines y corrección de perspectiva | `getRotationMatrix2D`, `warpAffine`, `getPerspectiveTransform`, `warpPerspective` | taller `cv2/04` §4 y §6 |
| `004_filtros` | Ruido gaussiano y sal y pimienta; filtros de suavizado | `blur`, `GaussianBlur`, `medianBlur`, `bilateralFilter` | taller `cv2/05` parte 1 |
| `005_bordes` | Gradiente, Sobel, Laplaciano y Canny | `Sobel`, `Laplacian`, `Canny` | **Nuevo en OpenCV.** Referencias: `001_intro/archivo/002/003` §3 y el cuaderno de bordes en scikit-image del bloque de fundamentos |
| `006_umbral` | Umbral global, Otsu y umbral adaptativo | `threshold`, `adaptiveThreshold` | taller `cv2/06` parte 1; `001_intro/archivo/002/003` §4 |
| `007_morfologia` | Erosión, dilatación, apertura y clausura | `erode`, `dilate`, `morphologyEx` | taller `cv2/06` parte 2 |
| `008_contornos` | Contornos y sus medidas: área, perímetro, caja, centroide | `findContours`, `contourArea`, `arcLength`, `boundingRect`, `moments` | taller `cv2/07`; `001_intro/archivo/002/006` §3 |
| `009_restauracion` | Inpainting con Telea y Navier-Stokes | `inpaint` | taller `cv2/05` parte 2 |

**Evaluación del nivel:** trabajo integrador de mejora y restauración de imágenes (tres casos, dos estrategias por caso, elección justificada), a partir del TFI 1 de la cursada 2026 anterior.

---

## Relación con el nivel de introducción

- El histograma con `cv2.calcHist` ya se presenta en `001_intro/005_resolucion`; `001_contraste` lo retoma para leer el efecto de la ecualización.
- El formato de caja `(x, y, ancho, alto)` de `001_intro/006_anotacion` es el que devuelve `cv2.boundingRect` en `008_contornos`.

---

## Entorno

Python 3.12 y `uv`. Desde esta carpeta:

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
```
