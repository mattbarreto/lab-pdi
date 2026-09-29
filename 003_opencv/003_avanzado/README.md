# Nivel 3 — OpenCV avanzado

**Laboratorio de Tecnologías de la Imagen Digital — IFTS24**
Matías Barreto, 2026

De la imagen a la escena: encontrar algo dentro de una imagen, relacionar dos imágenes entre sí y procesar secuencias de video. Este nivel prepara el paso a la visión artificial aplicada con modelos.

> **Estado: en preparación.** La mayor parte de este nivel es material nuevo; la tabla indica qué se reutiliza y qué hay que construir.

---

## Contenido planificado

| Bloque | Cuaderno | Tema | Funciones principales | Material de base |
|---|---|---|---|---|
| Detección | `001_plantillas` | Búsqueda por plantilla | `matchTemplate`, `minMaxLoc` | taller `cv2/08` parte 1 |
| Detección | `002_rostros` | De las cascadas de Haar a detectores con redes neuronales; desenfoque de privacidad | `CascadeClassifier`, `FaceDetectorYN`, `cv2.dnn` | taller `cv2/08` partes 2 y 3 (Haar). **La parte con redes neuronales es nueva** |
| Correspondencias | `003_puntos_clave` | Puntos clave, descriptores y emparejamiento | `ORB_create`, `detectAndCompute`, `BFMatcher` | **Nuevo** |
| Correspondencias | `004_homografia` | Homografía con RANSAC: alinear un documento, panorama simple | `findHomography`, `warpPerspective` | **Nuevo**; retoma la perspectiva de `002_fundamental/003_geometria` |
| Video | `005_video` | Leer y escribir video; procesamiento cuadro por cuadro | `VideoCapture`, `VideoWriter` | **Nuevo**; el bucle de captura aparece sin desarrollar en el módulo de visión artificial aplicada de la cursada anterior |
| Video | `006_movimiento` | Diferencia entre cuadros, sustracción de fondo y flujo óptico | `absdiff`, `createBackgroundSubtractorMOG2`, `calcOpticalFlowPyrLK` | **Nuevo** |

---

## Decisiones pendientes

- **Versión de OpenCV.** Con `opencv-python` 4.14 están disponibles tanto `cv2.CascadeClassifier` como `cv2.FaceDetectorYN` (verificado en 2026-09). OpenCV 5.0 quitó `CascadeClassifier` de Python. Hay que decidir si este nivel mantiene el rango `<5` o migra, y verificar la descarga y la licencia del modelo YuNet que usa `FaceDetectorYN`.
- **Fuentes de video.** Definir si los cuadernos usan la cámara web o archivos de video de ejemplo, para que puedan ejecutarse completos en cualquier computadora.

---

## Relación con los otros niveles

- Las cajas que dibuja `001_intro/006_anotacion` son el formato de salida de los detectores de este nivel.
- La corrección de perspectiva con cuatro puntos elegidos a mano (`002_fundamental`) se vuelve automática con puntos clave y homografía.
- El bucle de video conecta con MediaPipe y con los modelos de visión artificial de los módulos siguientes de la materia.

---

## Entorno

Python 3.12 y `uv`. Desde esta carpeta:

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
```
