# Nivel 1 — Introducción a OpenCV

**Laboratorio de Tecnologías de la Imagen Digital — IFTS24**
Matías Barreto, 2026

Este nivel traduce a OpenCV lo que ya saben hacer con NumPy y scikit-image, y agrega las decisiones que toda imagen exige antes de analizarla: cómo se lee, cómo se guarda, cómo se encuadra y cómo se anota. Cierra con un script que genera la ficha técnica de una imagen propia.

---

## Contenido

| Cuaderno | Tema | Producto |
|---|---|---|
| `001_traduccion` | De scikit-image a OpenCV: `imread`, orden BGR, banderas de lectura y orientación EXIF | Función `leer_imagen_rgb` |
| `002_canales` | Escala de grises, `split` y `merge`, espacio HSV y traducción de escalas | Figura comparativa RGB, grises y HSV |
| `003_archivos` | PNG, BMP, JPEG y WEBP: peso, fidelidad, artefactos y recompresión | Tabla de peso y diferencia por formato |
| `004_encuadre` | Recorte y vistas de NumPy, `resize`, proporción, interpolación, `flip` y `rotate` | Miniatura con criterio escrito |
| `005_resolucion` | Muestreo espacial, cuantización, `np.unique` y `cv2.calcHist` | Comparación de las dos pérdidas |
| `006_anotacion` | Coordenadas `(x, y)`, dibujo sobre copias, color según el orden de canales, texto | Imagen anotada con cajas y etiquetas |
| `007_ficha` | Integrador: ficha técnica de una imagen propia y script autónomo | `ficha_imagen.py` |

Los cuadernos están pensados para recorrerse en orden. Cada uno puede ejecutarse completo con **Restart Kernel and Run All Cells**.

---

## Cómo descargar esta carpeta

Para bajar solo este nivel sin clonar todo el repositorio:

1. Abran en GitHub la carpeta `003_opencv` (no solo `001_intro`: los cuadernos necesitan también la carpeta `imagenes`).
2. Copien la dirección de esa página.
3. Péguenla en [download-directory.github.io](https://download-directory.github.io/) y descarguen el archivo ZIP.
4. Descompriman el ZIP y verifiquen que `imagenes` y `001_intro` quedaron una al lado de la otra.

---

## Configuración del entorno local

1. **Instalar uv** siguiendo las instrucciones de [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/).
2. **Crear el entorno virtual** desde esta carpeta:

   ```bash
   uv venv --python 3.12
   ```

3. **Activarlo:**

   ```bash
   # Windows
   .venv\Scripts\activate
   # macOS y Linux
   source .venv/bin/activate
   ```

4. **Instalar las dependencias:**

   ```bash
   uv pip install -r requirements.txt
   ```

5. **Abrir los cuadernos** en **Visual Studio Code**, abrí cualquiera de los cuadernos y seleccioná el kernel de `.venv`.

| Escenario | Comando |
|---|---|
| Proyecto con `pyproject.toml` | `uv sync` |
| Proyecto solo con `requirements.txt` (este caso) | `uv pip install -r requirements.txt` |

---

## Archivos que generan los cuadernos

`003_archivos`, `006_anotacion` y `007_ficha` escriben resultados en una carpeta `salidas/` dentro de este nivel. Esa carpeta no forma parte del repositorio: se puede borrar y se vuelve a crear al ejecutar los cuadernos.

Para usar una foto propia en `007_ficha`, cópienla a esta carpeta y escriban su nombre en `RUTA_IMAGEN_PROPIA`. Si la foto muestra personas reconocibles, no la suban a un repositorio público sin su consentimiento.
